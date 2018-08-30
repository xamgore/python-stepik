import json

from jinja2 import Template

from common import to_camel_case, to_dash_case
from schemas.build_data_classes import main as build_data_classes
from schemas.schema import load_schemas, Model
from schemas.structure import base_methods, pk_methods

if __name__ == '__main__':
    build_data_classes()
    schemas = load_schemas()
    models = {s.resourcePath: m for s in schemas for m in s.models.values()
              if s.resources_name.startswith(to_dash_case(m.id)[:-2])}

    with open('api-refined/metadata/required_fields.post.base.json') as f:
        post_required_fields = json.load(f)

    with open('python-templates/lists-of-models.jinja2') as t:
        template_with_model = Template(t.read(), lstrip_blocks=True, trim_blocks=True)
    # with open('python-templates/lists-of-objects.jinja2') as t:
    #     template_with_object = Template(t.read(), lstrip_blocks=True, trim_blocks=True)

    for schema in schemas:
        post_base_params = post_required_fields.get(schema.resourcePath, None)

        if schema.resourcePath in models:
            model: Model = models[schema.resourcePath]
            model_id, pk = model.id, model.required[0]
            pk_type = model.properties[pk].python_type
            other_post_base_params = [p for p in model.properties.values()
                                      if not p.readOnly and p.name not in (post_base_params or [])]
            if post_base_params is not None:
                post_base_params = [p for p in model.properties.values()
                                    if p.name in post_base_params]
        else:
            model_id, pk, pk_type, other_post_base_params = 'dict', 'id', 'Any', []

        pk_route = pk_methods[schema.resourcePath]
        base_route = base_methods[schema.resourcePath]

        output = template_with_model.render(
            name=to_camel_case(schema.resources_name),
            model_id=model_id,
            pk=pk,
            pk_type=pk_type,
            resources_name=schema.resources_name,
            resource_name=schema.possible_module,
            GET_PK='GET' in pk_route,
            POST_PK='POST' in pk_route,
            PUT_PK='PUT' in pk_route,
            DELETE_PK='DELETE' in pk_route,
            GET_BASE='GET' in base_route,
            POST_BASE=('POST' in base_route) and (post_base_params is not None),
            POST_BASE_PARAMS=post_base_params,
            POST_BASE_OTHER_PARAMS=other_post_base_params,
        )

        with open(f'../api/{schema.py_module_name}.py', 'a') as out:
            out.write(output)
