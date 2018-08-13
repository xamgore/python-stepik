# This file is generated
from common import required, readonly
from typing import List


class WriteScoreFile:
    def __init__(self, data):
        self.__data = data


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


class ScoreFile:
    def __init__(self, data):
        self.__data = data


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
        Type: datetime
        """
        return self.__data['create_date']


    @readonly
    @property
    def process_date(self) -> str:
        """
        Type: datetime
        """
        return self.__data['process_date']


