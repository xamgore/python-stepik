# This file is generated
from common import required, readonly
from typing import List


class WriteSearchReaction:
    def __init__(self, data):
        self.__data = data


    @required
    @property
    def result(self) -> str:
        return self.__data['result']


    @result.setter
    def result(self, value: str):
        self.__data['result'] = value


class SearchReaction:
    def __init__(self, data):
        self.__data = data


    @required
    @property
    def result(self) -> str:
        return self.__data['result']


    @result.setter
    def result(self, value: str):
        self.__data['result'] = value


