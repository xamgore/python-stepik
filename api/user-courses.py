# This file is generated
from common import required, readonly
from typing import List


class WriteUserCourse:
    def __init__(self, data):
        self.__data = data


    @property
    def is_favorite(self) -> bool:
        """
        default value: False
        """
        return self.__data['is_favorite']


    @is_favorite.setter
    def is_favorite(self, value: bool):
        """
        default value: False
        """
        self.__data['is_favorite'] = value


class UserCourse:
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
    @readonly
    @property
    def course(self) -> str:
        return self.__data['course']


    @property
    def is_favorite(self) -> bool:
        """
        default value: False
        """
        return self.__data['is_favorite']


    @is_favorite.setter
    def is_favorite(self, value: bool):
        """
        default value: False
        """
        self.__data['is_favorite'] = value


    @required
    @readonly
    @property
    def last_viewed(self) -> str:
        """
        default value: "2018-08-10T09:48:51.981Z"
        """
        return self.__data.setdefault('last_viewed', "2018-08-10T09:48:51.981Z")


