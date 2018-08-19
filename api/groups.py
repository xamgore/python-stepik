# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class WriteGroup:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'WriteGroup(id={self.id!r})'




class Group:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'Group(id={self.id!r})'


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @readonly
    @property
    def users(self) -> str:
        return self.__data['users']


