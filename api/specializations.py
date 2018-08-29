# This file is generated
from typing import List

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class Specialization:
    _resources_name = 'specializations'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'Specialization(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model Specialization are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @property
    def title(self) -> str:
        return self._data['title']


    @title.setter
    def title(self, value: str):
        self._data['title'] = value


    @required
    @property
    def details_url(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('details_url', "None")


    @details_url.setter
    def details_url(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self._data['details_url'] = value


    @property
    def courses(self) -> str:
        return self._data['courses']


    @courses.setter
    def courses(self, value: str):
        self._data['courses'] = value


