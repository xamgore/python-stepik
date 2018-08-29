# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class GoalMetric:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'GoalMetric(id={self.id!r})'


    @required
    @property
    def goal_name(self) -> str:
        return self.__data['goal_name']


    @goal_name.setter
    def goal_name(self, value: str):
        self.__data['goal_name'] = value


    @required
    @property
    def value(self) -> str:
        """
        Default value: ``"0"``

        Type: str
        """
        return self.__data.setdefault('value', "0")


    @value.setter
    def value(self, value: str):
        """
        Default value: ``"0"``

        Type: str
        """
        self.__data['value'] = value

