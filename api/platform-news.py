# This file is generated
from common import required, readonly
from typing import List


class WritePlatformNews:
    def __init__(self, data):
        self.__data = data


    @required
    @property
    def language(self) -> str:
        """
        default value: "en"
        """
        return self.__data.setdefault('language', "en")


    @language.setter
    def language(self, value: str):
        """
        default value: "en"
        """
        self.__data['language'] = value


    @required
    @property
    def text(self) -> str:
        return self.__data['text']


    @text.setter
    def text(self, value: str):
        self.__data['text'] = value


class PlatformNews:
    def __init__(self, data):
        self.__data = data


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @required
    @property
    def language(self) -> str:
        """
        default value: "en"
        """
        return self.__data.setdefault('language', "en")


    @language.setter
    def language(self, value: str):
        """
        default value: "en"
        """
        self.__data['language'] = value


    @readonly
    @property
    def create_date(self) -> str:
        """
        Type: datetime
        """
        return self.__data['create_date']


    @required
    @property
    def text(self) -> str:
        return self.__data['text']


    @text.setter
    def text(self, value: str):
        self.__data['text'] = value


