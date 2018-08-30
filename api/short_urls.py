# This file is generated
from typing import List, Iterable, Any

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




class ListOfShortUrls:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get_all(self, ids: List[int], keep_order=False) -> Iterable[ShortUrl]:
        objects = self._stepik._fetch_objects(ShortUrl, ids)
        iterable = (ShortUrl(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)


    def create(self, url: str) -> ShortUrl:
        vars = locals().copy()
        data = {'short-url': {k: v for k, v in vars.items() if k != 'self' and v is not None}}

        resources_name = 'short-urls'
        response = self._stepik._post(resources_name, data)

        if resources_name not in response:
            raise StepikError(response)

        return ShortUrl(self._stepik, response[resources_name][0])
