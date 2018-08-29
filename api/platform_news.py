# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class PlatformNews:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'PlatformNews(id={self.id!r})'


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @required
    @property
    def language(self) -> str:
        """
        Default value: ``"en"``

        Type: str
        """
        return self.__data.setdefault('language', "en")


    @language.setter
    def language(self, value: str):
        """
        Default value: ``"en"``

        Type: str
        """
        self.__data['language'] = value


    @readonly
    @property
    def create_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('create_date', "None")


    @required
    @property
    def text(self) -> str:
        return self.__data['text']


    @text.setter
    def text(self, value: str):
        self.__data['text'] = value


