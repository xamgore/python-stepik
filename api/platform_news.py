# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class PlatformNews:
    _resources_name = 'platform-news'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'PlatformNews(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model PlatformNews are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @property
    def language(self) -> str:
        """
        Default value: ``"en"``

        Type: str
        """
        return self._data.setdefault('language', "en")


    @language.setter
    def language(self, value: str):
        """
        Default value: ``"en"``

        Type: str
        """
        self._data['language'] = value


    @readonly
    @property
    def create_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('create_date', "None")


    @required
    @property
    def text(self) -> str:
        return self._data['text']


    @text.setter
    def text(self, value: str):
        self._data['text'] = value




class ListOfPlatformNews:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> PlatformNews:
        return PlatformNews(self._stepik, self._stepik._fetch_object(PlatformNews, id))


    def get_all(self, ids: List[int], keep_order=False) -> Iterable[PlatformNews]:
        objects = self._stepik._fetch_objects(PlatformNews, ids)
        iterable = (PlatformNews(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)
