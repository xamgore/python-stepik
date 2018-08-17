# This file is generated
from common import required, readonly
from typing import List



class WriteClassPlan:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'WriteClassPlan(id={self.id!r})'


    @required
    @property
    def user(self) -> str:
        return self.__data['user']


    @user.setter
    def user(self, value: str):
        self.__data['user'] = value


    @required
    @property
    def allowed_students_count(self) -> int:
        return self.__data['allowed_students_count']


    @allowed_students_count.setter
    def allowed_students_count(self, value: int):
        self.__data['allowed_students_count'] = value


    @required
    @property
    def students_count(self) -> int:
        """
        Default value: 0
        """
        return self.__data['students_count']


    @students_count.setter
    def students_count(self, value: int):
        """
        Default value: 0
        """
        self.__data['students_count'] = value




class ClassPlan:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'ClassPlan(id={self.id!r})'


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
    def allowed_students_count(self) -> int:
        return self.__data['allowed_students_count']


    @allowed_students_count.setter
    def allowed_students_count(self, value: int):
        self.__data['allowed_students_count'] = value


    @required
    @property
    def students_count(self) -> int:
        """
        Default value: 0
        """
        return self.__data['students_count']


    @students_count.setter
    def students_count(self, value: int):
        """
        Default value: 0
        """
        self.__data['students_count'] = value


    @readonly
    @property
    def is_access_restricted(self) -> str:
        return self.__data['is_access_restricted']


