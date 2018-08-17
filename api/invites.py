# This file is generated
from common import required, readonly
from typing import List



class WriteInvite:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'WriteInvite(id={self.id!r})'


    @required
    @property
    def invite_key(self) -> str:
        return self.__data['invite_key']


    @invite_key.setter
    def invite_key(self, value: str):
        self.__data['invite_key'] = value




class Invite:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'Invite(id={self.id!r})'


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


