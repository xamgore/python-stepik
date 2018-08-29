# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class Device:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'Device(id={self.id!r})'


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @required
    @property
    def registration_id(self) -> str:
        return self.__data['registration_id']


    @registration_id.setter
    def registration_id(self, value: str):
        self.__data['registration_id'] = value


    @required
    @readonly
    @property
    def user(self) -> str:
        return self.__data['user']


    @required
    @property
    def description(self) -> str:
        return self.__data['description']


    @description.setter
    def description(self, value: str):
        self.__data['description'] = value


    @required
    @property
    def client_type(self) -> str:
        """
        Default value: ``"ios"``

        Type: str
        """
        return self.__data.setdefault('client_type', "ios")


    @client_type.setter
    def client_type(self, value: str):
        """
        Default value: ``"ios"``

        Type: str
        """
        self.__data['client_type'] = value


    @property
    def is_badges_enabled(self) -> bool:
        """
        Default value: ``False``
        """
        return self.__data['is_badges_enabled']


    @is_badges_enabled.setter
    def is_badges_enabled(self, value: bool):
        """
        Default value: ``False``
        """
        self.__data['is_badges_enabled'] = value


