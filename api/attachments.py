# This file is generated
from typing import List

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class Attachment:
    _resources_name = 'attachments'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'Attachment(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model Attachment are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @readonly
    @property
    def name(self) -> str:
        return self._data['name']


    @readonly
    @property
    def size(self) -> str:
        return self._data['size']


    @property
    def course(self) -> str:
        return self._data['course']


    @course.setter
    def course(self, value: str):
        self._data['course'] = value


    @property
    def lesson(self) -> str:
        return self._data['lesson']


    @lesson.setter
    def lesson(self, value: str):
        self._data['lesson'] = value


    @required
    @property
    def file(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('file', "None")


    @file.setter
    def file(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self._data['file'] = value


    @readonly
    @property
    def has_clones(self) -> str:
        return self._data['has_clones']


