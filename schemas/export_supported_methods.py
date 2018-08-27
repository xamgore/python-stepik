import json
import pathlib
from json import JSONDecodeError
from typing import List

import requests

server = 'stepik.org'


def auth(id, secret) -> str:
    # prepare auth token
    resp = requests.post(
        f'https://{server}/oauth2/token/',
        {'grant_type': 'client_credentials'},
        auth=(requests.auth.HTTPBasicAuth(id, secret)))

    token = resp.json().get('access_token', None)
    if not token:
        raise ConnectionRefusedError('Unable to authorize with provided credentials')

    return token


def get(token, url) -> List[str]:
    api_url = f'https://{server}/api/{url}'
    res = requests.options(api_url, headers={'Authorization': 'Bearer ' + token})
    return res.headers['Allow'].split(', ') \
        if res.headers['Content-Type'] == 'application/json' else []


if __name__ == '__main__':
    from schemas.schema import load_schemas
    from config import id, secret

    token = auth(id, secret)
    schemas = load_schemas()

    routes = {schema.resourcePath: get(token, schema.resources_name) for schema in schemas}
    routes_pk = {schema.resourcePath: get(token, f'{schema.resources_name}/0') for schema in schemas}

    dir = 'api-refined/metadata'
    pathlib.Path(dir).mkdir(parents=True, exist_ok=True)

    with open(f'{dir}/base.methods.json', 'w') as f:
        json.dump(routes, f, indent=2)

    with open(f'{dir}/pk.methods.json', 'w') as f:
        json.dump(routes_pk, f, indent=2)
