# This file is generated
from typing import List, Iterable, Any, Optional

from stepik.errors import StepikError
from stepik.common import required, readonly
from stepik.resources_list import ResourcesList


class UserCodeRun:
    _resources_name = 'user-code-runs'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'UserCodeRun(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model UserCodeRun are missing')


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
    def step(self) -> str:
        return self._data['step']


    @step.setter
    def step(self, value: str):
        self._data['step'] = value


    @required
    @property
    def language(self) -> str:
        return self._data['language']


    @language.setter
    def language(self, value: str):
        self._data['language'] = value


    @required
    @property
    def code(self) -> str:
        return self._data['code']


    @code.setter
    def code(self, value: str):
        self._data['code'] = value


    @readonly
    @property
    def status(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('status', "None")


    @required
    @property
    def stdin(self) -> str:
        return self._data['stdin']


    @stdin.setter
    def stdin(self, value: str):
        self._data['stdin'] = value


    @required
    @readonly
    @property
    def stdout(self) -> str:
        return self._data['stdout']


    @required
    @readonly
    @property
    def stderr(self) -> str:
        return self._data['stderr']


    @readonly
    @property
    def time_limit_exceeded(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['time_limit_exceeded']


    @readonly
    @property
    def memory_limit_exceeded(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['memory_limit_exceeded']


    @readonly
    @property
    def create_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('create_date', "None")


    @readonly
    @property
    def update_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('update_date', "None")




class ListOfUserCodeRuns:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> UserCodeRun:
        obj = self._stepik._fetch_object(UserCodeRun, id)
        return UserCodeRun(self._stepik, obj)


    def get_all(self, ids: Iterable[int], keep_order=False) -> Iterable[UserCodeRun]:
        """
        Grab a bunch of ids, usually 20 objects per request.
        """
        if keep_order:
            ids = list(ids)

        objects = self._stepik._fetch_objects(UserCodeRun, ids)
        iterable = (UserCodeRun(self._stepik, o) for o in objects)

        return iterable if not keep_order \
            else sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))


    def iterate(self,
                skip: int = 0, limit: Optional[int] = 20) -> Iterable[UserCodeRun]:
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
            page = self._stepik._get(f'user-code-runs?{params}&page={page_idx}&order={ordering}')

            for obj in page['user-code-runs']:
                if limit and count >= limit:
                    break

                yield UserCodeRun(self._stepik, obj)
                count += 1

            if not page['meta']['has_next']:
                break

            page_idx += 1


    def __iter__(self):
        yield from self.iterate(limit=None)


    def create(self,
               user: str,
               step: str,
               language: str,
               code: str,
               stdin: str,
               **kwargs) -> UserCodeRun:
        vars = locals().copy()
        data = {'user-code-run':
                    {k: v for k, v in {**vars, **kwargs}.items()
                     if k != 'self' and v is not None}}

        response = self._stepik._post('user-code-runs', data)
        if 'user-code-runs' not in response:
            raise StepikError(response)

        return UserCodeRun(self._stepik, response['user-code-runs'][0])

