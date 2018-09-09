# This file is generated
from typing import List, Iterable, Any, Optional

from stepik.errors import StepikError
from stepik.common import required, readonly
from stepik.resources_list import ResourcesList


class CourseGrade:
    """
    Course grade resource.
    """

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
        obj = self._stepik._fetch_object(CourseGrade, id)
        return CourseGrade(self._stepik, obj)


    def get_all(self, ids: Iterable[int], keep_order=False) -> Iterable[CourseGrade]:
        """
        Grab a bunch of ids, usually 20 objects per request.
        """
        if keep_order:
            ids = list(ids)

        objects = self._stepik._fetch_objects(CourseGrade, ids)
        iterable = (CourseGrade(self._stepik, o) for o in objects)

        return iterable if not keep_order \
            else sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))


    def iterate(self,
                course: str = None,
                user: str = None,
                is_teacher: bool = None,
                order: Any = None,
                klass: Any = None,
                search: str = None,
                skip: int = 0, limit: Optional[int] = 20) -> Iterable[CourseGrade]:
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
            page = self._stepik._get(f'course-grades?{params}&page={page_idx}&order={ordering}')

            for obj in page['course-grades']:
                if limit and count >= limit:
                    break

                yield CourseGrade(self._stepik, obj)
                count += 1

            if not page['meta']['has_next']:
                break

            page_idx += 1


    def __iter__(self):
        yield from self.iterate(limit=None)

