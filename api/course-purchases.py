# This file is generated
from common import required, readonly
from typing import List



class WriteCoursePurchase:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'WriteCoursePurchase(id={self.id!r})'


    @required
    @property
    def user(self) -> str:
        return self.__data['user']


    @user.setter
    def user(self, value: str):
        self.__data['user'] = value


    @required
    @property
    def course(self) -> str:
        return self.__data['course']


    @course.setter
    def course(self, value: str):
        self.__data['course'] = value


    @property
    def payment(self) -> str:
        return self.__data['payment']


    @payment.setter
    def payment(self, value: str):
        self.__data['payment'] = value


    @property
    def cancel_date(self) -> str:
        """
        Type: datetime
        """
        return self.__data['cancel_date']


    @cancel_date.setter
    def cancel_date(self, value: str):
        """
        Type: datetime
        """
        self.__data['cancel_date'] = value




class CoursePurchase:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'CoursePurchase(id={self.id!r})'


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @required
    @property
    def user(self) -> str:
        return self.__data['user']


    @user.setter
    def user(self, value: str):
        self.__data['user'] = value


    @required
    @property
    def course(self) -> str:
        return self.__data['course']


    @course.setter
    def course(self, value: str):
        self.__data['course'] = value


    @readonly
    @property
    def is_active(self) -> bool:
        return self.__data['is_active']


    @property
    def payment(self) -> str:
        return self.__data['payment']


    @payment.setter
    def payment(self, value: str):
        self.__data['payment'] = value


    @readonly
    @property
    def create_date(self) -> str:
        """
        Type: datetime
        """
        return self.__data['create_date']


    @property
    def cancel_date(self) -> str:
        """
        Type: datetime
        """
        return self.__data['cancel_date']


    @cancel_date.setter
    def cancel_date(self, value: str):
        """
        Type: datetime
        """
        self.__data['cancel_date'] = value


