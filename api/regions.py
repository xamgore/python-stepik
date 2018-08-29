# This file is generated
from typing import List

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class AlternativeName:
    _resources_name = 'regions'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'AlternativeName(id={self.name!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model AlternativeName are missing')


    @required
    @property
    def name(self) -> str:
        return self._data['name']


    @name.setter
    def name(self, value: str):
        self._data['name'] = value


    @required
    @property
    def language(self) -> str:
        return self._data['language']


    @language.setter
    def language(self, value: str):
        self._data['language'] = value


    @property
    def is_preferred(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['is_preferred']


    @is_preferred.setter
    def is_preferred(self, value: bool):
        """
        Default value: ``False``
        """
        self._data['is_preferred'] = value




class Region:
    _resources_name = 'regions'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'Region(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model Region are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @property
    def name_std(self) -> str:
        return self._data['name_std']


    @name_std.setter
    def name_std(self, value: str):
        self._data['name_std'] = value


    @required
    @property
    def alt_names(self) -> str:
        """
        Type: str
        """
        return self._data['alt_names']


    @alt_names.setter
    def alt_names(self, value: str):
        """
        Type: str
        """
        self._data['alt_names'] = value


