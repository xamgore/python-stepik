import json
import pathlib
from json import JSONDecodeError
from typing import List

import requests

server = 'stepik.org'


def get(url) -> List[str]:
    api_url = f'https://{server}/api/{url}'
    res = requests.options(api_url)
    return res.headers['Allow'].split(', ') \
        if res.headers['Content-Type'] == 'application/json' else []


if __name__ == '__main__':
    from schemas.schema import load_schemas
    schemas = load_schemas()

    routes = {schema.resourcePath: get(schema.resources_name) for schema in schemas}
    routes_pk = {schema.resourcePath: get(f'{schema.resources_name}/0') for schema in schemas}

    dir = 'api-refined/metadata'
    pathlib.Path(dir).mkdir(parents=True, exist_ok=True)

    with open(f'{dir}/methods.base.json', 'w') as f:
        json.dump(routes, f, indent=2)

    with open(f'{dir}/methods.pk.json', 'w') as f:
        json.dump(routes_pk, f, indent=2)
