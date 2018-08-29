# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class ShortUrl:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'ShortUrl(id={self.id!r})'


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


