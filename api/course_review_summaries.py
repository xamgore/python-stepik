# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class CourseReviewSummary:
    _resources_name = 'course-review-summaries'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'CourseReviewSummary(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model CourseReviewSummary are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @readonly
    @property
    def course(self) -> str:
        return self._data['course']


    @required
    @readonly
    @property
    def average(self) -> str:
        """
        Default value: ``"0"``

        Type: str
        """
        return self._data.setdefault('average', "0")


    @required
    @readonly
    @property
    def count(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['count']


    @readonly
    @property
    def distribution(self) -> str:
        """
        Enter a valid JSON object

        Default value: ``[0, 0, 0, 0, 0]``
        """
        return self._data.setdefault('distribution', [0, 0, 0, 0, 0])




class ListOfCourseReviewSummaries:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> CourseReviewSummary:
        return CourseReviewSummary(self._stepik, self._stepik._fetch_object(CourseReviewSummary, id))


    def get_all(self, ids: List[int], keep_order=False) -> Iterable[CourseReviewSummary]:
        objects = self._stepik._fetch_objects(CourseReviewSummary, ids)
        iterable = (CourseReviewSummary(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)
