# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class CourseList:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'CourseList(id={self.id!r})'


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @required
    @property
    def position(self) -> int:
        """
        Default value: ``1``
        """
        return self.__data.setdefault('position', 1)


    @position.setter
    def position(self, value: int):
        """
        Default value: ``1``
        """
        self.__data['position'] = value


    @required
    @property
    def title(self) -> str:
        return self.__data['title']


    @title.setter
    def title(self, value: str):
        self.__data['title'] = value


    @required
    @property
    def language(self) -> str:
        """
        Default value: ``"en"``

        Type: str
        """
        return self.__data.setdefault('language', "en")


    @language.setter
    def language(self, value: str):
        """
        Default value: ``"en"``

        Type: str
        """
        self.__data['language'] = value


    @property
    def courses(self) -> str:
        return self.__data['courses']


    @courses.setter
    def courses(self, value: str):
        self.__data['courses'] = value


    @property
    def description(self) -> str:
        return self.__data['description']


    @description.setter
    def description(self, value: str):
        self.__data['description'] = value


