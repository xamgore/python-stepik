# This file is generated
from typing import List

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class SocialProfile:
    _resources_name = 'social-profiles'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'SocialProfile(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model SocialProfile are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @readonly
    @property
    def user(self) -> str:
        return self._data['user']


    @required
    @property
    def provider(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('provider', "None")


    @provider.setter
    def provider(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self._data['provider'] = value


    @required
    @property
    def name(self) -> str:
        return self._data['name']


    @name.setter
    def name(self, value: str):
        self._data['name'] = value


    @readonly
    @property
    def url(self) -> str:
        return self._data['url']


