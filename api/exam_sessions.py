# This file is generated
from typing import List

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class ExamSession:
    _resources_name = 'exam-sessions'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'ExamSession(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model ExamSession are missing')


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
    def begin_date(self) -> str:
        """
        Default value: ``"2018-08-26T00:35:19.469Z"``

        Type: str
        """
        return self._data.setdefault('begin_date', "2018-08-26T00:35:19.469Z")


