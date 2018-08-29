# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class TodoItem:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'TodoItem(id={self.id!r})'


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
    def kind(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('kind', "None")


    @kind.setter
    def kind(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self.__data['kind'] = value


    @property
    def is_complete(self) -> bool:
        """
        Default value: ``False``
        """
        return self.__data['is_complete']


    @is_complete.setter
    def is_complete(self, value: bool):
        """
        Default value: ``False``
        """
        self.__data['is_complete'] = value


    @property
    def context(self) -> str:
        """
        Enter a valid JSON object

        Default value: ``{}``
        """
        return self.__data['context']


    @context.setter
    def context(self, value: str):
        """
        Enter a valid JSON object

        Default value: ``{}``
        """
        self.__data['context'] = value


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


