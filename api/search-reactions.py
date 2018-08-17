# This file is generated
from common import required, readonly
from typing import List



class WriteSearchReaction:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'WriteSearchReaction(id={self.id!r})'


    @required
    @property
    def result(self) -> str:
        return self.__data['result']


    @result.setter
    def result(self, value: str):
        self.__data['result'] = value




class SearchReaction:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'SearchReaction(id={self.id!r})'


    @required
    @property
    def result(self) -> str:
        return self.__data['result']


    @result.setter
    def result(self, value: str):
        self.__data['result'] = value


