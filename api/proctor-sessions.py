# This file is generated
from common import required, readonly
from typing import List



class WriteProctorSession:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'WriteProctorSession(id={self.id!r})'


    @required
    @property
    def section(self) -> str:
        return self.__data['section']


    @section.setter
    def section(self, value: str):
        self.__data['section'] = value




class ProctorSession:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'ProctorSession(id={self.id!r})'


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
    def create_date(self) -> str:
        """
        Default value: "2018-08-10T09:48:08.790Z"
        """
        return self.__data.setdefault('create_date', "2018-08-10T09:48:08.790Z")


    @readonly
    @property
    def start_date(self) -> str:
        """
        Type: datetime
        """
        return self.__data['start_date']


    @readonly
    @property
    def stop_date(self) -> str:
        """
        Type: datetime
        """
        return self.__data['stop_date']


    @readonly
    @property
    def submit_date(self) -> str:
        """
        Type: datetime
        """
        return self.__data['submit_date']


    @readonly
    @property
    def comment(self) -> str:
        return self.__data['comment']


    @required
    @readonly
    @property
    def score(self) -> str:
        """
        Default value: "0"
        """
        return self.__data.setdefault('score', "0")


