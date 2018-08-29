# This file is generated
from typing import List

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class UserCourse:
    _resources_name = 'user-courses'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'UserCourse(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model UserCourse are missing')


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
    @readonly
    @property
    def course(self) -> str:
        return self._data['course']


    @property
    def is_favorite(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['is_favorite']


    @is_favorite.setter
    def is_favorite(self, value: bool):
        """
        Default value: ``False``
        """
        self._data['is_favorite'] = value


    @required
    @readonly
    @property
    def last_viewed(self) -> str:
        """
        Default value: ``"2018-08-26T00:35:53.561Z"``

        Type: str
        """
        return self._data.setdefault('last_viewed', "2018-08-26T00:35:53.561Z")


