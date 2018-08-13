# This file is generated
from common import required, readonly
from typing import List


class WriteSocialAccount:
    def __init__(self, data):
        self.__data = data


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


    @property
    def first_name(self) -> str:
        return self.__data['first_name']


    @first_name.setter
    def first_name(self, value: str):
        self.__data['first_name'] = value


    @property
    def last_name(self) -> str:
        return self.__data['last_name']


    @last_name.setter
    def last_name(self, value: str):
        self.__data['last_name'] = value


    @property
    def email(self) -> str:
        """
        Type: email
        """
        return self.__data['email']


    @email.setter
    def email(self, value: str):
        """
        Type: email
        """
        self.__data['email'] = value


    @property
    def language(self) -> str:
        """
        Type: choice
        """
        return self.__data['language']


    @language.setter
    def language(self, value: str):
        """
        Type: choice
        """
        self.__data['language'] = value


class SocialAccount:
    def __init__(self, data):
        self.__data = data


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


