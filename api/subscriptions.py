# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class Subscription:
    _resources_name = 'subscriptions'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'Subscription(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model Subscription are missing')


    @readonly
    @property
    def id(self) -> str:
        return self._data['id']


    @readonly
    @property
    def action(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('action', "None")


    @property
    def is_active(self) -> str:
        return self._data['is_active']


    @is_active.setter
    def is_active(self, value: str):
        self._data['is_active'] = value




class ListOfSubscriptions:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: str) -> Subscription:
        return Subscription(self._stepik, self._stepik._fetch_object(Subscription, id))


    def get_all(self, ids: List[str], keep_order=False) -> Iterable[Subscription]:
        objects = self._stepik._fetch_objects(Subscription, ids)
        iterable = (Subscription(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)
