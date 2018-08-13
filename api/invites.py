# This file is generated
from common import required, readonly
from typing import List


class WriteInvite:
    def __init__(self, data):
        self.__data = data


    @required
    @property
    def invite_key(self) -> str:
        return self.__data['invite_key']


    @invite_key.setter
    def invite_key(self, value: str):
        self.__data['invite_key'] = value


class Invite:
    def __init__(self, data):
        self.__data = data


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @required
    @property
    def invite_key(self) -> str:
        return self.__data['invite_key']


    @invite_key.setter
    def invite_key(self, value: str):
        self.__data['invite_key'] = value


