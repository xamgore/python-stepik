# This file is generated
from typing import List

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class SearchReaction:
    _resources_name = 'search-reactions'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'SearchReaction(id={self.result!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model SearchReaction are missing')


    @required
    @property
    def result(self) -> str:
        return self._data['result']


    @result.setter
    def result(self, value: str):
        self._data['result'] = value


