# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class AchievementProgress:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'AchievementProgress(id={self.id!r})'


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
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('create_date', "None")


    @readonly
    @property
    def update_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('update_date', "None")


    @property
    def obtain_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('obtain_date', "None")


    @obtain_date.setter
    def obtain_date(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self.__data['obtain_date'] = value


