# This file is generated
from common import required, readonly
from typing import List



class WriteStripeSubscription:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'WriteStripeSubscription(id={self.id!r})'


    @property
    def customer_email(self) -> str:
        return self.__data['customer_email']


    @customer_email.setter
    def customer_email(self, value: str):
        self.__data['customer_email'] = value


    @property
    def coupon_code(self) -> str:
        return self.__data['coupon_code']


    @coupon_code.setter
    def coupon_code(self, value: str):
        self.__data['coupon_code'] = value




class StripeSubscription:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'StripeSubscription(id={self.id!r})'


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @required
    @readonly
    @property
    def user(self) -> str:
        return self.__data['user']


    @property
    def customer_email(self) -> str:
        return self.__data['customer_email']


    @customer_email.setter
    def customer_email(self, value: str):
        self.__data['customer_email'] = value


    @readonly
    @property
    def subscription_id(self) -> str:
        return self.__data['subscription_id']


    @readonly
    @property
    def update_date(self) -> str:
        """
        Type: datetime
        """
        return self.__data['update_date']


    @readonly
    @property
    def valid_until(self) -> str:
        """
        Type: datetime
        """
        return self.__data['valid_until']


    @property
    def coupon_code(self) -> str:
        return self.__data['coupon_code']


    @coupon_code.setter
    def coupon_code(self, value: str):
        self.__data['coupon_code'] = value


    @readonly
    @property
    def private_courses(self) -> str:
        return self.__data['private_courses']


    @readonly
    @property
    def card_digits(self) -> str:
        return self.__data['card_digits']


    @readonly
    @property
    def discount_end(self) -> str:
        """
        Type: datetime
        """
        return self.__data['discount_end']


    @readonly
    @property
    def display_amount(self) -> str:
        return self.__data['display_amount']


