# This file is generated
from common import required, readonly
from typing import List


class WriteInstruction:
    def __init__(self, data):
        self.__data = data


    @required
    @property
    def step(self) -> str:
        return self.__data['step']


    @step.setter
    def step(self, value: str):
        self.__data['step'] = value


    @required
    @property
    def min_reviews(self) -> int:
        """
        default value: 3
        """
        return self.__data.setdefault('min_reviews', 3)


    @min_reviews.setter
    def min_reviews(self, value: int):
        """
        default value: 3
        """
        self.__data['min_reviews'] = value


    @property
    def strategy_type(self) -> str:
        """
        Type: choice
        """
        return self.__data['strategy_type']


    @strategy_type.setter
    def strategy_type(self, value: str):
        """
        Type: choice
        """
        self.__data['strategy_type'] = value


    @required
    @property
    def rubrics(self) -> str:
        return self.__data['rubrics']


    @rubrics.setter
    def rubrics(self, value: str):
        self.__data['rubrics'] = value


    @property
    def text(self) -> str:
        return self.__data['text']


    @text.setter
    def text(self, value: str):
        self.__data['text'] = value


class Instruction:
    def __init__(self, data):
        self.__data = data


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @required
    @property
    def step(self) -> str:
        return self.__data['step']


    @step.setter
    def step(self, value: str):
        self.__data['step'] = value


    @required
    @property
    def min_reviews(self) -> int:
        """
        default value: 3
        """
        return self.__data.setdefault('min_reviews', 3)


    @min_reviews.setter
    def min_reviews(self, value: int):
        """
        default value: 3
        """
        self.__data['min_reviews'] = value


    @property
    def strategy_type(self) -> str:
        """
        Type: choice
        """
        return self.__data['strategy_type']


    @strategy_type.setter
    def strategy_type(self, value: str):
        """
        Type: choice
        """
        self.__data['strategy_type'] = value


    @required
    @property
    def rubrics(self) -> str:
        return self.__data['rubrics']


    @rubrics.setter
    def rubrics(self, value: str):
        self.__data['rubrics'] = value


    @readonly
    @property
    def is_frozen(self) -> bool:
        return self.__data['is_frozen']


    @property
    def text(self) -> str:
        return self.__data['text']


    @text.setter
    def text(self, value: str):
        self.__data['text'] = value


