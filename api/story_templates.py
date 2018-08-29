# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class StoryTemplate:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'StoryTemplate(id={self.id!r})'


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @required
    @property
    def title(self) -> str:
        return self.__data['title']


    @title.setter
    def title(self, value: str):
        self.__data['title'] = value


    @required
    @property
    def parts(self) -> str:
        """
        Enter a valid JSON object

        Default value: ``[]``
        """
        return self.__data['parts']


    @parts.setter
    def parts(self, value: str):
        """
        Enter a valid JSON object

        Default value: ``[]``
        """
        self.__data['parts'] = value


    @required
    @property
    def cover(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('cover', "None")


    @cover.setter
    def cover(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self.__data['cover'] = value


    @property
    def is_published(self) -> bool:
        """
        Default value: ``False``
        """
        return self.__data['is_published']


    @is_published.setter
    def is_published(self, value: bool):
        """
        Default value: ``False``
        """
        self.__data['is_published'] = value


