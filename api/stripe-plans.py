# This file is generated
from common import required, readonly
from typing import List


class WriteStripePlan:
    def __init__(self, data):
        self.__data = data


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
        Type: choice
        """
        return self.__data['currency']


    @currency.setter
    def currency(self, value: str):
        """
        Type: choice
        """
        self.__data['currency'] = value


class StripePlan:
    def __init__(self, data):
        self.__data = data


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
        Type: choice
        """
        return self.__data['currency']


    @currency.setter
    def currency(self, value: str):
        """
        Type: choice
        """
        self.__data['currency'] = value


