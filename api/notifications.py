# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class WriteNotification:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'WriteNotification(id={self.id!r})'


    @property
    def is_unread(self) -> bool:
        """
        Default value: ``True``
        """
        return self.__data.setdefault('is_unread', True)


    @is_unread.setter
    def is_unread(self, value: bool):
        """
        Default value: ``True``
        """
        self.__data['is_unread'] = value


    @property
    def is_muted(self) -> bool:
        """
        Default value: ``False``
        """
        return self.__data['is_muted']


    @is_muted.setter
    def is_muted(self, value: bool):
        """
        Default value: ``False``
        """
        self.__data['is_muted'] = value


    @property
    def is_favorite(self) -> bool:
        """
        Default value: ``False``
        """
        return self.__data['is_favorite']


    @is_favorite.setter
    def is_favorite(self, value: bool):
        """
        Default value: ``False``
        """
        self.__data['is_favorite'] = value




class Notification:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'Notification(id={self.id!r})'


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @property
    def is_unread(self) -> bool:
        """
        Default value: ``True``
        """
        return self.__data.setdefault('is_unread', True)


    @is_unread.setter
    def is_unread(self, value: bool):
        """
        Default value: ``True``
        """
        self.__data['is_unread'] = value


    @property
    def is_muted(self) -> bool:
        """
        Default value: ``False``
        """
        return self.__data['is_muted']


    @is_muted.setter
    def is_muted(self, value: bool):
        """
        Default value: ``False``
        """
        self.__data['is_muted'] = value


    @property
    def is_favorite(self) -> bool:
        """
        Default value: ``False``
        """
        return self.__data['is_favorite']


    @is_favorite.setter
    def is_favorite(self, value: bool):
        """
        Default value: ``False``
        """
        self.__data['is_favorite'] = value


    @readonly
    @property
    def time(self) -> str:
        """
        Type: datetime
        """
        return self.__data['time']


    @readonly
    @property
    def type(self) -> str:
        return self.__data['type']


    @readonly
    @property
    def action(self) -> str:
        """
        Type: choice
        """
        return self.__data['action']


    @readonly
    @property
    def level(self) -> str:
        """
        Type: choice
        """
        return self.__data['level']


    @readonly
    @property
    def priority(self) -> str:
        """
        Type: choice
        """
        return self.__data['priority']


    @readonly
    @property
    def html_text(self) -> str:
        return self.__data['html_text']


