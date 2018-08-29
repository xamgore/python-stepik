# This file is generated
from typing import List

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class ScoreFile:
    _resources_name = 'score-files'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'ScoreFile(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model ScoreFile are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @property
    def session(self) -> str:
        return self._data['session']


    @session.setter
    def session(self, value: str):
        self._data['session'] = value


    @required
    @property
    def file(self) -> str:
        return self._data['file']


    @file.setter
    def file(self, value: str):
        self._data['file'] = value


    @readonly
    @property
    def error(self) -> str:
        return self._data['error']


    @readonly
    @property
    def create_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('create_date', "None")


    @readonly
    @property
    def process_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('process_date', "None")


