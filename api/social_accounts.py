# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class SocialAccount:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'SocialAccount(id={self.id!r})'


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @property
    def user(self) -> str:
        return self.__data['user']


    @user.setter
    def user(self, value: str):
        self.__data['user'] = value


    @required
    @property
    def provider(self) -> str:
        return self.__data['provider']


    @provider.setter
    def provider(self, value: str):
        self.__data['provider'] = value


    @required
    @property
    def uid(self) -> str:
        return self.__data['uid']


    @uid.setter
    def uid(self, value: str):
        self.__data['uid'] = value


