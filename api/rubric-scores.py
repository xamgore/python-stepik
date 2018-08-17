# This file is generated
from common import required, readonly
from typing import List



class WriteRubricScore:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'WriteRubricScore(id={self.id!r})'


    @required
    @property
    def score(self) -> int:
        """
        Default value: 0
        """
        return self.__data['score']


    @score.setter
    def score(self, value: int):
        """
        Default value: 0
        """
        self.__data['score'] = value


    @property
    def text(self) -> str:
        return self.__data['text']


    @text.setter
    def text(self, value: str):
        self.__data['text'] = value




class RubricScore:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'RubricScore(id={self.id!r})'


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @required
    @readonly
    @property
    def review(self) -> str:
        return self.__data['review']


    @required
    @readonly
    @property
    def rubric(self) -> str:
        return self.__data['rubric']


    @required
    @property
    def score(self) -> int:
        """
        Default value: 0
        """
        return self.__data['score']


    @score.setter
    def score(self, value: int):
        """
        Default value: 0
        """
        self.__data['score'] = value


    @property
    def text(self) -> str:
        return self.__data['text']


    @text.setter
    def text(self, value: str):
        self.__data['text'] = value


