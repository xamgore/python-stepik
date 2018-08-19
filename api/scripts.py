# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class WriteScript:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'WriteScript(id={self.id!r})'


    @required
    @property
    def code(self) -> str:
        return self.__data['code']


    @code.setter
    def code(self, value: str):
        self.__data['code'] = value




class Script:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'Script(id={self.id!r})'


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @required
    @property
    def code(self) -> str:
        return self.__data['code']


    @code.setter
    def code(self, value: str):
        self.__data['code'] = value


    @required
    @readonly
    @property
    def stdout(self) -> str:
        return self.__data['stdout']


    @required
    @readonly
    @property
    def stderr(self) -> str:
        return self.__data['stderr']


    @readonly
    @property
    def status(self) -> str:
        """
        Type: choice
        """
        return self.__data['status']


