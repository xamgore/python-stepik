# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class CoursePayment:
    _resources_name = 'course-payments'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'CoursePayment(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model CoursePayment are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @readonly
    @property
    def user(self) -> str:
        return self._data['user']


    @required
    @property
    def course(self) -> str:
        return self._data['course']


    @course.setter
    def course(self, value: str):
        self._data['course'] = value


    @readonly
    @property
    def redirect_url(self) -> str:
        return self._data['redirect_url']


    @property
    def amount(self) -> float:
        """
        Default value: ``"None"``
        """
        return self._data.setdefault('amount', "None")


    @amount.setter
    def amount(self, value: float):
        """
        Default value: ``"None"``
        """
        self._data['amount'] = value


    @readonly
    @property
    def currency_code(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('currency_code', "None")


    @readonly
    @property
    def payment_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('payment_date', "None")


    @readonly
    @property
    def cancel_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('cancel_date', "None")


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
    def comment(self) -> str:
        return self._data['comment']


    @readonly
    @property
    def is_paid(self) -> bool:
        return self._data['is_paid']




class ListOfCoursePayments:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> CoursePayment:
        return CoursePayment(self._stepik, self._stepik._fetch_object(CoursePayment, id))


    def get_all(self, ids: List[int], keep_order=False) -> Iterable[CoursePayment]:
        objects = self._stepik._fetch_objects(CoursePayment, ids)
        iterable = (CoursePayment(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)


    def create(self, course: str, amount: float = None) -> CoursePayment:
        vars = locals().copy()
        data = {'course-payment': {k: v for k, v in vars.items() if k != 'self' and v is not None}}

        resources_name = 'course-payments'
        response = self._stepik._post(resources_name, data)

        if resources_name not in response:
            raise StepikError(response)

        return CoursePayment(self._stepik, response[resources_name][0])
