import pathlib
import json


def schemas():
    for path in pathlib.Path('api').iterdir():
        with open(str(path)) as file:
            yield json.load(file)


def types():
    types = set()

    for schema in schemas():
        for model in schema['models'].values():
            for p in model['properties'].values():
                types.add((p['type'], p.get('format', None)))

    yield from types


