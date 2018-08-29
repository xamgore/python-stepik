# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class CourseReminder:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'CourseReminder(id={self.id!r})'


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @required
    @readonly
    @property
    def user(self) -> str:
        return self.__data['user']


    @required
    @property
    def course(self) -> str:
        return self.__data['course']


    @course.setter
    def course(self, value: str):
        self.__data['course'] = value


    @readonly
    @property
    def create_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('create_date', "None")


    @property
    def is_active(self) -> bool:
        """
        Default value: ``True``
        """
        return self.__data.setdefault('is_active', True)


    @is_active.setter
    def is_active(self, value: bool):
        """
        Default value: ``True``
        """
        self.__data['is_active'] = value


    @readonly
    @property
    def payload(self) -> str:
        return self.__data['payload']


