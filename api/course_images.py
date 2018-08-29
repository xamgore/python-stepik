# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



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
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('certificate_footer', "None")


    @certificate_footer.setter
    def certificate_footer(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self.__data['certificate_footer'] = value


    @property
    def certificate_cover_org(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('certificate_cover_org', "None")


    @certificate_cover_org.setter
    def certificate_cover_org(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self.__data['certificate_cover_org'] = value


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


