# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class CoursePurchase:
    _resources_name = 'course-purchases'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'CoursePurchase(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model CoursePurchase are missing')


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
    def course(self) -> str:
        return self._data['course']


    @course.setter
    def course(self, value: str):
        self._data['course'] = value


    @readonly
    @property
    def is_active(self) -> bool:
        return self._data['is_active']


    @property
    def payment(self) -> str:
        return self._data['payment']


    @payment.setter
    def payment(self, value: str):
        self._data['payment'] = value


    @readonly
    @property
    def create_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('create_date', "None")


    @property
    def cancel_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('cancel_date', "None")


    @cancel_date.setter
    def cancel_date(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self._data['cancel_date'] = value




class ListOfCoursePurchases:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> CoursePurchase:
        return CoursePurchase(self._stepik, self._stepik._fetch_object(CoursePurchase, id))


    def get_all(self, ids: List[int], keep_order=False) -> Iterable[CoursePurchase]:
        objects = self._stepik._fetch_objects(CoursePurchase, ids)
        iterable = (CoursePurchase(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)
