# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class SocialProfile:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'SocialProfile(id={self.id!r})'


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
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('provider', "None")


    @provider.setter
    def provider(self, value: str):
        """
        Default value: ``"None"``

        Type: str
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


