# This file is generated
from typing import List, Iterable, Any, Optional

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
        obj = self._stepik._fetch_object(StripeSubscription, id)
        return StripeSubscription(self._stepik, obj)


    def get_all(self, ids: Iterable[int], keep_order=False) -> Iterable[StripeSubscription]:
        """
        Grab a bunch of ids, usually 20 objects per request.
        """
        if keep_order:
            ids = list(ids)

        objects = self._stepik._fetch_objects(StripeSubscription, ids)
        iterable = (StripeSubscription(self._stepik, o) for o in objects)

        return iterable if not keep_order \
            else sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))


    def iterate(self,
                skip: int = 0, limit: Optional[int] = 20) -> Iterable[StripeSubscription]:
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
            page = self._stepik._get(f'stripe-subscriptions?{params}&page={page_idx}&order={ordering}')

            for obj in page['stripe-subscriptions']:
                if limit and count >= limit:
                    break

                yield StripeSubscription(self._stepik, obj)
                count += 1

            if not page['meta']['has_next']:
                break

            page_idx += 1


    def __iter__(self):
        yield from self.iterate(limit=None)

