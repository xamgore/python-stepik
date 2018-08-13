# This file is generated
from common import required, readonly
from typing import List


class WriteRecommendationReaction:
    def __init__(self, data):
        self.__data = data


    @required
    @property
    def user(self) -> str:
        return self.__data['user']


    @user.setter
    def user(self, value: str):
        self.__data['user'] = value


    @required
    @property
    def lesson(self) -> str:
        return self.__data['lesson']


    @lesson.setter
    def lesson(self, value: str):
        self.__data['lesson'] = value


    @required
    @property
    def reaction(self) -> str:
        """
        Type: choice
        """
        return self.__data['reaction']


    @reaction.setter
    def reaction(self, value: str):
        """
        Type: choice
        """
        self.__data['reaction'] = value


    @required
    @property
    def time(self) -> str:
        """
        default value: "2018-08-10T09:48:13.586Z"
        """
        return self.__data.setdefault('time', "2018-08-10T09:48:13.586Z")


    @time.setter
    def time(self, value: str):
        """
        default value: "2018-08-10T09:48:13.586Z"
        """
        self.__data['time'] = value


class RecommendationReaction:
    def __init__(self, data):
        self.__data = data


    @required
    @property
    def user(self) -> str:
        return self.__data['user']


    @user.setter
    def user(self, value: str):
        self.__data['user'] = value


    @required
    @property
    def lesson(self) -> str:
        return self.__data['lesson']


    @lesson.setter
    def lesson(self, value: str):
        self.__data['lesson'] = value


    @required
    @property
    def reaction(self) -> str:
        """
        Type: choice
        """
        return self.__data['reaction']


    @reaction.setter
    def reaction(self, value: str):
        """
        Type: choice
        """
        self.__data['reaction'] = value


    @required
    @property
    def time(self) -> str:
        """
        default value: "2018-08-10T09:48:13.586Z"
        """
        return self.__data.setdefault('time', "2018-08-10T09:48:13.586Z")


    @time.setter
    def time(self, value: str):
        """
        default value: "2018-08-10T09:48:13.586Z"
        """
        self.__data['time'] = value


