# This file is generated
from common import required, readonly
from typing import List


class WriteAssistant:
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
    def user(self) -> str:
        return self.__data['user']


    @user.setter
    def user(self, value: str):
        self.__data['user'] = value


class Assistant:
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
    @property
    def user(self) -> str:
        return self.__data['user']


    @user.setter
    def user(self, value: str):
        self.__data['user'] = value


    @required
    @readonly
    @property
    def date_joined(self) -> str:
        """
        default value: "2018-08-10T09:47:15.843Z"
        """
        return self.__data.setdefault('date_joined', "2018-08-10T09:47:15.843Z")


