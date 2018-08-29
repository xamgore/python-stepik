# This file is generated
from typing import List

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class ShortUrl:
    _resources_name = 'short-urls'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'ShortUrl(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model ShortUrl are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @readonly
    @property
    def key(self) -> str:
        return self._data['key']


    @required
    @property
    def url(self) -> str:
        return self._data['url']


    @url.setter
    def url(self, value: str):
        self._data['url'] = value


    @readonly
    @property
    def short_url(self) -> str:
        return self._data['short_url']


