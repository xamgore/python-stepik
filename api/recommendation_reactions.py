# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class RecommendationReaction:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'RecommendationReaction(id={self.id!r})'


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
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('reaction', "None")


    @reaction.setter
    def reaction(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self.__data['reaction'] = value


    @required
    @property
    def time(self) -> str:
        """
        Default value: ``"2018-08-26T00:35:32.023Z"``

        Type: str
        """
        return self.__data.setdefault('time', "2018-08-26T00:35:32.023Z")


    @time.setter
    def time(self, value: str):
        """
        Default value: ``"2018-08-26T00:35:32.023Z"``

        Type: str
        """
        self.__data['time'] = value


