# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class Achievement:
    _resources_name = 'achievements'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'Achievement(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model Achievement are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @property
    def kind(self) -> str:
        return self._data['kind']


    @kind.setter
    def kind(self, value: str):
        self._data['kind'] = value


    @required
    @property
    def target_score(self) -> int:
        return self._data['target_score']


    @target_score.setter
    def target_score(self, value: int):
        self._data['target_score'] = value


    @required
    @property
    def icon_uploadcare_uuid(self) -> str:
        return self._data['icon_uploadcare_uuid']


    @icon_uploadcare_uuid.setter
    def icon_uploadcare_uuid(self, value: str):
        self._data['icon_uploadcare_uuid'] = value


    @readonly
    @property
    def icon_urls(self) -> str:
        return self._data['icon_urls']




class ListOfAchievements:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> Achievement:
        return Achievement(self._stepik, self._stepik._fetch_object(Achievement, id))


    def get_all(self, ids: List[int], keep_order=False) -> Iterable[Achievement]:
        objects = self._stepik._fetch_objects(Achievement, ids)
        iterable = (Achievement(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)
