# This file is generated
from common import required, readonly
from typing import List


class WriteEmailTemplate:
    def __init__(self, data):
        self.__data = data


    @required
    @property
    def mail_type(self) -> str:
        """
        default value: "announcement"
        """
        return self.__data.setdefault('mail_type', "announcement")


    @mail_type.setter
    def mail_type(self, value: str):
        """
        default value: "announcement"
        """
        self.__data['mail_type'] = value


    @required
    @property
    def name(self) -> str:
        return self.__data['name']


    @name.setter
    def name(self, value: str):
        self.__data['name'] = value


class EmailTemplate:
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
    def mail_type(self) -> str:
        """
        default value: "announcement"
        """
        return self.__data.setdefault('mail_type', "announcement")


    @mail_type.setter
    def mail_type(self, value: str):
        """
        default value: "announcement"
        """
        self.__data['mail_type'] = value


    @required
    @property
    def name(self) -> str:
        return self.__data['name']


    @name.setter
    def name(self, value: str):
        self.__data['name'] = value


