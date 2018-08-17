# This file is generated
from common import required, readonly
from typing import List



class WriteLongTask:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'WriteLongTask(id={self.id!r})'


    @required
    @property
    def type(self) -> str:
        """
        Type: choice
        """
        return self.__data['type']


    @type.setter
    def type(self, value: str):
        """
        Type: choice
        """
        self.__data['type'] = value


    @property
    def course(self) -> str:
        return self.__data['course']


    @course.setter
    def course(self, value: str):
        self.__data['course'] = value


    @property
    def lesson(self) -> str:
        return self.__data['lesson']


    @lesson.setter
    def lesson(self, value: str):
        self.__data['lesson'] = value


    @property
    def step(self) -> str:
        return self.__data['step']


    @step.setter
    def step(self, value: str):
        self.__data['step'] = value


    @property
    def klass(self) -> str:
        return self.__data['klass']


    @klass.setter
    def klass(self, value: str):
        self.__data['klass'] = value




class LongTask:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'LongTask(id={self.id!r})'


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @readonly
    @property
    def queue_date(self) -> str:
        """
        Type: datetime
        """
        return self.__data['queue_date']


    @readonly
    @property
    def start_date(self) -> str:
        """
        Type: datetime
        """
        return self.__data['start_date']


    @readonly
    @property
    def finish_date(self) -> str:
        """
        Type: datetime
        """
        return self.__data['finish_date']


    @required
    @readonly
    @property
    def user(self) -> str:
        return self.__data['user']


    @required
    @property
    def type(self) -> str:
        """
        Type: choice
        """
        return self.__data['type']


    @type.setter
    def type(self, value: str):
        """
        Type: choice
        """
        self.__data['type'] = value


    @readonly
    @property
    def status(self) -> str:
        return self.__data['status']


    @readonly
    @property
    def result(self) -> List:
        """
        Default value: {}
        """
        return self.__data['result']


    @property
    def course(self) -> str:
        return self.__data['course']


    @course.setter
    def course(self, value: str):
        self.__data['course'] = value


    @property
    def lesson(self) -> str:
        return self.__data['lesson']


    @lesson.setter
    def lesson(self, value: str):
        self.__data['lesson'] = value


    @property
    def step(self) -> str:
        return self.__data['step']


    @step.setter
    def step(self, value: str):
        self.__data['step'] = value


    @property
    def klass(self) -> str:
        return self.__data['klass']


    @klass.setter
    def klass(self, value: str):
        self.__data['klass'] = value


