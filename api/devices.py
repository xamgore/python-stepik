# This file is generated
from common import required, readonly
from typing import List


class WriteDevice:
    def __init__(self, data):
        self.__data = data


    @required
    @property
    def registration_id(self) -> str:
        return self.__data['registration_id']


    @registration_id.setter
    def registration_id(self, value: str):
        self.__data['registration_id'] = value


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
        default value: "ios"
        """
        return self.__data.setdefault('client_type', "ios")


    @client_type.setter
    def client_type(self, value: str):
        """
        default value: "ios"
        """
        self.__data['client_type'] = value


    @property
    def is_badges_enabled(self) -> bool:
        """
        default value: False
        """
        return self.__data['is_badges_enabled']


    @is_badges_enabled.setter
    def is_badges_enabled(self, value: bool):
        """
        default value: False
        """
        self.__data['is_badges_enabled'] = value


class Device:
    def __init__(self, data):
        self.__data = data


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
        default value: "ios"
        """
        return self.__data.setdefault('client_type', "ios")


    @client_type.setter
    def client_type(self, value: str):
        """
        default value: "ios"
        """
        self.__data['client_type'] = value


    @property
    def is_badges_enabled(self) -> bool:
        """
        default value: False
        """
        return self.__data['is_badges_enabled']


    @is_badges_enabled.setter
    def is_badges_enabled(self, value: bool):
        """
        default value: False
        """
        self.__data['is_badges_enabled'] = value


