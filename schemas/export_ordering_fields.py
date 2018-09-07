#!/bin/env python3
import json
import pathlib
from typing import Dict

import requests
from progress.bar import IncrementalBar

from common import run_once
from config import id, secret
from schemas.schema import Schema, Model

server = 'stepik.org'


@run_once
def auth(id: str, secret: str) -> str:
    # prepare auth token
    resp = requests.post(
        f'https://{server}/oauth2/token/',
        {'grant_type': 'client_credentials'},
        auth=(requests.auth.HTTPBasicAuth(id, secret)))

    token = resp.json().get('access_token', None)
    if not token:
        raise ConnectionRefusedError('Unable to authorize with provided credentials')

    return token


def get(url: str) -> Dict:
    res = requests.get(url, headers={'Authorization': f'Bearer {auth(id, secret)}'})
    return res.json() \
        if res.headers['Content-Type'] == 'application/json' \
        else {'detail': f'{res.status_code} {res.reason}'}


def direct_and_reversed_differs(field: str, model: Model, schema: Schema) -> bool:
    url = f'https://{server}{schema.resourcePath}?order=%s'

    # the first request with usual ordering
    res = get(url % field).get(schema.resources_name, [])
    ids = {r[model.primary_key] for r in res}

    # the second is with reversed ordering
    res = get(url % f'-{field}').get(schema.resources_name, [])
    ids_reversed = {r[model.primary_key] for r in res}

    return ids != ids_reversed


def is_ordering_field(field: str, model: Model, schema: Schema) -> bool:
    attempts = [
        direct_and_reversed_differs(field, model, schema),
        direct_and_reversed_differs(field, model, schema),
        direct_and_reversed_differs(field, model, schema)
    ]

    # true, if 2 of 3 voted so
    return sum(attempts) >= 2


if __name__ == '__main__':
    from schemas.schema import load_schemas
    from schemas.structure import base_methods

    # this file contains a list of fields, that is recommended to check
    with open(f'schemas/api-refined/metadata/ordering_fields.to_check.json', 'r') as f:
        recommended = json.load(f)

    ordering_fields = {}

    for schema in load_schemas():
        # we want to make GET requests
        if not 'GET' in base_methods.get(schema.resourcePath, []):
            continue

        # and filter out parameters of models
        model = schema.models.get(schema.possible_model_name, None)
        if not model:
            continue

        # todo: there might be even more fields
        to_check = {'asc', 'desc'}\
            .union(model.properties.keys())\
            .union(recommended.get(schema.resourcePath, []))

        ordering_fields[schema.resourcePath] = \
            [f for f in IncrementalBar(schema.resources_name).iter(to_check)
             if is_ordering_field(f, model, schema)]

    # mkdir to store result
    metadata = 'schemas/api-refined/metadata'
    pathlib.Path(metadata).mkdir(parents=True, exist_ok=True)

    with open(f'{metadata}/ordering_fields.json', 'w') as f:
        json.dump(ordering_fields, f, indent=2)
