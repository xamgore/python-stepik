# This file is generated
from typing import List, Iterable, Any, Optional

from stepik.errors import StepikError
from stepik.common import required, readonly
from stepik.resources_list import ResourcesList


class CourseProgressChange:
    _resources_name = 'course-progress-changes'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'CourseProgressChange(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model CourseProgressChange are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @property
    def user(self) -> str:
        return self._data['user']


    @user.setter
    def user(self, value: str):
        self._data['user'] = value


    @required
    @property
    def course(self) -> str:
        return self._data['course']


    @course.setter
    def course(self, value: str):
        self._data['course'] = value


    @required
    @property
    def time(self) -> str:
        """
        Default value: ``"2018-08-26T00:35:10.871Z"``

        Type: str
        """
        return self._data.setdefault('time', "2018-08-26T00:35:10.871Z")


    @time.setter
    def time(self, value: str):
        """
        Default value: ``"2018-08-26T00:35:10.871Z"``

        Type: str
        """
        self._data['time'] = value


    @required
    @property
    def score(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('score', "None")


    @score.setter
    def score(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self._data['score'] = value


    @required
    @property
    def cost(self) -> int:
        return self._data['cost']


    @cost.setter
    def cost(self, value: int):
        self._data['cost'] = value


    @required
    @property
    def n_steps(self) -> int:
        return self._data['n_steps']


    @n_steps.setter
    def n_steps(self, value: int):
        self._data['n_steps'] = value


    @required
    @property
    def n_steps_passed(self) -> int:
        return self._data['n_steps_passed']


    @n_steps_passed.setter
    def n_steps_passed(self, value: int):
        self._data['n_steps_passed'] = value


    @required
    @property
    def best_score(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('best_score', "None")


    @best_score.setter
    def best_score(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self._data['best_score'] = value


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


    @property
    def rank_position(self) -> int:
        return self._data['rank_position']


    @rank_position.setter
    def rank_position(self, value: int):
        self._data['rank_position'] = value


    @property
    def users_count(self) -> int:
        return self._data['users_count']


    @users_count.setter
    def users_count(self, value: int):
        self._data['users_count'] = value


    @property
    def is_teacher(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['is_teacher']


    @is_teacher.setter
    def is_teacher(self, value: bool):
        """
        Default value: ``False``
        """
        self._data['is_teacher'] = value


    @property
    def date_joined(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('date_joined', "None")


    @date_joined.setter
    def date_joined(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self._data['date_joined'] = value


    @property
    def last_viewed(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('last_viewed', "None")


    @last_viewed.setter
    def last_viewed(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self._data['last_viewed'] = value




class ListOfCourseProgressChanges:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> CourseProgressChange:
        obj = self._stepik._fetch_object(CourseProgressChange, id)
        return CourseProgressChange(self._stepik, obj)


    def get_all(self, ids: Iterable[int], keep_order=False) -> Iterable[CourseProgressChange]:
        """
        Grab a bunch of ids, usually 20 objects per request.
        """
        if keep_order:
            ids = list(ids)

        objects = self._stepik._fetch_objects(CourseProgressChange, ids)
        iterable = (CourseProgressChange(self._stepik, o) for o in objects)

        return iterable if not keep_order \
            else sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))


    def iterate(self,
                skip: int = 0, limit: Optional[int] = 20) -> Iterable[CourseProgressChange]:
        """
        There are base fields, like ``language``, that can be used to filter out
        objects. Also there are ordering fields, that starts with ``by_`` prefix.
        They are not used in queries if their value is ``None``. If ``True``
        objects are sorted in straight order, if ``False`` in reversed.
        The sorting is done on the server side, there is no guarantees will it be
        in ascending or descending order.

        ``skip`` parameter means how much objects to skip from the beginning.

        ``limit`` means how much objects to take. It can be set to ``None``,
        all objects will be fetched (not recommended, actually).
        """

        assert skip >= 0, 'skip must be positive'
        assert limit is None or limit >= 0, 'limit must be positive'

        vars = locals().copy()
        args, order = [], []

        for k, v in vars.items():
            is_ordering = k.startswith('by_')
            is_special = k in ['self', 'skip']

            if not v is None and not is_ordering and not is_special:
                args.append((k, v))

            if not v is None and is_ordering:
                sign = '-' if v else ''
                order.append(sign + k[3:])

        from urllib.parse import urlencode
        params = urlencode(args, doseq=True)
        ordering = ','.join(order)

        skip = 0 if skip is None else skip
        page_idx, count = divmod(skip, 20)
        page_idx += 1  # stepik counts from 1

        while True:
            page = self._stepik._get(f'course-progress-changes?{params}&page={page_idx}&order={ordering}')

            for obj in page['course-progress-changes']:
                if limit and count >= limit:
                    break

                yield CourseProgressChange(self._stepik, obj)
                count += 1

            if not page['meta']['has_next']:
                break

            page_idx += 1


    def __iter__(self):
        yield from self.iterate(limit=None)

