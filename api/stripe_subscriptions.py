# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



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
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('update_date', "None")


    @readonly
    @property
    def valid_until(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('valid_until', "None")


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
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('discount_end', "None")


    @readonly
    @property
    def display_amount(self) -> str:
        return self.__data['display_amount']


