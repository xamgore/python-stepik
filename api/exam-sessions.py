# This file is generated
from common import required, readonly
from typing import List


class WriteExamSession:
    def __init__(self, data):
        self.__data = data


    @required
    @property
    def section(self) -> str:
        return self.__data['section']


    @section.setter
    def section(self, value: str):
        self.__data['section'] = value


class ExamSession:
    def __init__(self, data):
        self.__data = data


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
    def section(self) -> str:
        return self.__data['section']


    @section.setter
    def section(self, value: str):
        self.__data['section'] = value


    @required
    @readonly
    @property
    def begin_date(self) -> str:
        """
        default value: "2018-08-10T09:47:47.303Z"
        """
        return self.__data.setdefault('begin_date', "2018-08-10T09:47:47.303Z")


