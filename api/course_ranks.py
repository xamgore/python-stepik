# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class CourseRank:
    _resources_name = 'course-ranks'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'CourseRank(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model CourseRank are missing')


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
    def user(self) -> str:
        return self._data['user']


    @user.setter
    def user(self, value: str):
        self._data['user'] = value


    @required
    @property
    def score(self) -> str:
        """
        Default value: ``"0"``

        Type: str
        """
        return self._data.setdefault('score', "0")


    @score.setter
    def score(self, value: str):
        """
        Default value: ``"0"``

        Type: str
        """
        self._data['score'] = value


    @property
    def rank(self) -> int:
        return self._data['rank']


    @rank.setter
    def rank(self, value: int):
        self._data['rank'] = value


    @property
    def rank_max(self) -> int:
        return self._data['rank_max']


    @rank_max.setter
    def rank_max(self, value: int):
        self._data['rank_max'] = value


    @readonly
    @property
    def position(self) -> str:
        return self._data['position']


    @property
    def users_count(self) -> int:
        return self._data['users_count']


    @users_count.setter
    def users_count(self, value: int):
        self._data['users_count'] = value




class ListOfCourseRanks:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> CourseRank:
        return CourseRank(self._stepik, self._stepik._fetch_object(CourseRank, id))


    def get_all(self, ids: List[int], keep_order=False) -> Iterable[CourseRank]:
        objects = self._stepik._fetch_objects(CourseRank, ids)
        iterable = (CourseRank(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)
