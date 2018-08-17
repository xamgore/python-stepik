import json
import pathlib

from jsonmerge import merge
from common import run_once


def schemas():
    for path in pathlib.Path('api').iterdir():
        with open(str(path)) as source:
            schema = json.load(source)

            refined_path = f'api-refined/{path.name}'
            if pathlib.Path(refined_path).exists():
                with open(refined_path) as refined:
                    yield merge(schema, json.load(refined))
            else:
                yield schema


def types():
    types = set()

    for schema in schemas():
        for model in schema['models'].values():
            for p in model['properties'].values():
                types.add(p['type'])

    yield from types


def get_types(model):
    return {p['type'] for p in model['properties'].values()}


@run_once
def imports():
    """Return dict of (model -> resource path)"""
    book = {}

    for schema in schemas():
        for model in schema['models'].keys():
            book[model.replace('Serializer', '')] = schema['resourcePath'].lstrip('/').replace('/', '.')

    return book


if __name__ == '__main__':
    print(*types())
