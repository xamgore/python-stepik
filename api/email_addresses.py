# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class EmailAddress:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'EmailAddress(id={self.id!r})'


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
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('email', "None")


    @email.setter
    def email(self, value: str):
        """
        Default value: ``"None"``

        Type: str
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


