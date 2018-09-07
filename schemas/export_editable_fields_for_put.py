import requests
from typing import List

from stepik import Stepik

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


def put(token, url, data=None) -> List[str]:
    api_url = f'https://{server}/api/{url}'
    res = requests.put(api_url, headers={'Authorization': 'Bearer ' + token}, json=data or {})
    return res.json() \
        if res.headers['Content-Type'] == 'application/json' \
        else {'detail': f'{res.status_code} {res.reason}'}


if __name__ == '__main__':
    from schemas.schema import load_schemas
    from config import id, secret

    token = auth(id, secret)
    stepik = Stepik(id, secret)
    schemas = load_schemas()

    # 1. If resource supports POST & PUT method
    # then we can take all parameters from create() method
    # and put them to update() method

    # 2. What if resource doesn't support POST request to base?
    # but has GET, GET by PK
    # ... todo

    pr_schema = [s for s in load_schemas() if s.resourcePath == '/api/profiles'][0]
    # for schema in schemas:
    pr = stepik.profiles.iterate()


    # for p in les_schema.model.properties.values():
    #     if p.readOnly:
    #         continue
    #
    #     print(p.name, p.python_type)
    #     print(put(token, f'{les_schema.resources_name}/{l.id}',
    #               {les_schema.possible_model_name: {'title': 'kek', p.name: '1'}}), end='\n\n')
