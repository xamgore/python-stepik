# This file is generated
from common import required, readonly
from typing import List



class WriteCourseImage:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'WriteCourseImage(id={self.id!r})'


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
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'CourseImage(id={self.id!r})'


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


