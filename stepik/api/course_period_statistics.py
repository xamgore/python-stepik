# This file is generated
from typing import List, Iterable, Any, Optional

from stepik.errors import StepikError
from stepik.common import required, readonly
from stepik.resources_list import ResourcesList


class CoursePeriodStatistics:
    _resources_name = 'course-period-statistics'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'CoursePeriodStatistics(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model CoursePeriodStatistics are missing')


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


    @property
    def from_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('from_date', "None")


    @from_date.setter
    def from_date(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self._data['from_date'] = value


    @property
    def to_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('to_date', "None")


    @to_date.setter
    def to_date(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self._data['to_date'] = value


    @required
    @property
    def active_learners_count(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['active_learners_count']


    @active_learners_count.setter
    def active_learners_count(self, value: int):
        """
        Default value: ``0``
        """
        self._data['active_learners_count'] = value


    @required
    @property
    def active_learners_delta(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['active_learners_delta']


    @active_learners_delta.setter
    def active_learners_delta(self, value: int):
        """
        Default value: ``0``
        """
        self._data['active_learners_delta'] = value


    @required
    @property
    def submissions_count(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['submissions_count']


    @submissions_count.setter
    def submissions_count(self, value: int):
        """
        Default value: ``0``
        """
        self._data['submissions_count'] = value


    @required
    @property
    def submissions_delta(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['submissions_delta']


    @submissions_delta.setter
    def submissions_delta(self, value: int):
        """
        Default value: ``0``
        """
        self._data['submissions_delta'] = value


    @required
    @property
    def certificates_count(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['certificates_count']


    @certificates_count.setter
    def certificates_count(self, value: int):
        """
        Default value: ``0``
        """
        self._data['certificates_count'] = value


    @required
    @property
    def certificates_delta(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['certificates_delta']


    @certificates_delta.setter
    def certificates_delta(self, value: int):
        """
        Default value: ``0``
        """
        self._data['certificates_delta'] = value


    @required
    @property
    def comments_count(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['comments_count']


    @comments_count.setter
    def comments_count(self, value: int):
        """
        Default value: ``0``
        """
        self._data['comments_count'] = value


    @required
    @property
    def comments_delta(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['comments_delta']


    @comments_delta.setter
    def comments_delta(self, value: int):
        """
        Default value: ``0``
        """
        self._data['comments_delta'] = value


    @required
    @property
    def enrollments_count(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['enrollments_count']


    @enrollments_count.setter
    def enrollments_count(self, value: int):
        """
        Default value: ``0``
        """
        self._data['enrollments_count'] = value


    @required
    @property
    def enrollments_delta(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['enrollments_delta']


    @enrollments_delta.setter
    def enrollments_delta(self, value: int):
        """
        Default value: ``0``
        """
        self._data['enrollments_delta'] = value


    @required
    @property
    def dropouts_count(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['dropouts_count']


    @dropouts_count.setter
    def dropouts_count(self, value: int):
        """
        Default value: ``0``
        """
        self._data['dropouts_count'] = value


    @required
    @property
    def dropouts_delta(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['dropouts_delta']


    @dropouts_delta.setter
    def dropouts_delta(self, value: int):
        """
        Default value: ``0``
        """
        self._data['dropouts_delta'] = value


    @readonly
    @property
    def update_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('update_date', "None")




class ListOfCoursePeriodStatistics:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> CoursePeriodStatistics:
        obj = self._stepik._fetch_object(CoursePeriodStatistics, id)
        return CoursePeriodStatistics(self._stepik, obj)


    def get_all(self, ids: Iterable[int], keep_order=False) -> Iterable[CoursePeriodStatistics]:
        """
        Grab a bunch of ids, usually 20 objects per request.
        """
        if keep_order:
            ids = list(ids)

        objects = self._stepik._fetch_objects(CoursePeriodStatistics, ids)
        iterable = (CoursePeriodStatistics(self._stepik, o) for o in objects)

        return iterable if not keep_order \
            else sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))


    def iterate(self,
                course: Any = None,
                is_featured: bool = None,
                schedule_type: str = None,
                skip: int = 0, limit: Optional[int] = 20) -> Iterable[CoursePeriodStatistics]:
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
            page = self._stepik._get(f'course-period-statistics?{params}&page={page_idx}&order={ordering}')

            for obj in page['course-period-statistics']:
                if limit and count >= limit:
                    break

                yield CoursePeriodStatistics(self._stepik, obj)
                count += 1

            if not page['meta']['has_next']:
                break

            page_idx += 1


    def __iter__(self):
        yield from self.iterate(limit=None)

