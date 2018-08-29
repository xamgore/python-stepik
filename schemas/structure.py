import json
import pathlib
from typing import Dict, List

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




base_methods: Dict[str, List[str]] = {}
with open('api-refined/metadata/methods.base.json') as f:
    base_methods = json.load(f)

pk_methods: Dict[str, List[str]] = {}
with open('api-refined/metadata/methods.pk.json') as f:
    pk_methods = json.load(f)

if __name__ == '__main__':
    print(*types())
