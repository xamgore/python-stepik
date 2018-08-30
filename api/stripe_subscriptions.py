# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class StripeSubscription:
    _resources_name = 'stripe-subscriptions'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'StripeSubscription(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model StripeSubscription are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @readonly
    @property
    def user(self) -> str:
        return self._data['user']


    @property
    def customer_email(self) -> str:
        return self._data['customer_email']


    @customer_email.setter
    def customer_email(self, value: str):
        self._data['customer_email'] = value


    @readonly
    @property
    def subscription_id(self) -> str:
        return self._data['subscription_id']


    @readonly
    @property
    def update_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('update_date', "None")


    @readonly
    @property
    def valid_until(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('valid_until', "None")


    @property
    def coupon_code(self) -> str:
        return self._data['coupon_code']


    @coupon_code.setter
    def coupon_code(self, value: str):
        self._data['coupon_code'] = value


    @readonly
    @property
    def private_courses(self) -> str:
        return self._data['private_courses']


    @readonly
    @property
    def card_digits(self) -> str:
        return self._data['card_digits']


    @readonly
    @property
    def discount_end(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('discount_end', "None")


    @readonly
    @property
    def display_amount(self) -> str:
        return self._data['display_amount']




class ListOfStripeSubscriptions:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> StripeSubscription:
        return StripeSubscription(self._stepik, self._stepik._fetch_object(StripeSubscription, id))


    def get_all(self, ids: List[int], keep_order=False) -> Iterable[StripeSubscription]:
        objects = self._stepik._fetch_objects(StripeSubscription, ids)
        iterable = (StripeSubscription(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)
