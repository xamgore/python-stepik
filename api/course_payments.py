# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class CoursePayment:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'CoursePayment(id={self.id!r})'


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @required
    @readonly
    @property
    def user(self) -> str:
        return self.__data['user']


    @required
    @property
    def course(self) -> str:
        return self.__data['course']


    @course.setter
    def course(self, value: str):
        self.__data['course'] = value


    @readonly
    @property
    def redirect_url(self) -> str:
        return self.__data['redirect_url']


    @property
    def amount(self) -> float:
        """
        Default value: ``"None"``
        """
        return self.__data.setdefault('amount', "None")


    @amount.setter
    def amount(self, value: float):
        """
        Default value: ``"None"``
        """
        self.__data['amount'] = value


    @readonly
    @property
    def currency_code(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('currency_code', "None")


    @readonly
    @property
    def payment_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('payment_date', "None")


    @readonly
    @property
    def cancel_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('cancel_date', "None")


    @readonly
    @property
    def status(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('status', "None")


    @readonly
    @property
    def comment(self) -> str:
        return self.__data['comment']


    @readonly
    @property
    def is_paid(self) -> bool:
        return self.__data['is_paid']


