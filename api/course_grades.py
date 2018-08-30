# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class CourseGrade:
    _resources_name = 'course-grades'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'CourseGrade(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model CourseGrade are missing')


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
    def user(self) -> str:
        return self._data['user']


    @readonly
    @property
    def results(self) -> str:
        return self._data['results']


    @required
    @readonly
    @property
    def score(self) -> str:
        """
        Default value: ``"0"``

        Type: str
        """
        return self._data.setdefault('score', "0")


    @readonly
    @property
    def rank(self) -> int:
        return self._data['rank']


    @readonly
    @property
    def rank_max(self) -> int:
        return self._data['rank_max']


    @readonly
    @property
    def rank_position(self) -> int:
        return self._data['rank_position']


    @readonly
    @property
    def users_count(self) -> int:
        return self._data['users_count']


    @readonly
    @property
    def is_teacher(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['is_teacher']


    @readonly
    @property
    def date_joined(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('date_joined', "None")


    @readonly
    @property
    def last_viewed(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('last_viewed', "None")


    @readonly
    @property
    def certificate_issue_date(self) -> str:
        return self._data['certificate_issue_date']


    @readonly
    @property
    def certificate_issue_regular_date(self) -> str:
        return self._data['certificate_issue_regular_date']


    @readonly
    @property
    def certificate_issue_distinction_date(self) -> str:
        return self._data['certificate_issue_distinction_date']


    @readonly
    @property
    def certificate_update_date(self) -> str:
        return self._data['certificate_update_date']


    @readonly
    @property
    def certificate_url(self) -> str:
        return self._data['certificate_url']




class ListOfCourseGrades:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> CourseGrade:
        return CourseGrade(self._stepik, self._stepik._fetch_object(CourseGrade, id))


    def get_all(self, ids: List[int], keep_order=False) -> Iterable[CourseGrade]:
        objects = self._stepik._fetch_objects(CourseGrade, ids)
        iterable = (CourseGrade(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)
