# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class ScoreFile:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'ScoreFile(id={self.id!r})'


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @required
    @property
    def session(self) -> str:
        return self.__data['session']


    @session.setter
    def session(self, value: str):
        self.__data['session'] = value


    @required
    @property
    def file(self) -> str:
        return self.__data['file']


    @file.setter
    def file(self, value: str):
        self.__data['file'] = value


    @readonly
    @property
    def error(self) -> str:
        return self.__data['error']


    @readonly
    @property
    def create_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('create_date', "None")


    @readonly
    @property
    def process_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('process_date', "None")


