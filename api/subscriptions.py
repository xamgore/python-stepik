# This file is generated
from common import required, readonly
from typing import List



class WriteSubscription:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'WriteSubscription(id={self.id!r})'


    @property
    def is_active(self) -> str:
        return self.__data['is_active']


    @is_active.setter
    def is_active(self, value: str):
        self.__data['is_active'] = value




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
        Type: choice
        """
        return self.__data['action']


    @property
    def is_active(self) -> str:
        return self.__data['is_active']


    @is_active.setter
    def is_active(self, value: str):
        self.__data['is_active'] = value


