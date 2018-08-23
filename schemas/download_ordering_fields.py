#!/bin/env python3
import json
import os
import pathlib
from time import sleep

from progress.bar import IncrementalBar
from requests import get
from structure import schemas


def get_props_names(schema):
    props = set()

    for model, struct in schema['models'].items():
        if not model.startswith('Write'):
            props.update(struct['properties'].keys())

    return props


def direct_and_reversed_order_differs(resource, prop):
    # make first request with normal ordering
    url = f'https://stepik.org:443/api/{resource}?order=%s'
    resources = get(url % prop).json().get(resource, [])
    ids = {r['id'] for r in resources}

    # second with reversed one
    resources = get(url % f'-{prop}').json().get(resource, [])
    ids_reversed = {r['id'] for r in resources}

    return ids != ids_reversed


# mkdir to store result
pathlib.Path('ordering_fields').mkdir(parents=True, exist_ok=True)

for schema in IncrementalBar('Downloading').iter(schemas()):
    path = schema['resourcePath']
    resource = path.split('/')[-1]
    ordering_fields = set()

    for name in get_props_names(schema):
        try:
            if direct_and_reversed_order_differs(resource, name):
                ordering_fields.add(name)
        except BaseException as e:
            print(f'failed {path} order by {name}: {e}')
            pass

    if not ordering_fields:
        continue

    path_to_refined = f'api-refined/{resource}.json'
    refinedSchema = {}

    if os.path.exists(path_to_refined):
        with open(path_to_refined, 'r') as f:
            refinedSchema = json.load(f)

    with open(f'api-refined/{resource}.json', 'w') as f:
        refinedSchema['ordering'] = list(sorted(ordering_fields))
        json.dump(refinedSchema, f, indent=2, ensure_ascii=False)

    print(f'{path}: {", ".join(ordering_fields)}')
