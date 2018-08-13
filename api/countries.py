# This file is generated
from common import required, readonly
from typing import List


class WriteCountry:
    def __init__(self, data):
        self.__data = data


    @required
    @property
    def name(self) -> str:
        return self.__data['name']


    @name.setter
    def name(self, value: str):
        self.__data['name'] = value


    @required
    @property
    def alt_names(self) -> str:
        """
        Type: array
        """
        return self.__data['alt_names']


    @alt_names.setter
    def alt_names(self, value: str):
        """
        Type: array
        """
        self.__data['alt_names'] = value


class Country:
    def __init__(self, data):
        self.__data = data


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @required
    @property
    def name(self) -> str:
        return self.__data['name']


    @name.setter
    def name(self, value: str):
        self.__data['name'] = value


    @required
    @property
    def alt_names(self) -> str:
        """
        Type: array
        """
        return self.__data['alt_names']


    @alt_names.setter
    def alt_names(self, value: str):
        """
        Type: array
        """
        self.__data['alt_names'] = value


class WriteAlternativeName:
    def __init__(self, data):
        self.__data = data


    @required
    @property
    def name(self) -> str:
        return self.__data['name']


    @name.setter
    def name(self, value: str):
        self.__data['name'] = value


    @required
    @property
    def language(self) -> str:
        return self.__data['language']


    @language.setter
    def language(self, value: str):
        self.__data['language'] = value


    @property
    def is_preferred(self) -> bool:
        """
        default value: False
        """
        return self.__data['is_preferred']


    @is_preferred.setter
    def is_preferred(self, value: bool):
        """
        default value: False
        """
        self.__data['is_preferred'] = value


class AlternativeName:
    def __init__(self, data):
        self.__data = data


    @required
    @property
    def name(self) -> str:
        return self.__data['name']


    @name.setter
    def name(self, value: str):
        self.__data['name'] = value


    @required
    @property
    def language(self) -> str:
        return self.__data['language']


    @language.setter
    def language(self, value: str):
        self.__data['language'] = value


    @property
    def is_preferred(self) -> bool:
        """
        default value: False
        """
        return self.__data['is_preferred']


    @is_preferred.setter
    def is_preferred(self, value: bool):
        """
        default value: False
        """
        self.__data['is_preferred'] = value


