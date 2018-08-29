# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class ExamSession:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'ExamSession(id={self.id!r})'


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
        Default value: ``"2018-08-26T00:35:19.469Z"``

        Type: str
        """
        return self.__data.setdefault('begin_date', "2018-08-26T00:35:19.469Z")


