# This file is generated
from common import required, readonly
from typing import List



class WriteInvitation:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'WriteInvitation(id={self.id!r})'


    @required
    @property
    def group(self) -> str:
        return self.__data['group']


    @group.setter
    def group(self, value: str):
        self.__data['group'] = value


    @property
    def email(self) -> str:
        """
        Type: email
        """
        return self.__data['email']


    @email.setter
    def email(self, value: str):
        """
        Type: email
        """
        self.__data['email'] = value


    @property
    def description(self) -> str:
        return self.__data['description']


    @description.setter
    def description(self, value: str):
        self.__data['description'] = value


    @property
    def limit(self) -> int:
        return self.__data['limit']


    @limit.setter
    def limit(self, value: int):
        self.__data['limit'] = value




class Invitation:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'Invitation(id={self.id!r})'


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @required
    @property
    def group(self) -> str:
        return self.__data['group']


    @group.setter
    def group(self, value: str):
        self.__data['group'] = value


    @readonly
    @property
    def name(self) -> str:
        return self.__data['name']


    @readonly
    @property
    def url(self) -> str:
        return self.__data['url']


    @property
    def description(self) -> str:
        return self.__data['description']


    @description.setter
    def description(self, value: str):
        self.__data['description'] = value


    @property
    def limit(self) -> int:
        return self.__data['limit']


    @limit.setter
    def limit(self, value: int):
        self.__data['limit'] = value


