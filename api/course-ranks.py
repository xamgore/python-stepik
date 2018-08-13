# This file is generated
from common import required, readonly
from typing import List


class WriteCourseRank:
    def __init__(self, data):
        self.__data = data


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
        default value: "0"
        """
        return self.__data.setdefault('score', "0")


    @score.setter
    def score(self, value: str):
        """
        default value: "0"
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


    @property
    def users_count(self) -> int:
        return self.__data['users_count']


    @users_count.setter
    def users_count(self, value: int):
        self.__data['users_count'] = value


class CourseRank:
    def __init__(self, data):
        self.__data = data


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
        default value: "0"
        """
        return self.__data.setdefault('score', "0")


    @score.setter
    def score(self, value: str):
        """
        default value: "0"
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


