# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class Submission:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'Submission(id={self.id!r})'


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @readonly
    @property
    def status(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('status', "None")


    @required
    @readonly
    @property
    def score(self) -> str:
        """
        Default value: ``"0"``

        Type: str
        """
        return self.__data.setdefault('score', "0")


    @readonly
    @property
    def hint(self) -> str:
        return self.__data['hint']


    @readonly
    @property
    def feedback(self) -> str:
        return self.__data['feedback']


    @readonly
    @property
    def time(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('time', "None")


    @property
    def reply(self) -> str:
        """
        Default value: ``{}``
        """
        return self.__data['reply']


    @reply.setter
    def reply(self, value: str):
        """
        Default value: ``{}``
        """
        self.__data['reply'] = value


    @readonly
    @property
    def reply_url(self) -> str:
        return self.__data['reply_url']


    @required
    @property
    def attempt(self) -> str:
        return self.__data['attempt']


    @attempt.setter
    def attempt(self, value: str):
        self.__data['attempt'] = value


    @required
    @readonly
    @property
    def session(self) -> str:
        return self.__data['session']


    @readonly
    @property
    def eta(self) -> int:
        return self.__data['eta']


