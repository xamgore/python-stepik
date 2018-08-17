# This file is generated
from common import required, readonly
from typing import List



class WriteAttachment:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'WriteAttachment(id={self.id!r})'


    @property
    def course(self) -> str:
        return self.__data['course']


    @course.setter
    def course(self, value: str):
        self.__data['course'] = value


    @property
    def lesson(self) -> str:
        return self.__data['lesson']


    @lesson.setter
    def lesson(self, value: str):
        self.__data['lesson'] = value


    @required
    @property
    def file(self) -> str:
        """
        Type: file upload
        """
        return self.__data['file']


    @file.setter
    def file(self, value: str):
        """
        Type: file upload
        """
        self.__data['file'] = value




class Attachment:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'Attachment(id={self.id!r})'


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @readonly
    @property
    def name(self) -> str:
        return self.__data['name']


    @readonly
    @property
    def size(self) -> str:
        return self.__data['size']


    @property
    def course(self) -> str:
        return self.__data['course']


    @course.setter
    def course(self, value: str):
        self.__data['course'] = value


    @property
    def lesson(self) -> str:
        return self.__data['lesson']


    @lesson.setter
    def lesson(self, value: str):
        self.__data['lesson'] = value


    @required
    @property
    def file(self) -> str:
        """
        Type: file upload
        """
        return self.__data['file']


    @file.setter
    def file(self, value: str):
        """
        Type: file upload
        """
        self.__data['file'] = value


    @readonly
    @property
    def has_clones(self) -> str:
        return self.__data['has_clones']


