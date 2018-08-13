# This file is generated
from common import required, readonly
from typing import List


class WriteUserLicense:
    def __init__(self, data):
        self.__data = data


class UserLicense:
    def __init__(self, data):
        self.__data = data


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @readonly
    @property
    def activation_code(self) -> str:
        return self.__data['activation_code']


    @readonly
    @property
    def expire_date(self) -> str:
        return self.__data['expire_date']


    @readonly
    @property
    def is_personal(self) -> str:
        return self.__data['is_personal']


    @required
    @readonly
    @property
    def user(self) -> str:
        return self.__data['user']


