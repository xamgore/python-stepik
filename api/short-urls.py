# This file is generated
from common import required, readonly
from typing import List


class WriteShortUrl:
    def __init__(self, data):
        self.__data = data


    @required
    @property
    def url(self) -> str:
        return self.__data['url']


    @url.setter
    def url(self, value: str):
        self.__data['url'] = value


class ShortUrl:
    def __init__(self, data):
        self.__data = data


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @readonly
    @property
    def key(self) -> str:
        return self.__data['key']


    @required
    @property
    def url(self) -> str:
        return self.__data['url']


    @url.setter
    def url(self, value: str):
        self.__data['url'] = value


    @readonly
    @property
    def short_url(self) -> str:
        return self.__data['short_url']


