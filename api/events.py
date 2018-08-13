# This file is generated
from common import required, readonly
from typing import List


class WriteEvent:
    def __init__(self, data):
        self.__data = data


    @required
    @property
    def time(self) -> str:
        """
        default value: "2018-08-10T09:47:46.439Z"
        """
        return self.__data.setdefault('time', "2018-08-10T09:47:46.439Z")


    @time.setter
    def time(self, value: str):
        """
        default value: "2018-08-10T09:47:46.439Z"
        """
        self.__data['time'] = value


class Event:
    def __init__(self, data):
        self.__data = data


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @required
    @property
    def time(self) -> str:
        """
        default value: "2018-08-10T09:47:46.439Z"
        """
        return self.__data.setdefault('time', "2018-08-10T09:47:46.439Z")


    @time.setter
    def time(self, value: str):
        """
        default value: "2018-08-10T09:47:46.439Z"
        """
        self.__data['time'] = value


    @readonly
    @property
    def type(self) -> str:
        return self.__data['type']


    @readonly
    @property
    def action(self) -> str:
        """
        Type: choice
        """
        return self.__data['action']


    @readonly
    @property
    def html_text(self) -> str:
        return self.__data['html_text']


