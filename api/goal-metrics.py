# This file is generated
from common import required, readonly
from typing import List



class WriteGoalMetric:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'WriteGoalMetric(id={self.id!r})'


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
        Default value: "0"
        """
        return self.__data.setdefault('value', "0")


    @value.setter
    def value(self, value: str):
        """
        Default value: "0"
        """
        self.__data['value'] = value




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
        Default value: "0"
        """
        return self.__data.setdefault('value', "0")


    @value.setter
    def value(self, value: str):
        """
        Default value: "0"
        """
        self.__data['value'] = value


