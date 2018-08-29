# This file is generated
from typing import List

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class Event:
    _resources_name = 'events'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'Event(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model Event are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @property
    def time(self) -> str:
        """
        Default value: ``"2018-08-26T00:35:18.956Z"``

        Type: str
        """
        return self._data.setdefault('time', "2018-08-26T00:35:18.956Z")


    @time.setter
    def time(self, value: str):
        """
        Default value: ``"2018-08-26T00:35:18.956Z"``

        Type: str
        """
        self._data['time'] = value


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
    def html_text(self) -> str:
        return self._data['html_text']


