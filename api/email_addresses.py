# This file is generated
from typing import List

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class EmailAddress:
    _resources_name = 'email-addresses'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'EmailAddress(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model EmailAddress are missing')


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
    def email(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('email', "None")


    @email.setter
    def email(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self._data['email'] = value


    @readonly
    @property
    def is_verified(self) -> bool:
        return self._data['is_verified']


    @readonly
    @property
    def is_primary(self) -> bool:
        return self._data['is_primary']


