# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class CourseList:
    _resources_name = 'course-lists'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'CourseList(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model CourseList are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @property
    def position(self) -> int:
        """
        Default value: ``1``
        """
        return self._data.setdefault('position', 1)


    @position.setter
    def position(self, value: int):
        """
        Default value: ``1``
        """
        self._data['position'] = value


    @required
    @property
    def title(self) -> str:
        return self._data['title']


    @title.setter
    def title(self, value: str):
        self._data['title'] = value


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


    @property
    def courses(self) -> str:
        return self._data['courses']


    @courses.setter
    def courses(self, value: str):
        self._data['courses'] = value


    @property
    def description(self) -> str:
        return self._data['description']


    @description.setter
    def description(self, value: str):
        self._data['description'] = value




class ListOfCourseLists:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> CourseList:
        return CourseList(self._stepik, self._stepik._fetch_object(CourseList, id))


    def get_all(self, ids: List[int], keep_order=False) -> Iterable[CourseList]:
        objects = self._stepik._fetch_objects(CourseList, ids)
        iterable = (CourseList(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)
