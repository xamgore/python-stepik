# This file is generated
from common import required, readonly
from typing import List


class WriteUserCodeRun:
    def __init__(self, data):
        self.__data = data


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


    @required
    @property
    def stdin(self) -> str:
        return self.__data['stdin']


    @stdin.setter
    def stdin(self, value: str):
        self.__data['stdin'] = value


class UserCodeRun:
    def __init__(self, data):
        self.__data = data


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
        Type: choice
        """
        return self.__data['status']


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
        default value: False
        """
        return self.__data['time_limit_exceeded']


    @readonly
    @property
    def memory_limit_exceeded(self) -> bool:
        """
        default value: False
        """
        return self.__data['memory_limit_exceeded']


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


