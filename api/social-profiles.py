# This file is generated
from common import required, readonly
from typing import List


class WriteSocialProfile:
    def __init__(self, data):
        self.__data = data


    @required
    @property
    def provider(self) -> str:
        """
        Type: choice
        """
        return self.__data['provider']


    @provider.setter
    def provider(self, value: str):
        """
        Type: choice
        """
        self.__data['provider'] = value


    @required
    @property
    def name(self) -> str:
        return self.__data['name']


    @name.setter
    def name(self, value: str):
        self.__data['name'] = value


class SocialProfile:
    def __init__(self, data):
        self.__data = data


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @required
    @readonly
    @property
    def user(self) -> str:
        return self.__data['user']


    @required
    @property
    def provider(self) -> str:
        """
        Type: choice
        """
        return self.__data['provider']


    @provider.setter
    def provider(self, value: str):
        """
        Type: choice
        """
        self.__data['provider'] = value


    @required
    @property
    def name(self) -> str:
        return self.__data['name']


    @name.setter
    def name(self, value: str):
        self.__data['name'] = value


    @readonly
    @property
    def url(self) -> str:
        return self.__data['url']


