# This file is generated
from typing import List, Iterable, Any, Optional

from stepik.errors import StepikError
from stepik.common import required, readonly
from stepik.resources_list import ResourcesList


class LongTask:
    _resources_name = 'long-tasks'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'LongTask(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model LongTask are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @readonly
    @property
    def queue_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('queue_date', "None")


    @readonly
    @property
    def start_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('start_date', "None")


    @readonly
    @property
    def finish_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('finish_date', "None")


    @required
    @readonly
    @property
    def user(self) -> str:
        return self._data['user']


    @required
    @property
    def type(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('type', "None")


    @type.setter
    def type(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self._data['type'] = value


    @readonly
    @property
    def status(self) -> str:
        return self._data['status']


    @readonly
    @property
    def result(self) -> str:
        """
        Enter a valid JSON object

        Default value: ``{}``
        """
        return self._data['result']


    @property
    def course(self) -> str:
        return self._data['course']


    @course.setter
    def course(self, value: str):
        self._data['course'] = value


    @property
    def lesson(self) -> str:
        return self._data['lesson']


    @lesson.setter
    def lesson(self, value: str):
        self._data['lesson'] = value


    @property
    def step(self) -> str:
        return self._data['step']


    @step.setter
    def step(self, value: str):
        self._data['step'] = value


    @property
    def klass(self) -> str:
        return self._data['klass']


    @klass.setter
    def klass(self, value: str):
        self._data['klass'] = value




class ListOfLongTasks:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> LongTask:
        obj = self._stepik._fetch_object(LongTask, id)
        return LongTask(self._stepik, obj)


    def get_all(self, ids: Iterable[int], keep_order=False) -> Iterable[LongTask]:
        """
        Grab a bunch of ids, usually 20 objects per request.
        """
        if keep_order:
            ids = list(ids)

        objects = self._stepik._fetch_objects(LongTask, ids)
        iterable = (LongTask(self._stepik, o) for o in objects)

        return iterable if not keep_order \
            else sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))


    def iterate(self,
                user: Any = None,
                type: str = None,
                course: Any = None,
                lesson: Any = None,
                step: Any = None,
                klass: Any = None,
                skip: int = 0, limit: Optional[int] = 20) -> Iterable[LongTask]:
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
            page = self._stepik._get(f'long-tasks?{params}&page={page_idx}&order={ordering}')

            for obj in page['long-tasks']:
                if limit and count >= limit:
                    break

                yield LongTask(self._stepik, obj)
                count += 1

            if not page['meta']['has_next']:
                break

            page_idx += 1


    def __iter__(self):
        yield from self.iterate(limit=None)


    def create(self,
               type: str,
               course: str = None,
               lesson: str = None,
               step: str = None,
               klass: str = None,
               **kwargs) -> LongTask:
        vars = locals().copy()
        data = {'long-task':
                    {k: v for k, v in {**vars, **kwargs}.items()
                     if k != 'self' and v is not None}}

        response = self._stepik._post('long-tasks', data)
        if 'long-tasks' not in response:
            raise StepikError(response)

        return LongTask(self._stepik, response['long-tasks'][0])

