# This file is generated
from common import required, readonly
from typing import List


class WriteGroup:
    def __init__(self, data):
        self.__data = data


class Group:
    def __init__(self, data):
        self.__data = data


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @readonly
    @property
    def users(self) -> str:
        return self.__data['users']


