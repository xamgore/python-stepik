# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class WriteMember:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'WriteMember(id={self.id!r})'


    @required
    @property
    def group(self) -> str:
        return self.__data['group']


    @group.setter
    def group(self, value: str):
        self.__data['group'] = value


    @property
    def user(self) -> str:
        return self.__data['user']


    @user.setter
    def user(self, value: str):
        self.__data['user'] = value


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
    def is_synced(self) -> bool:
        """
        Default value: ``False``
        """
        return self.__data['is_synced']


    @is_synced.setter
    def is_synced(self, value: bool):
        """
        Default value: ``False``
        """
        self.__data['is_synced'] = value




class Member:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'Member(id={self.id!r})'


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


    @property
    def user(self) -> str:
        return self.__data['user']


    @user.setter
    def user(self, value: str):
        self.__data['user'] = value


    @required
    @readonly
    @property
    def date_joined(self) -> str:
        """
        Default value: ``"2018-08-10T09:48:04.316Z"``
        """
        return self.__data.setdefault('date_joined', "2018-08-10T09:48:04.316Z")


    @property
    def is_synced(self) -> bool:
        """
        Default value: ``False``
        """
        return self.__data['is_synced']


    @is_synced.setter
    def is_synced(self, value: bool):
        """
        Default value: ``False``
        """
        self.__data['is_synced'] = value


