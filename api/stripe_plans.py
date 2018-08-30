# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class StripePlan:
    _resources_name = 'stripe-plans'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'StripePlan(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model StripePlan are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @property
    def code(self) -> str:
        return self._data['code']


    @code.setter
    def code(self, value: str):
        self._data['code'] = value


    @required
    @property
    def currency(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('currency', "None")


    @currency.setter
    def currency(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self._data['currency'] = value




class ListOfStripePlans:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get_all(self, ids: List[int], keep_order=False) -> Iterable[StripePlan]:
        objects = self._stepik._fetch_objects(StripePlan, ids)
        iterable = (StripePlan(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)
