# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


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
        return LongTask(self._stepik, self._stepik._fetch_object(LongTask, id))


    def get_all(self, ids: List[int], keep_order=False) -> Iterable[LongTask]:
        objects = self._stepik._fetch_objects(LongTask, ids)
        iterable = (LongTask(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)


    def create(self, type: str, course: str = None, lesson: str = None, step: str = None, klass: str = None) -> LongTask:
        vars = locals().copy()
        data = {'long-task': {k: v for k, v in vars.items() if k != 'self' and v is not None}}

        resources_name = 'long-tasks'
        response = self._stepik._post(resources_name, data)

        if resources_name not in response:
            raise StepikError(response)

        return LongTask(self._stepik, response[resources_name][0])
