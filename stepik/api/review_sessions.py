# This file is generated
from typing import List, Iterable, Any, Optional

from stepik.errors import StepikError
from stepik.common import required, readonly
from stepik.resources_list import ResourcesList


class Session:
    """
    ReviewSession resource.
    ReviewSession represents a state of reviewing process.
    """

    _resources_name = 'review-sessions'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'Session(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model Session are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @property
    def instruction(self) -> str:
        return self._data['instruction']


    @instruction.setter
    def instruction(self, value: str):
        self._data['instruction'] = value


    @property
    def submission(self) -> str:
        return self._data['submission']


    @submission.setter
    def submission(self, value: str):
        self._data['submission'] = value


    @readonly
    @property
    def given_reviews(self) -> str:
        return self._data['given_reviews']


    @readonly
    @property
    def is_giving_started(self) -> str:
        return self._data['is_giving_started']


    @readonly
    @property
    def is_giving_finished(self) -> str:
        return self._data['is_giving_finished']


    @readonly
    @property
    def taken_reviews(self) -> str:
        return self._data['taken_reviews']


    @readonly
    @property
    def is_taking_started(self) -> str:
        return self._data['is_taking_started']


    @readonly
    @property
    def is_taking_finished(self) -> str:
        return self._data['is_taking_finished']


    @readonly
    @property
    def is_taking_finished_by_teacher(self) -> str:
        return self._data['is_taking_finished_by_teacher']


    @readonly
    @property
    def when_taking_finished_by_teacher(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('when_taking_finished_by_teacher', "None")


    @readonly
    @property
    def is_review_available(self) -> str:
        return self._data['is_review_available']


    @readonly
    @property
    def is_finished(self) -> str:
        return self._data['is_finished']


    @required
    @readonly
    @property
    def score(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['score']


    @readonly
    @property
    def available_reviews_count(self) -> str:
        return self._data['available_reviews_count']


    @readonly
    @property
    def active_review(self) -> str:
        return self._data['active_review']


    @readonly
    @property
    def actions(self) -> str:
        return self._data['actions']




class ListOfReviewSessions:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> Session:
        obj = self._stepik._fetch_object(Session, id)
        return Session(self._stepik, obj)


    def get_all(self, ids: Iterable[int], keep_order=False) -> Iterable[Session]:
        """
        Grab a bunch of ids, usually 20 objects per request.
        """
        if keep_order:
            ids = list(ids)

        objects = self._stepik._fetch_objects(Session, ids)
        iterable = (Session(self._stepik, o) for o in objects)

        return iterable if not keep_order \
            else sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))


    def iterate(self,
                skip: int = 0, limit: Optional[int] = 20) -> Iterable[Session]:
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
            page = self._stepik._get(f'review-sessions?{params}&page={page_idx}&order={ordering}')

            for obj in page['review-sessions']:
                if limit and count >= limit:
                    break

                yield Session(self._stepik, obj)
                count += 1

            if not page['meta']['has_next']:
                break

            page_idx += 1


    def __iter__(self):
        yield from self.iterate(limit=None)

