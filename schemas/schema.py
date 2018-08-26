from typing import Dict, List, Callable, Any


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
        self.method: str = data['method']
        """Always GET"""
        self.nickname: str = data['nickname']
        """Resource name + action (retrieve, list, etc)"""
        self.notes: str = data['notes']
        """Short description about the resource"""
        # TODO: use notes when generating list resources
        self.summary: str = data['summary']
        """Short description about the resource. Use ``notes`` instead, it has more text."""
        self.type: str = data['type']
        """Model that is used in the route"""
        self.parameters: Dict[str, Parameter] = \
            {p.name: p for p in map(Parameter, data.get('parameters', []))}
        check_other_fields(self, data)

        self.type = self.type[:-len('Serializer')] \
            if self.type.endswith('Serializer') else self.type


class Route:
    def __init__(self, route):
        self.url: str = route['path']
        self.description: str = route['description']
        check_other_fields(self, route, ignore=['operations', 'path'])

        self.operations = list(map(Operation, route['operations']))
        self.get = self.operations[0] if self.operations else None

        if self.get and self.get.method != 'GET':
            raise AttributeError('Swagger generates only GET methods, need intervention')


    @property
    def route(self):
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
        self.properties: Dict[str, Property] = \
            {k: Property(k, p) for k, p in struct['properties'].items()}
        check_other_fields(self, struct)


class Schema:
    def __init__(self, schema):
        self.resourcePath = schema['resourcePath']
        self.ordering: List[str] = schema.get('ordering', [])

        models: Dict[str, Model] = {m.id: m for m in map(Model, schema['models'].values())}
        self.write_models: Dict[str, Model] = \
            {m.id: m for m in models.values() if m.id.startswith('Write')}
        self.models: Dict[str, Model] = \
            {m.id: m for m in models.values() if not m.id.startswith('Write')}

        self.routes: Dict[str, Route] = {r.url: r for r in map(Route, schema['apis'])}
        check_other_fields(self, schema, ignore=['apiVersion', 'swaggerVersion', 'basePath', 'apis'])


##############

def remove_routes_by_predicates(schema: Schema, *tests: Callable[[Route], bool]) -> Schema:
    to_delete = set()

    for url, route in schema.routes.items():
        for test in tests:
            if test(route):
                to_delete.add(url)

    for url in to_delete:
        del schema.routes[url]

    if not len(schema.routes):
        print(f'Resource {schema.resourcePath} has no routes!')

    return schema


from schemas.structure import schemas

schemas = [remove_routes_by_predicates(
    Schema(s),
    lambda r: '{pk}/' in r.url
    # lambda r: not r.has_methods
) for s in schemas()]

for s in schemas:
    print(s.resourcePath)
    for url, r in s.routes.items():
        print('  ', url, r.route)
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
