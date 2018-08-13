from jinja2 import Template

from schemas import structure


# template = Template('Hello {{ name }}!')
# print(template.render(name='John Doe'))


def refine_type(p):
    """Get a python type by name of type in schema"""
    ty = p['type']

    if ty == 'integer':
        return 'int'
    if ty == 'boolean':
        return 'bool'
    if ty == 'decimal':
        return 'float'
    if ('description' in p) and (p['description'] == 'Enter a valid JSON object'):
        p['description'] = None
        return 'dict' if (p['defaultValue'] == '{}') else 'List'
    if ty == 'string':
        return 'str'

    # todo: make smart types, like in structure.types()
    if ty:
        p['docstring'] = f"{p['docstring'] or ''}\n\nType: {ty}".lstrip('\n')

    return 'str'


def refine_doc_string_with_default_value(p):
    """Add information about the default value"""
    description = p.get('description', '') or ''
    p['docstring'] = f'{description}\n\ndefault value: {p["defaultValue"]}'.lstrip()


def refine_default_value(p):
    """Surround the default value with commas if type is string"""
    if ('format' in p) and p['format'] == 'string':
        p['defaultValue'] = f'"{p["defaultValue"]}"'


for schema in structure.schemas():
    for model in schema['models'].values():

        for p in model['properties'].values():
            p['docstring'] = p['description']
            p['type'] = refine_type(p)

            if 'defaultValue' in p:
                refine_default_value(p)
                refine_doc_string_with_default_value(p)

    with open('data-class.jinja2') as t:
        with open(f'../{schema["resourcePath"]}.py', 'w') as out:
            template = Template(t.read(), lstrip_blocks=True, trim_blocks=True)
            out.write(template.render(models=schema['models']))
