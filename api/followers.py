# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class Follower:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'Follower(id={self.id!r})'


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @required
    @property
    def followee(self) -> str:
        return self.__data['followee']


    @followee.setter
    def followee(self, value: str):
        self.__data['followee'] = value


    @required
    @readonly
    @property
    def user(self) -> str:
        return self.__data['user']


    @required
    @readonly
    @property
    def date_joined(self) -> str:
        """
        Default value: ``"2018-08-26T00:35:20.667Z"``

        Type: str
        """
        return self.__data.setdefault('date_joined', "2018-08-26T00:35:20.667Z")


