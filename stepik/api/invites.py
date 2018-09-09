# This file is generated
from typing import List, Iterable, Any, Optional

from stepik.errors import StepikError
from stepik.common import required, readonly
from stepik.resources_list import ResourcesList


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


    def create(self,
               invite_key: str,
               **kwargs) -> Invite:
        vars = locals().copy()
        data = {'invite':
                    {k: v for k, v in {**vars, **kwargs}.items()
                     if k != 'self' and v is not None}}

        response = self._stepik._post('invites', data)
        if 'invites' not in response:
            raise StepikError(response)

        return Invite(self._stepik, response['invites'][0])

