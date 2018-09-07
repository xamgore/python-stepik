#!/bin/env python3
import json
import pathlib

from progress.bar import IncrementalBar
from requests import get

# mkdir to store schemas
pathlib.Path('api').mkdir(parents=True, exist_ok=True)

# grab the main schema, api is flat
url = 'https://stepik.org/api/docs/api-docs/'
resources = [r['path'] for r in get(url).json()['apis']]

# save each schema to a separate file with formatting
for path in IncrementalBar('Downloading', max=20).iter(resources):
    with open(f'/schemas{path}.json', 'w') as f:
        description = get(url + path).json()
        json.dump(description, f, indent=2)
