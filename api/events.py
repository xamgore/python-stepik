# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class WriteEvent:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'WriteEvent(id={self.id!r})'


    @required
    @property
    def time(self) -> str:
        """
        Default value: ``"2018-08-10T09:47:46.439Z"``
        """
        return self.__data.setdefault('time', "2018-08-10T09:47:46.439Z")


    @time.setter
    def time(self, value: str):
        """
        Default value: ``"2018-08-10T09:47:46.439Z"``
        """
        self.__data['time'] = value




class Event:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'Event(id={self.id!r})'


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @required
    @property
    def time(self) -> str:
        """
        Default value: ``"2018-08-10T09:47:46.439Z"``
        """
        return self.__data.setdefault('time', "2018-08-10T09:47:46.439Z")


    @time.setter
    def time(self, value: str):
        """
        Default value: ``"2018-08-10T09:47:46.439Z"``
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


