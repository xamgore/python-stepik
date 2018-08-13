# This file is generated
from common import required, readonly
from typing import List


class WriteSubmission:
    def __init__(self, data):
        self.__data = data


    @property
    def reply(self) -> str:
        """
        default value: {}
        """
        return self.__data['reply']


    @reply.setter
    def reply(self, value: str):
        """
        default value: {}
        """
        self.__data['reply'] = value


    @required
    @property
    def attempt(self) -> str:
        return self.__data['attempt']


    @attempt.setter
    def attempt(self, value: str):
        self.__data['attempt'] = value


class Submission:
    def __init__(self, data):
        self.__data = data


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @readonly
    @property
    def status(self) -> str:
        """
        Type: choice
        """
        return self.__data['status']


    @required
    @readonly
    @property
    def score(self) -> str:
        """
        default value: "0"
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
        Type: datetime
        """
        return self.__data['time']


    @property
    def reply(self) -> str:
        """
        default value: {}
        """
        return self.__data['reply']


    @reply.setter
    def reply(self, value: str):
        """
        default value: {}
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


