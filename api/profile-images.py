# This file is generated
from common import required, readonly
from typing import List


class WriteProfileImage:
    def __init__(self, data):
        self.__data = data


    @property
    def avatar(self) -> str:
        """
        Type: image upload
        """
        return self.__data['avatar']


    @avatar.setter
    def avatar(self, value: str):
        """
        Type: image upload
        """
        self.__data['avatar'] = value


class ProfileImage:
    def __init__(self, data):
        self.__data = data


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @property
    def avatar(self) -> str:
        """
        Type: image upload
        """
        return self.__data['avatar']


    @avatar.setter
    def avatar(self, value: str):
        """
        Type: image upload
        """
        self.__data['avatar'] = value


