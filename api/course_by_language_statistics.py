# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class CourseByLanguageStatistics:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'CourseByLanguageStatistics(id={self.id!r})'


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
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('language', "None")


    @language.setter
    def language(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self.__data['language'] = value


    @required
    @property
    def learners_count(self) -> int:
        """
        Default value: ``0``
        """
        return self.__data['learners_count']


    @learners_count.setter
    def learners_count(self, value: int):
        """
        Default value: ``0``
        """
        self.__data['learners_count'] = value


