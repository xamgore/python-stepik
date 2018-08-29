# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class Attempt:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'Attempt(id={self.id!r})'


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
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('time', "None")


    @readonly
    @property
    def status(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('status', "None")


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


