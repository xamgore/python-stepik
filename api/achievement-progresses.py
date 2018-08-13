# This file is generated
from common import required, readonly
from typing import List


class WriteAchievementProgress:
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
    def achievement(self) -> str:
        return self.__data['achievement']


    @achievement.setter
    def achievement(self, value: str):
        self.__data['achievement'] = value


    @required
    @property
    def score(self) -> int:
        return self.__data['score']


    @score.setter
    def score(self, value: int):
        self.__data['score'] = value


    @property
    def obtain_date(self) -> str:
        """
        Type: datetime
        """
        return self.__data['obtain_date']


    @obtain_date.setter
    def obtain_date(self, value: str):
        """
        Type: datetime
        """
        self.__data['obtain_date'] = value


class AchievementProgress:
    def __init__(self, data):
        self.__data = data


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @required
    @property
    def user(self) -> str:
        return self.__data['user']


    @user.setter
    def user(self, value: str):
        self.__data['user'] = value


    @required
    @property
    def achievement(self) -> str:
        return self.__data['achievement']


    @achievement.setter
    def achievement(self, value: str):
        self.__data['achievement'] = value


    @required
    @property
    def score(self) -> int:
        return self.__data['score']


    @score.setter
    def score(self, value: int):
        self.__data['score'] = value


    @readonly
    @property
    def kind(self) -> str:
        return self.__data['kind']


    @readonly
    @property
    def create_date(self) -> str:
        """
        Type: datetime
        """
        return self.__data['create_date']


    @readonly
    @property
    def update_date(self) -> str:
        """
        Type: datetime
        """
        return self.__data['update_date']


    @property
    def obtain_date(self) -> str:
        """
        Type: datetime
        """
        return self.__data['obtain_date']


    @obtain_date.setter
    def obtain_date(self, value: str):
        """
        Type: datetime
        """
        self.__data['obtain_date'] = value


