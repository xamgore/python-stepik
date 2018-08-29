# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class UserCodeRun:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'UserCodeRun(id={self.id!r})'


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @required
    @property
    def user(self) -> str:
        return self.__data['user']


    @user.setter
    def user(self, value: str):
        self.__data['user'] = value


    @required
    @property
    def step(self) -> str:
        return self.__data['step']


    @step.setter
    def step(self, value: str):
        self.__data['step'] = value


    @required
    @property
    def language(self) -> str:
        return self.__data['language']


    @language.setter
    def language(self, value: str):
        self.__data['language'] = value


    @required
    @property
    def code(self) -> str:
        return self.__data['code']


    @code.setter
    def code(self, value: str):
        self.__data['code'] = value


    @readonly
    @property
    def status(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('status', "None")


    @required
    @property
    def stdin(self) -> str:
        return self.__data['stdin']


    @stdin.setter
    def stdin(self, value: str):
        self.__data['stdin'] = value


    @required
    @readonly
    @property
    def stdout(self) -> str:
        return self.__data['stdout']


    @required
    @readonly
    @property
    def stderr(self) -> str:
        return self.__data['stderr']


    @readonly
    @property
    def time_limit_exceeded(self) -> bool:
        """
        Default value: ``False``
        """
        return self.__data['time_limit_exceeded']


    @readonly
    @property
    def memory_limit_exceeded(self) -> bool:
        """
        Default value: ``False``
        """
        return self.__data['memory_limit_exceeded']


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


