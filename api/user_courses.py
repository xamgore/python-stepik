# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class UserCourse:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'UserCourse(id={self.id!r})'


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
        Default value: ``False``
        """
        return self.__data['is_favorite']


    @is_favorite.setter
    def is_favorite(self, value: bool):
        """
        Default value: ``False``
        """
        self.__data['is_favorite'] = value


    @required
    @readonly
    @property
    def last_viewed(self) -> str:
        """
        Default value: ``"2018-08-26T00:35:53.561Z"``

        Type: str
        """
        return self.__data.setdefault('last_viewed', "2018-08-26T00:35:53.561Z")


