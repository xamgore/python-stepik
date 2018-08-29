# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class Class:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'Class(id={self.id!r})'


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
    @readonly
    @property
    def owner(self) -> str:
        return self.__data['owner']


    @property
    def title(self) -> str:
        return self.__data['title']


    @title.setter
    def title(self, value: str):
        self.__data['title'] = value


    @property
    def description(self) -> str:
        return self.__data['description']


    @description.setter
    def description(self, value: str):
        self.__data['description'] = value


    @required
    @readonly
    @property
    def invitation_key(self) -> str:
        return self.__data['invitation_key']


    @readonly
    @property
    def is_access_restricted(self) -> str:
        return self.__data['is_access_restricted']


    @readonly
    @property
    def actions(self) -> str:
        return self.__data['actions']


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


