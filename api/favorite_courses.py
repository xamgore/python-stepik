# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class FavoriteCourse:
    _resources_name = 'favorite-courses'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'FavoriteCourse(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model FavoriteCourse are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @readonly
    @property
    def user(self) -> str:
        return self._data['user']


    @required
    @property
    def course(self) -> str:
        return self._data['course']


    @course.setter
    def course(self, value: str):
        self._data['course'] = value




class ListOfFavoriteCourses:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> FavoriteCourse:
        return FavoriteCourse(self._stepik, self._stepik._fetch_object(FavoriteCourse, id))


    def get_all(self, ids: List[int], keep_order=False) -> Iterable[FavoriteCourse]:
        objects = self._stepik._fetch_objects(FavoriteCourse, ids)
        iterable = (FavoriteCourse(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)


    def create(self, course: str) -> FavoriteCourse:
        vars = locals().copy()
        data = {'favorite-course': {k: v for k, v in vars.items() if k != 'self' and v is not None}}

        resources_name = 'favorite-courses'
        response = self._stepik._post(resources_name, data)

        if resources_name not in response:
            raise StepikError(response)

        return FavoriteCourse(self._stepik, response[resources_name][0])


    def delete(self, id: int) -> dict:
        return self._stepik._delete('favorite-courses', id)
