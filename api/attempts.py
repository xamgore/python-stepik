# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class Attempt:
    _resources_name = 'attempts'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'Attempt(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model Attempt are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @readonly
    @property
    def dataset(self) -> str:
        return self._data['dataset']


    @readonly
    @property
    def dataset_url(self) -> str:
        return self._data['dataset_url']


    @readonly
    @property
    def time(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('time', "None")


    @readonly
    @property
    def status(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('status', "None")


    @readonly
    @property
    def time_left(self) -> int:
        return self._data['time_left']


    @required
    @property
    def step(self) -> str:
        return self._data['step']


    @step.setter
    def step(self, value: str):
        self._data['step'] = value


    @readonly
    @property
    def user(self) -> str:
        return self._data['user']




class ListOfAttempts:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> Attempt:
        return Attempt(self._stepik, self._stepik._fetch_object(Attempt, id))


    def get_all(self, ids: List[int], keep_order=False) -> Iterable[Attempt]:
        objects = self._stepik._fetch_objects(Attempt, ids)
        iterable = (Attempt(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)


    def create(self, step: str) -> Attempt:
        vars = locals().copy()
        data = {'attempt': {k: v for k, v in vars.items() if k != 'self' and v is not None}}

        resources_name = 'attempts'
        response = self._stepik._post(resources_name, data)

        if resources_name not in response:
            raise StepikError(response)

        return Attempt(self._stepik, response[resources_name][0])
