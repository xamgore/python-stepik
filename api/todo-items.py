# This file is generated
from common import required, readonly
from typing import List



class WriteTodoItem:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'WriteTodoItem(id={self.id!r})'


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
        Type: choice
        """
        return self.__data['kind']


    @kind.setter
    def kind(self, value: str):
        """
        Type: choice
        """
        self.__data['kind'] = value


    @property
    def is_complete(self) -> bool:
        """
        Default value: False
        """
        return self.__data['is_complete']


    @is_complete.setter
    def is_complete(self, value: bool):
        """
        Default value: False
        """
        self.__data['is_complete'] = value


    @property
    def context(self) -> List:
        """
        Default value: {}
        """
        return self.__data['context']


    @context.setter
    def context(self, value: List):
        """
        Default value: {}
        """
        self.__data['context'] = value




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
        Type: choice
        """
        return self.__data['kind']


    @kind.setter
    def kind(self, value: str):
        """
        Type: choice
        """
        self.__data['kind'] = value


    @property
    def is_complete(self) -> bool:
        """
        Default value: False
        """
        return self.__data['is_complete']


    @is_complete.setter
    def is_complete(self, value: bool):
        """
        Default value: False
        """
        self.__data['is_complete'] = value


    @property
    def context(self) -> List:
        """
        Default value: {}
        """
        return self.__data['context']


    @context.setter
    def context(self, value: List):
        """
        Default value: {}
        """
        self.__data['context'] = value


    @readonly
    @property
    def create_date(self) -> str:
        """
        Type: datetime
        """
        return self.__data['create_date']


    @readonly
    @property
    def update_date(self) -> str:
        """
        Type: datetime
        """
        return self.__data['update_date']


