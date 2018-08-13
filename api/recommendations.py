# This file is generated
from common import required, readonly
from typing import List


class WriteRecommendation:
    def __init__(self, data):
        self.__data = data


class Recommendation:
    def __init__(self, data):
        self.__data = data


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


