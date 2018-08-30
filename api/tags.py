# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class Tag:
    _resources_name = 'tags'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'Tag(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model Tag are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @property
    def title(self) -> str:
        return self._data['title']


    @title.setter
    def title(self, value: str):
        self._data['title'] = value




class ListOfTags:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> Tag:
        return Tag(self._stepik, self._stepik._fetch_object(Tag, id))


    def get_all(self, ids: List[int], keep_order=False) -> Iterable[Tag]:
        objects = self._stepik._fetch_objects(Tag, ids)
        iterable = (Tag(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)
