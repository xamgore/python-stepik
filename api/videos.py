# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class Video:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'Video(id={self.id!r})'


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @readonly
    @property
    def thumbnail(self) -> str:
        return self.__data['thumbnail']


    @required
    @readonly
    @property
    def urls(self) -> str:
        """
        Enter a valid JSON object

        Default value: ``[]``
        """
        return self.__data['urls']


    @required
    @readonly
    @property
    def duration(self) -> int:
        """
        Default value: ``0``
        """
        return self.__data['duration']


    @readonly
    @property
    def status(self) -> str:
        return self.__data['status']


    @property
    def upload_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('upload_date', "None")


    @upload_date.setter
    def upload_date(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self.__data['upload_date'] = value


    @property
    def filename(self) -> str:
        return self.__data['filename']


    @filename.setter
    def filename(self, value: str):
        self.__data['filename'] = value


