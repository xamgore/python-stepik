# This file is generated
from typing import List

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class StorageRecord:
    _resources_name = 'storage-records'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'StorageRecord(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model StorageRecord are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @readonly
    @property
    def user(self) -> str:
        return self._data['user']


    @property
    def kind(self) -> str:
        """
        Default value: ````
        """
        return self._data['kind']


    @kind.setter
    def kind(self, value: str):
        """
        Default value: ````
        """
        self._data['kind'] = value


    @property
    def data(self) -> str:
        """
        Enter a valid JSON object

        Default value: ``{}``
        """
        return self._data['data']


    @data.setter
    def data(self, value: str):
        """
        Enter a valid JSON object

        Default value: ``{}``
        """
        self._data['data'] = value


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
    def update_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('update_date', "None")


