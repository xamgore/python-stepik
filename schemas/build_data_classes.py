from copy import copy
from typing import Set, Dict

from jinja2 import Template

from schemas.common import run_once
from schemas.schema import load_schemas, Model, Property, Schema


def rename_properties(model: Model):
    to_rename: Set[Property] = {p for p in model.properties.values() if p.rename}
    remove_list = lambda ty: ty[5:-1] if ty.startswith('List[') and ty.endswith(']') else ty

    for prop in to_rename:
        # which property's name to use in rest api
        prop.api_name = prop.name

        # rename raw property (lessons -> lessons_ids)
        raw_prop = copy(prop)
        raw_prop.name = raw_prop.rename
        del model.properties[prop.api_name]
        model.properties[raw_prop.name] = raw_prop

        # extract the inner type, so it could be imported
        # used in template, i.e. ResourcesList[prop.type]
        prop.type = remove_list(prop.new_type)

        # make "lesson" either method, or list-property
        if prop.new_type.startswith('List['):
            model.resources[prop.name] = prop
        else:
            model.methods[prop.name] = prop


@run_once
def models() -> Dict[str, Model]:
    """Return dict of all models"""
    return {m.id: m for schema in load_schemas() for m in schema.models.values()}


def get_imports_to_types(schema: Schema):
    """Search for types, used in properties & methods, and get correct imports"""
    boxes = [box for m in schema.models.values()
             for box in (m.properties, m.resources, m.methods)]

    models_to_import = {prop.type for box in boxes for prop in box.values()} \
        .intersection(models().keys())

    # TODO topological sort :(
    return {m: f'.{models()[m].schema.py_module_name}' for m in models_to_import}


def improve_doc_string(p: Property):
    """Surround the default value with commas if type equals to string"""
    if p.format == 'string':
        p.defaultValue = f'"{p.defaultValue}"'

    """Add information about the default value"""
    p.docstring = p.description or ''
    if p.defaultValue is not None:
        p.docstring = f'{p.docstring}\n\nDefault value: ``{p.defaultValue}``'.lstrip()

    # todo: make smart types, like in structure.types()
    if p.type not in ['string', 'integer', 'decimal', 'boolean']:
        p.docstring = f"{p.docstring}\n\nType: {p.python_type}".lstrip('\n')


def main():
    template: Template = None
    with open('schemas/python-templates/data-class.jinja2') as t:
        template = template or Template(t.read(), lstrip_blocks=True, trim_blocks=True)

    for schema in load_schemas():
        for model in schema.models.values():
            model.resources, model.methods = {}, {}
            rename_properties(model)

            for prop in model.properties.values():
                improve_doc_string(prop)

        output = template.render(models=schema.models, imports=get_imports_to_types(schema))

        with open(f'stepik/api/{schema.py_module_name}.py', 'w') as out:
            out.write(output)


if __name__ == '__main__':
    main()
