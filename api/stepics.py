# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList

from api.users import User


class Environment:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'Environment(id={self.id!r})'


    def user(self) -> User:
        return User(self.__stepik, self.__stepik._fetch_object('User', self.user_id))


    def profile(self) -> User:
        return User(self.__stepik, self.__stepik._fetch_object('User', self.user_id))


    @property
    def total_quizzes(self) -> int:
        return self.__data['total_quizzes']


    @total_quizzes.setter
    def total_quizzes(self, value: int):
        self.__data['total_quizzes'] = value


    @property
    def total_active(self) -> int:
        return self.__data['total_active']


    @total_active.setter
    def total_active(self, value: int):
        self.__data['total_active'] = value


    @property
    def total_submissions(self) -> int:
        return self.__data['total_submissions']


    @total_submissions.setter
    def total_submissions(self, value: int):
        self.__data['total_submissions'] = value


    @property
    def config(self) -> dict:
        """
        Some trash actively used on the frontend.

        See `server's response <https://stepik.org/api/docs/#!/stepics>`_ to get more information.
        """
        return self.__data['config']


    @config.setter
    def config(self, value: dict):
        """
        Some trash actively used on the frontend.

        See `server's response <https://stepik.org/api/docs/#!/stepics>`_ to get more information.
        """
        self.__data['config'] = value


    @property
    def server_time(self) -> float:
        return self.__data['server_time']


    @server_time.setter
    def server_time(self, value: float):
        self.__data['server_time'] = value


    @property
    def user_id(self) -> int:
        """
        :class:`Profile`'s id
        """
        return self.__data['profile']


    @user_id.setter
    def user_id(self, value: int):
        """
        :class:`Profile`'s id
        """
        self.__data['profile'] = value


