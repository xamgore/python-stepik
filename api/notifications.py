# This file is generated
from typing import List

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class Notification:
    _resources_name = 'notifications'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'Notification(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model Notification are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @property
    def is_unread(self) -> bool:
        """
        Default value: ``True``
        """
        return self._data.setdefault('is_unread', True)


    @is_unread.setter
    def is_unread(self, value: bool):
        """
        Default value: ``True``
        """
        self._data['is_unread'] = value


    @property
    def is_muted(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['is_muted']


    @is_muted.setter
    def is_muted(self, value: bool):
        """
        Default value: ``False``
        """
        self._data['is_muted'] = value


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


    @readonly
    @property
    def time(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('time', "None")


    @readonly
    @property
    def type(self) -> str:
        return self._data['type']


    @readonly
    @property
    def action(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('action', "None")


    @readonly
    @property
    def level(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('level', "None")


    @readonly
    @property
    def priority(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('priority', "None")


    @readonly
    @property
    def html_text(self) -> str:
        return self._data['html_text']


