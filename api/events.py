# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



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
        Default value: ``"2018-08-26T00:35:18.956Z"``

        Type: str
        """
        return self.__data.setdefault('time', "2018-08-26T00:35:18.956Z")


    @time.setter
    def time(self, value: str):
        """
        Default value: ``"2018-08-26T00:35:18.956Z"``

        Type: str
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
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('action', "None")


    @readonly
    @property
    def html_text(self) -> str:
        return self.__data['html_text']


