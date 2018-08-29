# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class Subscription:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'Subscription(id={self.id!r})'


    @readonly
    @property
    def id(self) -> str:
        return self.__data['id']


    @readonly
    @property
    def action(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('action', "None")


    @property
    def is_active(self) -> str:
        return self.__data['is_active']


    @is_active.setter
    def is_active(self, value: str):
        self.__data['is_active'] = value


