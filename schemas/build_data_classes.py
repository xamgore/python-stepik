from importlib import import_module
from pathlib import Path

from jinja2 import Template

from schemas import structure


# template = Template('Hello {{ name }}!')
# print(template.render(name='John Doe'))


def rename_properties(model):
    attrs = model['properties']
    to_rename = {n: prop for n, prop in attrs.items() if 'rename' in prop}
    remove_list = lambda ty: ty[5:-1] if ty.startswith('List[') and ty.endswith(']') else ty

    for name, prop in to_rename.items():
        # need to know, what property is used in rest api
        prop['from'] = name

        # rename "lesson" to "lesson_id"
        attrs[prop['rename']] = prop.copy()
        del attrs[name]

        # extract the inner type, so it could be imported
        prop['type'] = remove_list(prop['new_type'])

        # make "lesson" either method, or list-property
        new_prop_name = 'resources' if prop['new_type'].startswith('List[') else 'methods'
        model[new_prop_name][name] = prop


def import_typings(model):
    """Search for types, used in properties & methods, and get correct imports"""
    import_paths = structure.imports()

    types = set().union(
        {p['type'] for p in model['properties'].values()},
        {p['type'] for p in model['resources'].values()},
        {p['type'] for p in model['methods'].values()})

    return {type: import_paths[type] for type in types.intersection(import_paths.keys())}


def refine_type(p):
    """Get a python type by name of type in schema"""
    ty = p['type']

    if ty.startswith('Optional['):
        return ty
    if ty == 'integer':
        return 'int'
    if ty == 'boolean':
        return 'bool'
    if ty == 'decimal':
        return 'float'
    if ('description' in p) and (p['description'] == 'Enter a valid JSON object'):
        p['description'] = None
        return 'dict' if (p['defaultValue'] == '{}') else 'List'
    if ty == 'dict':
        return ty
    if ty == 'string':
        return 'str'
    if ty.startswith('List['):
        return ty

    # todo: make smart types, like in structure.types()
    if ty:
        p['docstring'] = f"{p['docstring'] or ''}\n\nType: {ty}".lstrip('\n')

    return 'str'


def refine_doc_string_with_default_value(p):
    """Add information about the default value"""
    description = p.get('description', '') or ''
    p['docstring'] = f'{description}\n\nDefault value: ``{p["defaultValue"]}``'.lstrip()


def expand_with_meta_data(model_name, model):
    model_name = model_name.replace('Serializer', '')

    if Path(f'docs/{model_name}.py').exists():
        extension = import_module(f'docs.{model_name}', package=None)

        for prop, attrs in model['properties'].items():
            if prop in dir(extension):
                getattr(extension, prop)(attrs)


def refine_default_value(p):
    """Surround the default value with commas if type equals string"""
    if ('format' in p) and p['format'] == 'string':
        p['defaultValue'] = f'"{p["defaultValue"]}"'


if __name__ == '__main__':
    resources_without_models = []

    for schema in structure.schemas():
        if len(schema['models'].keys()) == 0:
            resources_without_models.append(schema['resourcePath'])
            continue

        for name, model in schema['models'].items():
            model['resources'], model['methods'] = {}, {}
            rename_properties(model)

            for pn, p in model['properties'].items():
                p['docstring'] = p.get('description', None)
                p['type'] = refine_type(p)

                if 'defaultValue' in p:
                    refine_default_value(p)
                    refine_doc_string_with_default_value(p)

            model['imports'] = import_typings(model)

        with open('python-templates/data-class.jinja2') as t:
            output_module = schema["resourcePath"].replace('-', '_')

            with open(f'../{output_module}.py', 'w') as out:
                template = Template(t.read(), lstrip_blocks=True, trim_blocks=True)
                out.write(template.render(models=schema['models']))

    print(f'{len(resources_without_models)} resources without models:', *resources_without_models, sep='\n  ')
