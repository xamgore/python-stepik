# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



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
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('avatar', "None")


    @avatar.setter
    def avatar(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self.__data['avatar'] = value


