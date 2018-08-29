# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class CourseRank:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'CourseRank(id={self.id!r})'


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @required
    @property
    def course(self) -> str:
        return self.__data['course']


    @course.setter
    def course(self, value: str):
        self.__data['course'] = value


    @required
    @property
    def user(self) -> str:
        return self.__data['user']


    @user.setter
    def user(self, value: str):
        self.__data['user'] = value


    @required
    @property
    def score(self) -> str:
        """
        Default value: ``"0"``

        Type: str
        """
        return self.__data.setdefault('score', "0")


    @score.setter
    def score(self, value: str):
        """
        Default value: ``"0"``

        Type: str
        """
        self.__data['score'] = value


    @property
    def rank(self) -> int:
        return self.__data['rank']


    @rank.setter
    def rank(self, value: int):
        self.__data['rank'] = value


    @property
    def rank_max(self) -> int:
        return self.__data['rank_max']


    @rank_max.setter
    def rank_max(self, value: int):
        self.__data['rank_max'] = value


    @readonly
    @property
    def position(self) -> str:
        return self.__data['position']


    @property
    def users_count(self) -> int:
        return self.__data['users_count']


    @users_count.setter
    def users_count(self, value: int):
        self.__data['users_count'] = value


