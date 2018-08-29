# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class StripePlan:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'StripePlan(id={self.id!r})'


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @required
    @property
    def code(self) -> str:
        return self.__data['code']


    @code.setter
    def code(self, value: str):
        self.__data['code'] = value


    @required
    @property
    def currency(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('currency', "None")


    @currency.setter
    def currency(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self.__data['currency'] = value


