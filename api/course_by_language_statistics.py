# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class CourseByLanguageStatistics:
    _resources_name = 'course-by-language-statistics'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'CourseByLanguageStatistics(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model CourseByLanguageStatistics are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @property
    def course(self) -> str:
        return self._data['course']


    @course.setter
    def course(self, value: str):
        self._data['course'] = value


    @required
    @property
    def language(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('language', "None")


    @language.setter
    def language(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self._data['language'] = value


    @required
    @property
    def learners_count(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['learners_count']


    @learners_count.setter
    def learners_count(self, value: int):
        """
        Default value: ``0``
        """
        self._data['learners_count'] = value




class ListOfCourseByLanguageStatistics:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> CourseByLanguageStatistics:
        return CourseByLanguageStatistics(self._stepik, self._stepik._fetch_object(CourseByLanguageStatistics, id))


    def get_all(self, ids: List[int], keep_order=False) -> Iterable[CourseByLanguageStatistics]:
        objects = self._stepik._fetch_objects(CourseByLanguageStatistics, ids)
        iterable = (CourseByLanguageStatistics(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)
