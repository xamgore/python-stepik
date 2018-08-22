# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class WriteCertificate:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'WriteCertificate(id={self.id!r})'


    @property
    def is_public(self) -> bool:
        """
        Default value: ``True``
        """
        return self.__data.setdefault('is_public', True)


    @is_public.setter
    def is_public(self, value: bool):
        """
        Default value: ``True``
        """
        self.__data['is_public'] = value




class Certificate:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'Certificate(id={self.id!r})'


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
    @readonly
    @property
    def course(self) -> str:
        return self.__data['course']


    @required
    @readonly
    @property
    def issue_date(self) -> str:
        """
        Default value: ``"2018-08-22T13:17:44.906Z"``
        """
        return self.__data.setdefault('issue_date', "2018-08-22T13:17:44.906Z")


    @readonly
    @property
    def update_date(self) -> str:
        """
        Type: datetime
        """
        return self.__data['update_date']


    @readonly
    @property
    def grade(self) -> str:
        return self.__data['grade']


    @readonly
    @property
    def type(self) -> str:
        return self.__data['type']


    @readonly
    @property
    def url(self) -> str:
        return self.__data['url']


    @readonly
    @property
    def preview_url(self) -> str:
        return self.__data['preview_url']


    @property
    def is_public(self) -> bool:
        """
        Default value: ``True``
        """
        return self.__data.setdefault('is_public', True)


    @is_public.setter
    def is_public(self, value: bool):
        """
        Default value: ``True``
        """
        self.__data['is_public'] = value


    @readonly
    @property
    def user_rank(self) -> str:
        return self.__data['user_rank']


    @readonly
    @property
    def user_rank_max(self) -> str:
        return self.__data['user_rank_max']


    @readonly
    @property
    def leaderboard_size(self) -> str:
        return self.__data['leaderboard_size']


