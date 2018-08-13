# This file is generated
from common import required, readonly
from typing import List


class WriteEmailAddress:
    def __init__(self, data):
        self.__data = data


    @required
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


class EmailAddress:
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


    @readonly
    @property
    def is_verified(self) -> bool:
        return self.__data['is_verified']


    @readonly
    @property
    def is_primary(self) -> bool:
        return self.__data['is_primary']


