# This file is generated
from common import required, readonly
from typing import List


class WriteStripeCoupon:
    def __init__(self, data):
        self.__data = data


    @required
    @property
    def percent_off(self) -> int:
        return self.__data['percent_off']


    @percent_off.setter
    def percent_off(self, value: int):
        self.__data['percent_off'] = value


class StripeCoupon:
    def __init__(self, data):
        self.__data = data


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @required
    @property
    def percent_off(self) -> int:
        return self.__data['percent_off']


    @percent_off.setter
    def percent_off(self, value: int):
        self.__data['percent_off'] = value


