# This file is generated
from common import required, readonly
from typing import List


class WriteQuery:
    def __init__(self, data):
        self.__data = data


    @required
    @property
    def text(self) -> str:
        return self.__data['text']


    @text.setter
    def text(self, value: str):
        self.__data['text'] = value


class Query:
    def __init__(self, data):
        self.__data = data


    @required
    @property
    def text(self) -> str:
        return self.__data['text']


    @text.setter
    def text(self, value: str):
        self.__data['text'] = value


