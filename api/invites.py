# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class Invite:
    _resources_name = 'invites'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'Invite(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model Invite are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @property
    def invite_key(self) -> str:
        return self._data['invite_key']


    @invite_key.setter
    def invite_key(self, value: str):
        self._data['invite_key'] = value




class ListOfInvites:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def create(self, invite_key: str) -> Invite:
        vars = locals().copy()
        data = {'invite': {k: v for k, v in vars.items() if k != 'self' and v is not None}}

        resources_name = 'invites'
        response = self._stepik._post(resources_name, data)

        if resources_name not in response:
            raise StepikError(response)

        return Invite(self._stepik, response[resources_name][0])
