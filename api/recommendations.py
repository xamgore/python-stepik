# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class Recommendation:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'Recommendation(id={self.id!r})'


    @readonly
    @property
    def id(self) -> str:
        return self.__data['id']


    @readonly
    @property
    def lesson(self) -> str:
        return self.__data['lesson']


    @readonly
    @property
    def reasons(self) -> str:
        return self.__data['reasons']


