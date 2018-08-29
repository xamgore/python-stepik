import json
import pathlib
from typing import List, Dict, Any

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


def post(token, url, data=None) -> List[str]:
    api_url = f'https://{server}/api/{url}'
    res = requests.post(api_url, headers={'Authorization': 'Bearer ' + token}, json=data or {})
    return res.json() \
        if res.headers['Content-Type'] == 'application/json' \
        else {'detail': f'{res.status_code} {res.reason}'}


def contains_required(value):
    # checks that data is like this:
    # {'target': ['This field is required.']}
    # but not these:
    # {'non_field_errors': ['Submission or instruction are required']}
    # {'url': 'https://stepik.org/ws', 'token': 'Mjk2MjA4Nw:1fuRmu:p8NxPfuvgAZzHlUIelh2LV5gUP4'}
    return isinstance(value, List) and \
           isinstance(value[0], str) and \
           value[0] == 'This field is required.'


if __name__ == '__main__':
    from schemas.schema import load_schemas
    from schemas.structure import base_methods
    from config import id, secret

    token = auth(id, secret)
    schemas = load_schemas()

    required_fields = {
        '/api/submissions':     ['attempt'],
        '/api/storage-records': [],    # can put anything we want
        '/api/review-sessions': None,  # todo
        '/api/videos':          None,  # there is Stepik.upload_video method
        '/api/ws':              []     # todo, ignores input
    }

    for schema in schemas:
        if schema.resourcePath == '/api/submissions':
            continue  # doesn't return meta information

        path = schema.resourcePath
        if path in base_methods and 'POST' in base_methods[path]:
            fields: Dict[str, Any] = post(token, schema.resources_name, {'object': {}})
            is_description = all(map(contains_required, fields.values()))

            if is_description:
                required_fields[schema.resourcePath] = list(fields.keys())
            else:
                print('Error: ', schema.resourcePath, fields, end='\n\n')

    dir = 'api-refined/metadata'
    pathlib.Path(dir).mkdir(parents=True, exist_ok=True)

    with open(f'{dir}/required_fields.post.base.json', 'w') as f:
        json.dump(required_fields, f, indent=2)

    # TODO save results, and raise error on any changes
