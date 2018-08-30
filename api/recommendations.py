# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class Recommendation:
    _resources_name = 'recommendations'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'Recommendation(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model Recommendation are missing')


    @readonly
    @property
    def id(self) -> str:
        return self._data['id']


    @readonly
    @property
    def lesson(self) -> str:
        return self._data['lesson']


    @readonly
    @property
    def reasons(self) -> str:
        return self._data['reasons']




class ListOfRecommendations:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get_all(self, ids: List[str], keep_order=False) -> Iterable[Recommendation]:
        objects = self._stepik._fetch_objects(Recommendation, ids)
        iterable = (Recommendation(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)
