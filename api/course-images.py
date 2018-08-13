# This file is generated
from common import required, readonly
from typing import List


class WriteCourseImage:
    def __init__(self, data):
        self.__data = data


    @property
    def certificate_footer(self) -> str:
        """
        Type: image upload
        """
        return self.__data['certificate_footer']


    @certificate_footer.setter
    def certificate_footer(self, value: str):
        """
        Type: image upload
        """
        self.__data['certificate_footer'] = value


    @property
    def certificate_cover_org(self) -> str:
        """
        Type: image upload
        """
        return self.__data['certificate_cover_org']


    @certificate_cover_org.setter
    def certificate_cover_org(self, value: str):
        """
        Type: image upload
        """
        self.__data['certificate_cover_org'] = value


    @property
    def cover(self) -> str:
        """
        Type: image upload
        """
        return self.__data['cover']


    @cover.setter
    def cover(self, value: str):
        """
        Type: image upload
        """
        self.__data['cover'] = value


class CourseImage:
    def __init__(self, data):
        self.__data = data


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @property
    def certificate_footer(self) -> str:
        """
        Type: image upload
        """
        return self.__data['certificate_footer']


    @certificate_footer.setter
    def certificate_footer(self, value: str):
        """
        Type: image upload
        """
        self.__data['certificate_footer'] = value


    @property
    def certificate_cover_org(self) -> str:
        """
        Type: image upload
        """
        return self.__data['certificate_cover_org']


    @certificate_cover_org.setter
    def certificate_cover_org(self, value: str):
        """
        Type: image upload
        """
        self.__data['certificate_cover_org'] = value


    @property
    def cover(self) -> str:
        """
        Type: image upload
        """
        return self.__data['cover']


    @cover.setter
    def cover(self, value: str):
        """
        Type: image upload
        """
        self.__data['cover'] = value


