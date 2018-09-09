# This file is generated
from typing import List, Iterable, Any, Optional

from stepik.errors import StepikError
from stepik.common import required, readonly
from stepik.resources_list import ResourcesList


class Submission:
    """
    Submission resource.
    """

    _resources_name = 'submissions'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'Submission(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model Submission are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @readonly
    @property
    def status(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('status', "None")


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
    def hint(self) -> str:
        return self._data['hint']


    @readonly
    @property
    def feedback(self) -> str:
        return self._data['feedback']


    @readonly
    @property
    def time(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('time', "None")


    @property
    def reply(self) -> str:
        """
        Default value: ``{}``
        """
        return self._data['reply']


    @reply.setter
    def reply(self, value: str):
        """
        Default value: ``{}``
        """
        self._data['reply'] = value


    @readonly
    @property
    def reply_url(self) -> str:
        return self._data['reply_url']


    @required
    @property
    def attempt(self) -> str:
        return self._data['attempt']


    @attempt.setter
    def attempt(self, value: str):
        self._data['attempt'] = value


    @required
    @readonly
    @property
    def session(self) -> str:
        return self._data['session']


    @readonly
    @property
    def eta(self) -> int:
        return self._data['eta']




class ListOfSubmissions:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> Submission:
        obj = self._stepik._fetch_object(Submission, id)
        return Submission(self._stepik, obj)


    def get_all(self, ids: Iterable[int], keep_order=False) -> Iterable[Submission]:
        """
        Grab a bunch of ids, usually 20 objects per request.
        """
        if keep_order:
            ids = list(ids)

        objects = self._stepik._fetch_objects(Submission, ids)
        iterable = (Submission(self._stepik, o) for o in objects)

        return iterable if not keep_order \
            else sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))


    def iterate(self,
                status: str = None,
                user_name: str = None,
                step: str = None,
                user: str = None,
                attempt: str = None,
                search: str = None,
                order: str = None,
                review_status: str = None,
                by_desc: bool = None,
                skip: int = 0, limit: Optional[int] = 20) -> Iterable[Submission]:
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
            page = self._stepik._get(f'submissions?{params}&page={page_idx}&order={ordering}')

            for obj in page['submissions']:
                if limit and count >= limit:
                    break

                yield Submission(self._stepik, obj)
                count += 1

            if not page['meta']['has_next']:
                break

            page_idx += 1


    def __iter__(self):
        yield from self.iterate(limit=None)


    def create(self,
               attempt: str,
               reply: str = None,
               **kwargs) -> Submission:
        vars = locals().copy()
        data = {'submission':
                    {k: v for k, v in {**vars, **kwargs}.items()
                     if k != 'self' and v is not None}}

        response = self._stepik._post('submissions', data)
        if 'submissions' not in response:
            raise StepikError(response)

        return Submission(self._stepik, response['submissions'][0])

