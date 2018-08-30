# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class Specialization:
    _resources_name = 'specializations'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'Specialization(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model Specialization are missing')


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


    @required
    @property
    def details_url(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('details_url', "None")


    @details_url.setter
    def details_url(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self._data['details_url'] = value


    @property
    def courses(self) -> str:
        return self._data['courses']


    @courses.setter
    def courses(self, value: str):
        self._data['courses'] = value




class ListOfSpecializations:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> Specialization:
        return Specialization(self._stepik, self._stepik._fetch_object(Specialization, id))


    def get_all(self, ids: List[int], keep_order=False) -> Iterable[Specialization]:
        objects = self._stepik._fetch_objects(Specialization, ids)
        iterable = (Specialization(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)
