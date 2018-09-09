# This file is generated
from typing import List, Iterable, Any, Optional

from stepik.errors import StepikError
from stepik.common import required, readonly
from stepik.resources_list import ResourcesList


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
        obj = self._stepik._fetch_object(CourseReviewSummary, id)
        return CourseReviewSummary(self._stepik, obj)


    def get_all(self, ids: Iterable[int], keep_order=False) -> Iterable[CourseReviewSummary]:
        """
        Grab a bunch of ids, usually 20 objects per request.
        """
        if keep_order:
            ids = list(ids)

        objects = self._stepik._fetch_objects(CourseReviewSummary, ids)
        iterable = (CourseReviewSummary(self._stepik, o) for o in objects)

        return iterable if not keep_order \
            else sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))


    def iterate(self,
                by_id: bool = None,
                by_average: bool = None,
                by_count: bool = None,
                skip: int = 0, limit: Optional[int] = 20) -> Iterable[CourseReviewSummary]:
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
            page = self._stepik._get(f'course-review-summaries?{params}&page={page_idx}&order={ordering}')

            for obj in page['course-review-summaries']:
                if limit and count >= limit:
                    break

                yield CourseReviewSummary(self._stepik, obj)
                count += 1

            if not page['meta']['has_next']:
                break

            page_idx += 1


    def __iter__(self):
        yield from self.iterate(limit=None)

