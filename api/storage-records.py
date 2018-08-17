# This file is generated
from common import required, readonly
from typing import List



class WriteStorageRecord:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'WriteStorageRecord(id={self.id!r})'


    @property
    def kind(self) -> str:
        """
        Default value: 
        """
        return self.__data['kind']


    @kind.setter
    def kind(self, value: str):
        """
        Default value: 
        """
        self.__data['kind'] = value


    @property
    def data(self) -> List:
        """
        Default value: {}
        """
        return self.__data['data']


    @data.setter
    def data(self, value: List):
        """
        Default value: {}
        """
        self.__data['data'] = value




class StorageRecord:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'StorageRecord(id={self.id!r})'


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
        Default value: 
        """
        return self.__data['kind']


    @kind.setter
    def kind(self, value: str):
        """
        Default value: 
        """
        self.__data['kind'] = value


    @property
    def data(self) -> List:
        """
        Default value: {}
        """
        return self.__data['data']


    @data.setter
    def data(self, value: List):
        """
        Default value: {}
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


