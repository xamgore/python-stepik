# This file is generated
from common import required, readonly
from typing import List


class WriteStudent:
    def __init__(self, data):
        self.__data = data


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
    def __init__(self, data):
        self.__data = data


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
        default value: "2018-08-10T09:48:43.661Z"
        """
        return self.__data.setdefault('date_joined', "2018-08-10T09:48:43.661Z")


