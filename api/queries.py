# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class Query:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'Query(id={self.id!r})'


    @required
    @property
    def text(self) -> str:
        return self.__data['text']


    @text.setter
    def text(self, value: str):
        self.__data['text'] = value


