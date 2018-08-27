from typing import Dict, List, Any

debug = False

def check_other_fields(self, data, ignore: List[str] = None):
    known_fields = (ignore or []) + list(self.__dict__.keys())
    for k, v in data.items():
        if k not in known_fields:
            raise AttributeError(
                f'There is an unknown field "{k}", add it to {self.__class__.__name__} class please')


class Parameter:
    def __init__(self, param: Dict[str, Any]):
        self.paramType = param['paramType']
        self.name = param['name']
        self.description = param.get('description', '')
        self.dataType = param.get('dataType', None)
        self.type = param.get('type', None)
        self.required = param.get('required', False)
        self.defaultValue = param.get('defaultValue', None)
        self.format = param.get('format', None)
        """Same as self.type field"""
        self.enum: List[Any] = param.get('enum', None)
        check_other_fields(self, param)


    @property
    def python_type(self):
        """Return the python type"""
        ty = self.type or self.dataType

        if ty == 'string':
            return 'str'
        if ty == 'integer':
            return 'int'
        if ty == 'boolean':
            return 'bool'
        if ty == 'enum':
            return 'str'  # TODO something with that
        if ty == '':
            return 'bool' if self.name.startswith('is_') else 'Any'
        # TODO: take from model
        raise AttributeError(
            f'There is an unknown type "{ty}", add it to {self.__class__.__name__}.python_type class please')


    def __repr__(self):
        return f'({self.name})'
        # return json.dumps(self.__dict__, indent=2)


class Property:
    def __init__(self, name, prop: Dict[str, Any]):
        self.name = name
        self.description = prop.get('description', None)
        self.type = prop['type']
        self.required = prop.get('required', None)
        self.readOnly = prop.get('readOnly', None)
        self.defaultValue = prop.get('defaultValue', None)
        self.format = prop.get('format', None)
        self.enum: List[Any] = prop.get('enum', None)
        self.rename = prop.get('rename', None)
        self.new_type = prop.get('new_type', None)
        self.items: Dict[str, str] = prop.get('items', None)
        self.deprecated: bool = prop.get('deprecated', None)
        """Contains {"type": "string"}, when self.type equals to \"array\""""

        check_other_fields(self, prop)


class Operation:
    def __init__(self, data):
        self.type: str = data['type']
        self.method: str = data['method']
        """Always GET"""
        self.nickname: str = data['nickname']
        """Resource name + action (retrieve, list, etc)"""
        self.notes: str = data['notes']
        """Short description about the resource"""
        # TODO: use notes when generating list resources
        self.summary: str = data['summary']
        """Short description about the resource. Use ``notes`` instead, it has more text."""
        self.parameters: Dict[str, Parameter] = \
            {p.name: p for p in map(Parameter, data.get('parameters', []))}
        check_other_fields(self, data)

        self.type = self.type[:-len('Serializer')] \
            if self.type.endswith('Serializer') else self.type
        """Model that is used in the route"""


class Route:
    def __init__(self, route, schema):
        self.url: str = route['path']
        self.description: str = route['description']
        self.operations = list(map(Operation, route['operations']))
        check_other_fields(self, route, ignore=['operations', 'path'])

        self.schema: Schema = schema
        self.get = self.operations[0] if self.operations else None
        # self.post = None

        if self.get and self.get.method != 'GET':
            raise AttributeError('Swagger generates only GET methods, need intervention')

        global debug
        if self.get and self.get.type == 'object' and debug:
            print(f'Route {self.url} has type "object", that\'s strange')
            # models_with_names_like_url = \
            #     [m for m in self.schema.models.values() if m.id[:-2] in self.route]
            # if len(models_with_names_like_url) != 1:
            #     raise AttributeError(f'Refine a model, that corresponds to the route {self.url}')
            # self.get.type = models_with_names_like_url[0]


    @property
    def route(self) -> str:
        """
        Url converted to CamelCase

        ``/api/courses/{pk}/distinction`` to ``CoursesDistinction``
        """
        name = self.url.replace('/api/', '', 1).replace('/{pk}', '')
        camel_case = ''.join(map(str.title, name.split('-')))
        return camel_case.replace('/', '')


    @property
    def has_primary_key(self):
        return '{pk}' in self.url


    def __repr__(self):
        return f'<Route({self.route})>'


    @property
    def has_methods(self) -> bool:
        return len([o.method for o in self.operations]) > 0


class Model:
    def __init__(self, struct):
        self.id: str = struct['id'][: -len('Serializer')]
        self.required: List[str] = struct.get('required', [])
        """
        Contains names of properties. For usual models this field is useless,
        it just contains all properties. For write models it contains properties,
        whose ``required`` field is ``True``.
        """
        self.properties: Dict[str, Property] = \
            {k: Property(k, p) for k, p in struct['properties'].items()}
        check_other_fields(self, struct)


class Schema:
    def __init__(self, schema):
        self.resourcePath: str = schema['resourcePath']
        self.ordering: List[str] = schema.get('ordering', [])

        models: Dict[str, Model] = \
            {m.id: m for m in map(Model, schema['models'].values())}
        self.write_models: Dict[str, Model] = \
            {m.id: m for m in models.values() if m.id.startswith('Write')}
        self.models: Dict[str, Model] = \
            {m.id: m for m in models.values() if not m.id.startswith('Write')}

        self.routes: Dict[str, Route] = \
            {r.url: r for r in map(lambda x: Route(x, self), schema['apis']) if '{pk}/' not in r.url}
        check_other_fields(self, schema, ignore=['apiVersion', 'swaggerVersion', 'basePath', 'apis'])

        self.base_route = self.routes.get(self.resourcePath, None)
        self.pk_route = self.routes.get(self.resourcePath + '/{pk}', None)


    @property
    def resources_name(self) -> str:
        need_cut = self.resourcePath.startswith('/api/')
        start_idx = len('/api/') if need_cut else 0
        return self.resourcePath[start_idx:]


    @property
    def there_is_no_models(self) -> bool:
        return len(self.models) == 0


    @property
    def supports(self) -> Dict[str, bool]:
        return {
            "list": self.base_route and (self.base_route.get is not None),
        }


##############
# Problems TODO:
# 1. To infer types in query params (list method),
# we need to know types of models' primary keys.
# 2. To check whether POST requests (create method)
# is available, we have to brute force it.
# 3. GET / PUT / DELETE are ok (for now)
# 4. To generate get(), get_all(), create(), etc methods
# we need to know, which methods are supported by routes.


def load_schemas() -> List[Schema]:
    from schemas.structure import schemas
    return list(map(Schema, schemas()))


def print_routes():
    global schemas
    for s in schemas:

        # "ok schema", there is base & pk routes with only model
        if s.base_route and s.pk_route and s.base_route.get and s.pk_route.get and s.base_route.get.type == s.pk_route.get.type and s.pk_route.get.type in s.models:
            print('everything')

        # have just pk route with only model
        if not s.base_route and s.pk_route and s.pk_route.get and s.pk_route.get.type in s.models:
            print('get-id / put-post-id')

        # have just base route with only model
        if s.base_route and not s.pk_route and s.base_route.get and s.base_route.get.type in s.models:
            print('get-list / post-list')

        # old routes, we don't know, what to do with them
        if s.base_route and not s.base_route.get and s.there_is_no_models:
            print('nothing')

        # these have only PUT method by {pk}
        if not s.base_route and s.pk_route and not s.pk_route.get and len(s.models) == 1:
            print('put-post-id')

        # these have only POST method by base
        if not s.pk_route and s.base_route and not s.base_route.get and len(s.models) == 1:
            print('post-list')

        # if s.base_route and not s.base_route.get:

        print(s.resourcePath)
        print(f'  Routes: {len(s.routes)}')

        if s.base_route:
            print(f'  base: {s.base_route}')
            if s.base_route.get:
                print(f'    + op: {s.base_route.get.type}')
            else:
                print(f'    - op: NONE')

        if s.pk_route:
            print(f'  pk: {s.pk_route}')
            if s.pk_route.get:
                print(f'    + op: {s.pk_route.get.type}')
            else:
                print(f'    - op: NONE')

        if s.models:
            print(' ', *[m for m in s.models], sep=' ')
        print()


if __name__ == '__main__':
    debug = True
# print_routes()

# from common import to_dash_case
# for s in schemas:
#     print(s.resourcePath)
#
#     resource_route = s.base_route or s.pk_route
#     from_route = to_dash_case(resource_route.get.type) if resource_route and resource_route.get else ''
#     from_model = [to_dash_case(m) for m in s.models]
#     print('-', from_route)
#     print('-', from_model, sep=' ')
#     print()

# for url, r in s.routes.items():
#     print('  ', url, r.route)
# any((r.operations == [] for r in s.routes.values()))
# to_delete = set()
#
# for url, route in schema.routes.items():
#     for test in tests:
#         if test(route):
#             to_delete.add(url)

# print([s for s in s.models])
# for r in s.routes.values():
#     print('  ', r.url)
# for pr in r.get.parameters.values():
#     if pr.python_type == 'Any':
#         print('   ', pr.name)
#         print('   ', [
#             (p.name, p.type) for m in s.models.values()
#             for p in m.properties.values() if pr.name == p.name])


