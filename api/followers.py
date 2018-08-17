# This file is generated
from common import required, readonly
from typing import List



class WriteFollower:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'WriteFollower(id={self.id!r})'


    @required
    @property
    def followee(self) -> str:
        return self.__data['followee']


    @followee.setter
    def followee(self, value: str):
        self.__data['followee'] = value




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
        Default value: "2018-08-10T09:47:52.623Z"
        """
        return self.__data.setdefault('date_joined', "2018-08-10T09:47:52.623Z")


