# This file is generated
from common import required, readonly
from typing import List


class WriteStorageRecord:
    def __init__(self, data):
        self.__data = data


    @property
    def kind(self) -> str:
        """
        default value: 
        """
        return self.__data['kind']


    @kind.setter
    def kind(self, value: str):
        """
        default value: 
        """
        self.__data['kind'] = value


    @property
    def data(self) -> List:
        """
        default value: {}
        """
        return self.__data['data']


    @data.setter
    def data(self, value: List):
        """
        default value: {}
        """
        self.__data['data'] = value


class StorageRecord:
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


    @property
    def kind(self) -> str:
        """
        default value: 
        """
        return self.__data['kind']


    @kind.setter
    def kind(self, value: str):
        """
        default value: 
        """
        self.__data['kind'] = value


    @property
    def data(self) -> List:
        """
        default value: {}
        """
        return self.__data['data']


    @data.setter
    def data(self, value: List):
        """
        default value: {}
        """
        self.__data['data'] = value


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


