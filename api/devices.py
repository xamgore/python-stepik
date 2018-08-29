# This file is generated
from typing import List

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class Device:
    _resources_name = 'devices'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'Device(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model Device are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @property
    def registration_id(self) -> str:
        return self._data['registration_id']


    @registration_id.setter
    def registration_id(self, value: str):
        self._data['registration_id'] = value


    @required
    @readonly
    @property
    def user(self) -> str:
        return self._data['user']


    @required
    @property
    def description(self) -> str:
        return self._data['description']


    @description.setter
    def description(self, value: str):
        self._data['description'] = value


    @required
    @property
    def client_type(self) -> str:
        """
        Default value: ``"ios"``

        Type: str
        """
        return self._data.setdefault('client_type', "ios")


    @client_type.setter
    def client_type(self, value: str):
        """
        Default value: ``"ios"``

        Type: str
        """
        self._data['client_type'] = value


    @property
    def is_badges_enabled(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['is_badges_enabled']


    @is_badges_enabled.setter
    def is_badges_enabled(self, value: bool):
        """
        Default value: ``False``
        """
        self._data['is_badges_enabled'] = value


