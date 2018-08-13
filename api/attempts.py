# This file is generated
from common import required, readonly
from typing import List


class WriteAttempt:
    def __init__(self, data):
        self.__data = data


    @required
    @property
    def step(self) -> str:
        return self.__data['step']


    @step.setter
    def step(self, value: str):
        self.__data['step'] = value


class Attempt:
    def __init__(self, data):
        self.__data = data


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @readonly
    @property
    def dataset(self) -> str:
        return self.__data['dataset']


    @readonly
    @property
    def dataset_url(self) -> str:
        return self.__data['dataset_url']


    @readonly
    @property
    def time(self) -> str:
        """
        Type: datetime
        """
        return self.__data['time']


    @readonly
    @property
    def status(self) -> str:
        """
        Type: choice
        """
        return self.__data['status']


    @readonly
    @property
    def time_left(self) -> int:
        return self.__data['time_left']


    @required
    @property
    def step(self) -> str:
        return self.__data['step']


    @step.setter
    def step(self, value: str):
        self.__data['step'] = value


    @readonly
    @property
    def user(self) -> str:
        return self.__data['user']


