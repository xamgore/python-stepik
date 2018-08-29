# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class Specialization:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'Specialization(id={self.id!r})'


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @required
    @property
    def title(self) -> str:
        return self.__data['title']


    @title.setter
    def title(self, value: str):
        self.__data['title'] = value


    @required
    @property
    def details_url(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('details_url', "None")


    @details_url.setter
    def details_url(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self.__data['details_url'] = value


    @property
    def courses(self) -> str:
        return self.__data['courses']


    @courses.setter
    def courses(self, value: str):
        self.__data['courses'] = value


