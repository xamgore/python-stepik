# This file is generated
from common import required, readonly
from typing import List


class WriteGoalMetric:
    def __init__(self, data):
        self.__data = data


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
        default value: "0"
        """
        return self.__data.setdefault('value', "0")


    @value.setter
    def value(self, value: str):
        """
        default value: "0"
        """
        self.__data['value'] = value


class GoalMetric:
    def __init__(self, data):
        self.__data = data


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
        default value: "0"
        """
        return self.__data.setdefault('value', "0")


    @value.setter
    def value(self, value: str):
        """
        default value: "0"
        """
        self.__data['value'] = value


