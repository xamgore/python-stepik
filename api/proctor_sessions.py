# This file is generated
from typing import List

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class ProctorSession:
    _resources_name = 'proctor-sessions'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'ProctorSession(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model ProctorSession are missing')


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
    def section(self) -> str:
        return self._data['section']


    @section.setter
    def section(self, value: str):
        self._data['section'] = value


    @required
    @readonly
    @property
    def create_date(self) -> str:
        """
        Default value: ``"2018-08-26T00:35:29.583Z"``

        Type: str
        """
        return self._data.setdefault('create_date', "2018-08-26T00:35:29.583Z")


    @readonly
    @property
    def start_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('start_date', "None")


    @readonly
    @property
    def stop_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('stop_date', "None")


    @readonly
    @property
    def submit_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('submit_date', "None")


    @readonly
    @property
    def comment(self) -> str:
        return self._data['comment']


    @required
    @readonly
    @property
    def score(self) -> str:
        """
        Default value: ``"0"``

        Type: str
        """
        return self._data.setdefault('score', "0")


