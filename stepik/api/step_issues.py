# This file is generated
from typing import List, Iterable, Any, Optional

from stepik.errors import StepikError
from stepik.common import required, readonly
from stepik.resources_list import ResourcesList


class StepIssue:
    _resources_name = 'step-issues'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'StepIssue(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model StepIssue are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @property
    def step(self) -> str:
        return self._data['step']


    @step.setter
    def step(self, value: str):
        self._data['step'] = value


    @required
    @property
    def epoch_time(self) -> str:
        """
        Default value: ``"2018-08-26T00:35:43.217Z"``

        Type: str
        """
        return self._data.setdefault('epoch_time', "2018-08-26T00:35:43.217Z")


    @epoch_time.setter
    def epoch_time(self, value: str):
        """
        Default value: ``"2018-08-26T00:35:43.217Z"``

        Type: str
        """
        self._data['epoch_time'] = value


    @property
    def has_quiz_error(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['has_quiz_error']


    @has_quiz_error.setter
    def has_quiz_error(self, value: bool):
        """
        Default value: ``False``
        """
        self._data['has_quiz_error'] = value


    @property
    def has_quiz_warning(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['has_quiz_warning']


    @has_quiz_warning.setter
    def has_quiz_warning(self, value: bool):
        """
        Default value: ``False``
        """
        self._data['has_quiz_warning'] = value


    @required
    @property
    def unique_views(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['unique_views']


    @unique_views.setter
    def unique_views(self, value: int):
        """
        Default value: ``0``
        """
        self._data['unique_views'] = value


    @required
    @property
    def total_views(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['total_views']


    @total_views.setter
    def total_views(self, value: int):
        """
        Default value: ``0``
        """
        self._data['total_views'] = value


    @required
    @property
    def unique_successes(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['unique_successes']


    @unique_successes.setter
    def unique_successes(self, value: int):
        """
        Default value: ``0``
        """
        self._data['unique_successes'] = value


    @required
    @property
    def unique_failures(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['unique_failures']


    @unique_failures.setter
    def unique_failures(self, value: int):
        """
        Default value: ``0``
        """
        self._data['unique_failures'] = value


    @required
    @property
    def unique_attempts(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['unique_attempts']


    @unique_attempts.setter
    def unique_attempts(self, value: int):
        """
        Default value: ``0``
        """
        self._data['unique_attempts'] = value


    @required
    @property
    def unique_correct_ratio(self) -> str:
        """
        Default value: ``"0"``

        Type: str
        """
        return self._data.setdefault('unique_correct_ratio', "0")


    @unique_correct_ratio.setter
    def unique_correct_ratio(self, value: str):
        """
        Default value: ``"0"``

        Type: str
        """
        self._data['unique_correct_ratio'] = value


    @required
    @property
    def total_successes(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['total_successes']


    @total_successes.setter
    def total_successes(self, value: int):
        """
        Default value: ``0``
        """
        self._data['total_successes'] = value


    @required
    @property
    def total_failures(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['total_failures']


    @total_failures.setter
    def total_failures(self, value: int):
        """
        Default value: ``0``
        """
        self._data['total_failures'] = value


    @required
    @property
    def total_attempts(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['total_attempts']


    @total_attempts.setter
    def total_attempts(self, value: int):
        """
        Default value: ``0``
        """
        self._data['total_attempts'] = value


    @required
    @property
    def total_correct_ratio(self) -> str:
        """
        Default value: ``"0"``

        Type: str
        """
        return self._data.setdefault('total_correct_ratio', "0")


    @total_correct_ratio.setter
    def total_correct_ratio(self, value: str):
        """
        Default value: ``"0"``

        Type: str
        """
        self._data['total_correct_ratio'] = value


    @required
    @property
    def total_comments(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['total_comments']


    @total_comments.setter
    def total_comments(self, value: int):
        """
        Default value: ``0``
        """
        self._data['total_comments'] = value


    @required
    @property
    def pending_comments(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['pending_comments']


    @pending_comments.setter
    def pending_comments(self, value: int):
        """
        Default value: ``0``
        """
        self._data['pending_comments'] = value


    @required
    @property
    def deleted_comments(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['deleted_comments']


    @deleted_comments.setter
    def deleted_comments(self, value: int):
        """
        Default value: ``0``
        """
        self._data['deleted_comments'] = value


    @required
    @property
    def epic_comment_votes(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['epic_comment_votes']


    @epic_comment_votes.setter
    def epic_comment_votes(self, value: int):
        """
        Default value: ``0``
        """
        self._data['epic_comment_votes'] = value


    @required
    @property
    def abuse_comment_votes(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['abuse_comment_votes']


    @abuse_comment_votes.setter
    def abuse_comment_votes(self, value: int):
        """
        Default value: ``0``
        """
        self._data['abuse_comment_votes'] = value


    @required
    @property
    def total_reviews(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['total_reviews']


    @total_reviews.setter
    def total_reviews(self, value: int):
        """
        Default value: ``0``
        """
        self._data['total_reviews'] = value


    @required
    @property
    def reviews_outliers(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['reviews_outliers']


    @reviews_outliers.setter
    def reviews_outliers(self, value: int):
        """
        Default value: ``0``
        """
        self._data['reviews_outliers'] = value


    @required
    @property
    def plagiarized_submissions(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['plagiarized_submissions']


    @plagiarized_submissions.setter
    def plagiarized_submissions(self, value: int):
        """
        Default value: ``0``
        """
        self._data['plagiarized_submissions'] = value


    @required
    @property
    def magic(self) -> str:
        """
        Default value: ``"0"``

        Type: str
        """
        return self._data.setdefault('magic', "0")


    @magic.setter
    def magic(self, value: str):
        """
        Default value: ``"0"``

        Type: str
        """
        self._data['magic'] = value


    @required
    @property
    def discrimination(self) -> str:
        """
        Default value: ``"0"``

        Type: str
        """
        return self._data.setdefault('discrimination', "0")


    @discrimination.setter
    def discrimination(self, value: str):
        """
        Default value: ``"0"``

        Type: str
        """
        self._data['discrimination'] = value




class ListOfStepIssues:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> StepIssue:
        obj = self._stepik._fetch_object(StepIssue, id)
        return StepIssue(self._stepik, obj)


    def get_all(self, ids: Iterable[int], keep_order=False) -> Iterable[StepIssue]:
        """
        Grab a bunch of ids, usually 20 objects per request.
        """
        if keep_order:
            ids = list(ids)

        objects = self._stepik._fetch_objects(StepIssue, ids)
        iterable = (StepIssue(self._stepik, o) for o in objects)

        return iterable if not keep_order \
            else sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))


    def iterate(self,
                step: Any = None,
                course: Any = None,
                kind: Any = None,
                skip: int = 0, limit: Optional[int] = 20) -> Iterable[StepIssue]:
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
            page = self._stepik._get(f'step-issues?{params}&page={page_idx}&order={ordering}')

            for obj in page['step-issues']:
                if limit and count >= limit:
                    break

                yield StepIssue(self._stepik, obj)
                count += 1

            if not page['meta']['has_next']:
                break

            page_idx += 1


    def __iter__(self):
        yield from self.iterate(limit=None)


    def delete(self, id: int) -> dict:
        """Delete the object by its id. Returns the server's response"""
        return self._stepik._delete('step-issues', id)

