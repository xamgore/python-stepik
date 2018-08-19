# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class WriteStudent:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'WriteStudent(id={self.id!r})'


    @required
    @property
    def klass(self) -> str:
        return self.__data['klass']


    @klass.setter
    def klass(self, value: str):
        self.__data['klass'] = value


    @required
    @property
    def invitation_key(self) -> str:
        return self.__data['invitation_key']


    @invitation_key.setter
    def invitation_key(self, value: str):
        self.__data['invitation_key'] = value




class Student:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'Student(id={self.id!r})'


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @required
    @property
    def klass(self) -> str:
        return self.__data['klass']


    @klass.setter
    def klass(self, value: str):
        self.__data['klass'] = value


    @required
    @readonly
    @property
    def user(self) -> str:
        return self.__data['user']


    @required
    @readonly
    @property
    def date_joined(self) -> str:
        """
        Default value: ``"2018-08-10T09:48:43.661Z"``
        """
        return self.__data.setdefault('date_joined', "2018-08-10T09:48:43.661Z")


