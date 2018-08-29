# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class UserLicense:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'UserLicense(id={self.id!r})'


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @readonly
    @property
    def activation_code(self) -> str:
        return self.__data['activation_code']


    @readonly
    @property
    def expire_date(self) -> str:
        return self.__data['expire_date']


    @readonly
    @property
    def is_personal(self) -> str:
        return self.__data['is_personal']


    @required
    @readonly
    @property
    def user(self) -> str:
        return self.__data['user']


