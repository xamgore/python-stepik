# This file is generated
from common import required, readonly
from typing import List


class WriteRubric:
    def __init__(self, data):
        self.__data = data


    @required
    @property
    def instruction(self) -> str:
        return self.__data['instruction']


    @instruction.setter
    def instruction(self, value: str):
        self.__data['instruction'] = value


    @required
    @property
    def text(self) -> str:
        return self.__data['text']


    @text.setter
    def text(self, value: str):
        self.__data['text'] = value


    @required
    @property
    def cost(self) -> int:
        return self.__data['cost']


    @cost.setter
    def cost(self, value: int):
        self.__data['cost'] = value


    @required
    @property
    def position(self) -> int:
        """
        default value: 1
        """
        return self.__data.setdefault('position', 1)


    @position.setter
    def position(self, value: int):
        """
        default value: 1
        """
        self.__data['position'] = value


class Rubric:
    def __init__(self, data):
        self.__data = data


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @required
    @property
    def instruction(self) -> str:
        return self.__data['instruction']


    @instruction.setter
    def instruction(self, value: str):
        self.__data['instruction'] = value


    @required
    @property
    def text(self) -> str:
        return self.__data['text']


    @text.setter
    def text(self, value: str):
        self.__data['text'] = value


    @required
    @property
    def cost(self) -> int:
        return self.__data['cost']


    @cost.setter
    def cost(self, value: int):
        self.__data['cost'] = value


    @required
    @property
    def position(self) -> int:
        """
        default value: 1
        """
        return self.__data.setdefault('position', 1)


    @position.setter
    def position(self, value: int):
        """
        default value: 1
        """
        self.__data['position'] = value


