# This file is generated
from typing import List

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class Invitation:
    _resources_name = 'invitations'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'Invitation(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model Invitation are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @property
    def group(self) -> str:
        return self._data['group']


    @group.setter
    def group(self, value: str):
        self._data['group'] = value


    @readonly
    @property
    def name(self) -> str:
        return self._data['name']


    @readonly
    @property
    def url(self) -> str:
        return self._data['url']


    @property
    def description(self) -> str:
        return self._data['description']


    @description.setter
    def description(self, value: str):
        self._data['description'] = value


    @property
    def limit(self) -> int:
        return self._data['limit']


    @limit.setter
    def limit(self, value: int):
        self._data['limit'] = value


