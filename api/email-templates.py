# This file is generated
from common import required, readonly
from typing import List



class WriteEmailTemplate:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'WriteEmailTemplate(id={self.id!r})'


    @required
    @property
    def mail_type(self) -> str:
        """
        Default value: "announcement"
        """
        return self.__data.setdefault('mail_type', "announcement")


    @mail_type.setter
    def mail_type(self, value: str):
        """
        Default value: "announcement"
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
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'EmailTemplate(id={self.id!r})'


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
        Default value: "announcement"
        """
        return self.__data.setdefault('mail_type', "announcement")


    @mail_type.setter
    def mail_type(self, value: str):
        """
        Default value: "announcement"
        """
        self.__data['mail_type'] = value


    @required
    @property
    def name(self) -> str:
        return self.__data['name']


    @name.setter
    def name(self, value: str):
        self.__data['name'] = value


