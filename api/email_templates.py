# This file is generated
from typing import List

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class EmailTemplate:
    _resources_name = 'email-templates'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'EmailTemplate(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model EmailTemplate are missing')


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
    def mail_type(self) -> str:
        """
        Default value: ``"announcement"``

        Type: str
        """
        return self._data.setdefault('mail_type', "announcement")


    @mail_type.setter
    def mail_type(self, value: str):
        """
        Default value: ``"announcement"``

        Type: str
        """
        self._data['mail_type'] = value


    @required
    @property
    def name(self) -> str:
        return self._data['name']


    @name.setter
    def name(self, value: str):
        self._data['name'] = value


