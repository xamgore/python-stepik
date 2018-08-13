# This file is generated
from common import required, readonly
from typing import List


class WriteCoursePayment:
    def __init__(self, data):
        self.__data = data


    @required
    @property
    def course(self) -> str:
        return self.__data['course']


    @course.setter
    def course(self, value: str):
        self.__data['course'] = value


    @property
    def amount(self) -> float:
        return self.__data['amount']


    @amount.setter
    def amount(self, value: float):
        self.__data['amount'] = value


class CoursePayment:
    def __init__(self, data):
        self.__data = data


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
        return self.__data['amount']


    @amount.setter
    def amount(self, value: float):
        self.__data['amount'] = value


    @readonly
    @property
    def currency_code(self) -> str:
        """
        Type: choice
        """
        return self.__data['currency_code']


    @readonly
    @property
    def payment_date(self) -> str:
        """
        Type: datetime
        """
        return self.__data['payment_date']


    @readonly
    @property
    def cancel_date(self) -> str:
        """
        Type: datetime
        """
        return self.__data['cancel_date']


    @readonly
    @property
    def status(self) -> str:
        """
        Type: choice
        """
        return self.__data['status']


    @readonly
    @property
    def comment(self) -> str:
        return self.__data['comment']


    @readonly
    @property
    def is_paid(self) -> bool:
        return self.__data['is_paid']


