# This file is generated
from typing import List, Iterable, Any, Optional

from stepik.errors import StepikError
from stepik.common import required, readonly
from stepik.resources_list import ResourcesList


class ProfileImage:
    _resources_name = 'profile-images'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'ProfileImage(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model ProfileImage are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @property
    def avatar(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('avatar', "None")


    @avatar.setter
    def avatar(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self._data['avatar'] = value




class ListOfProfileImages:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik

