# This file is generated
from common import required, readonly
from typing import List



class WriteProfileImage:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'WriteProfileImage(id={self.id!r})'


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
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'ProfileImage(id={self.id!r})'


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


