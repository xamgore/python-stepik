# This file is generated
from typing import List

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class SocialAccount:
    _resources_name = 'social-accounts'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'SocialAccount(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model SocialAccount are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @property
    def user(self) -> str:
        return self._data['user']


    @user.setter
    def user(self, value: str):
        self._data['user'] = value


    @required
    @property
    def provider(self) -> str:
        return self._data['provider']


    @provider.setter
    def provider(self, value: str):
        self._data['provider'] = value


    @required
    @property
    def uid(self) -> str:
        return self._data['uid']


    @uid.setter
    def uid(self, value: str):
        self._data['uid'] = value


