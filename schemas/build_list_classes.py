import json
from jinja2 import Template

from common import to_camel_case, to_dash_case
from schemas.build_data_classes import main as build_data_classes
from schemas.schema import load_schemas, Schema
from schemas.structure import base_methods, pk_methods


def gen_with_model(schema: Schema) -> str:
    base_route, pk_route = {}, {}
    resource_path = schema.resourcePath

    pk_type = schema.model.properties[schema.model.primary_key].python_type

    # /api/resource methods
    if 'GET' in base_methods[resource_path]:
        global ordering_fields

        fields = [p for p in schema.base_route.get.parameters.values()
                  if p.name != 'pk' and p.name != 'page']

        base_route['GET'] = {
            'pk':               schema.model.primary_key,
            'var':              f'{schema.model.primary_key}s',
            'var_type':         f'Iterable[{ pk_type }]',
            'model_class_name': schema.model.id,
            'base_fields':      fields,
            'ordering_fields':  ordering_fields[schema.resourcePath],
            'resources_plural': schema.resources_name,
        }

    if 'POST' in base_methods[resource_path]:
        global post_required_fields
        fields = post_required_fields.get(resource_path, None)

        if fields is not None:
            base_route['POST'] = {
                'required':         [schema.model.properties.get(p, {'name': p}) for p in fields],
                'other':            [p for p in schema.model.properties.values()
                                     if not (p.readOnly or p.name in fields)],
                'model_class_name': schema.model.id,
                'resource':         to_dash_case(schema.model.id),
                'resources_plural': schema.resources_name,
            }

    # /api/resource/{pk} methods
    if 'GET' in pk_methods[resource_path]:
        pk_route['GET'] = {
            'var':              schema.model.primary_key,
            'var_type':         pk_type,
            'model_class_name': schema.model.id,
        }

    if 'PUT' in pk_methods[resource_path]:
        pk_route['PUT'] = {}  # todo remove required fields and test

    if 'POST' in pk_methods[resource_path]:
        pk_route['POST'] = {}

    if 'DELETE' in pk_methods[resource_path]:
        pk_route['DELETE'] = {
            'var':      schema.model.primary_key,
            'var_type': pk_type,
            'url':      schema.resources_name,
        }

    # global post_required_fields
    # I want to load ordering_fields and fields from base_route
    # order_fields = \
    #     ordering_fields[schema.resourcePath]
    # base_route_fields = \
    #     [p for p in schema.base_route.get.parameters.values() if p.name != 'pk']
    #
    # var_name = schema.possible_model_name.lower()
    # resource_name_as_variable='clazz' if var_name == 'class' else var_name,

    return template_with_model.render(
        name=to_camel_case(schema.resources_name),
        model=schema.model,
        base_route=base_route,
        pk_route=pk_route,
    )


def gen_with_object(schema: Schema) -> str:
    model_id, pk, pk_type, other_post_base_params = 'dict', 'id', 'Any', []
    order_fields = []
    post_base_params = post_required_fields.get(schema.resourcePath, None)
    pk_route = pk_methods[schema.resourcePath]
    base_route = base_methods[schema.resourcePath]
    var_name = schema.possible_model_name.lower()

    output = template_with_model.render(
        name=to_camel_case(schema.resources_name),
        model_id=model_id,
        pk=pk,
        pk_type=pk_type,
        resources_name=schema.resources_name,
        resource_name=to_dash_case(schema.possible_model_name),
        resource_name_as_variable='clazz' if var_name == 'class' else var_name,
        GET_PK='GET' in pk_route,
        POST_PK='POST' in pk_route,
        PUT_PK='PUT' in pk_route,
        DELETE_PK='DELETE' in pk_route,
        GET_BASE='GET' in base_route,
        POST_BASE=('POST' in base_route) and (post_base_params is not None),
        POST_BASE_PARAMS=post_base_params,
        POST_BASE_OTHER_PARAMS=other_post_base_params, )

    return output


if __name__ == '__main__':
    with open(f'schemas/api-refined/metadata/ordering_fields.json') as f:
        ordering_fields = json.load(f)
    with open(f'schemas/api-refined/metadata/required_fields.post.base.json') as f:
        post_required_fields = json.load(f)
    with open('schemas/python-templates/list-of-models.jinja2') as t:
        template_with_model = Template(t.read(), lstrip_blocks=True, trim_blocks=True)
    with open('schemas/python-templates/list-of-objects.jinja2') as t:
        template_with_object = Template(t.read(), lstrip_blocks=True, trim_blocks=True)

    build_data_classes()

    for schema in load_schemas():
        output = gen_with_model(schema) if schema.model else ''  # gen_with_object(schema)
        with open(f'api/{schema.py_module_name}.py', 'a') as f:
            f.write(output)
