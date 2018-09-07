# Run with Python 3
import requests
from random import randint
from os.path import splitext, dirname

from stepik import Stepik


if __name__ == '__main__':
    from config import id, secret
    stepik = Stepik(id, secret)

    # Get leader user randomly from 100 leaders and download his avatar
    top_leaders = list(stepik.users.iterate(by_knowledge_rank=False, limit=10))
    random_leader = top_leaders[randint(0, len(top_leaders))]

    avatar_url = random_leader.avatar
    response = requests.get(avatar_url, stream=True)
    extension = splitext(avatar_url)[1]

    with open(f'{dirname(__file__)}/out/leader{extension}', 'wb') as out_file:
        out_file.write(response.content)
