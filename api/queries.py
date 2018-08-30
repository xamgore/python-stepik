# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class Query:
    _resources_name = 'queries'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'Query(id={self.text!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model Query are missing')


    @required
    @property
    def text(self) -> str:
        return self._data['text']


    @text.setter
    def text(self, value: str):
        self._data['text'] = value




class ListOfQueries:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get_all(self, texts: List[str], keep_order=False) -> Iterable[Query]:
        objects = self._stepik._fetch_objects(Query, texts)
        iterable = (Query(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'text')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)
