#!/usr/bin/env python3

# Get username using auth token. Simple version.

from config import id, secret
from stepik import Stepik

stepik = Stepik(client_id=id, client_secret=secret)

user = stepik.stepics().user()

print(user.first_name, user.last_name)
