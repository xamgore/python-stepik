# This file is generated
from common import required, readonly
from typing import List


class WriteCourseByLanguageStatistics:
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
    def language(self) -> str:
        """
        Type: choice
        """
        return self.__data['language']


    @language.setter
    def language(self, value: str):
        """
        Type: choice
        """
        self.__data['language'] = value


    @required
    @property
    def learners_count(self) -> int:
        """
        default value: 0
        """
        return self.__data['learners_count']


    @learners_count.setter
    def learners_count(self, value: int):
        """
        default value: 0
        """
        self.__data['learners_count'] = value


class CourseByLanguageStatistics:
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
    def language(self) -> str:
        """
        Type: choice
        """
        return self.__data['language']


    @language.setter
    def language(self, value: str):
        """
        Type: choice
        """
        self.__data['language'] = value


    @required
    @property
    def learners_count(self) -> int:
        """
        default value: 0
        """
        return self.__data['learners_count']


    @learners_count.setter
    def learners_count(self, value: int):
        """
        default value: 0
        """
        self.__data['learners_count'] = value


