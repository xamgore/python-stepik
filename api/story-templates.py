# This file is generated
from common import required, readonly
from typing import List


class WriteStoryTemplate:
    def __init__(self, data):
        self.__data = data


    @required
    @property
    def title(self) -> str:
        return self.__data['title']


    @title.setter
    def title(self, value: str):
        self.__data['title'] = value


    @required
    @property
    def parts(self) -> List:
        """
        default value: []
        """
        return self.__data['parts']


    @parts.setter
    def parts(self, value: List):
        """
        default value: []
        """
        self.__data['parts'] = value


    @required
    @property
    def cover(self) -> str:
        """
        Type: file upload
        """
        return self.__data['cover']


    @cover.setter
    def cover(self, value: str):
        """
        Type: file upload
        """
        self.__data['cover'] = value


    @property
    def is_published(self) -> bool:
        """
        default value: False
        """
        return self.__data['is_published']


    @is_published.setter
    def is_published(self, value: bool):
        """
        default value: False
        """
        self.__data['is_published'] = value


class StoryTemplate:
    def __init__(self, data):
        self.__data = data


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
    def parts(self) -> List:
        """
        default value: []
        """
        return self.__data['parts']


    @parts.setter
    def parts(self, value: List):
        """
        default value: []
        """
        self.__data['parts'] = value


    @required
    @property
    def cover(self) -> str:
        """
        Type: file upload
        """
        return self.__data['cover']


    @cover.setter
    def cover(self, value: str):
        """
        Type: file upload
        """
        self.__data['cover'] = value


    @property
    def is_published(self) -> bool:
        """
        default value: False
        """
        return self.__data['is_published']


    @is_published.setter
    def is_published(self, value: bool):
        """
        default value: False
        """
        self.__data['is_published'] = value


