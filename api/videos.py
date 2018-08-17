# This file is generated
from common import required, readonly
from typing import List



class WriteVideoSource:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'WriteVideoSource(id={self.id!r})'


    @property
    def upload_date(self) -> str:
        """
        Type: datetime
        """
        return self.__data['upload_date']


    @upload_date.setter
    def upload_date(self, value: str):
        """
        Type: datetime
        """
        self.__data['upload_date'] = value


    @property
    def filename(self) -> str:
        return self.__data['filename']


    @filename.setter
    def filename(self, value: str):
        self.__data['filename'] = value


    @property
    def lesson(self) -> str:
        return self.__data['lesson']


    @lesson.setter
    def lesson(self, value: str):
        self.__data['lesson'] = value


    @property
    def course(self) -> str:
        return self.__data['course']


    @course.setter
    def course(self, value: str):
        self.__data['course'] = value


    @property
    def source(self) -> str:
        """
        Type: file upload
        """
        return self.__data['source']


    @source.setter
    def source(self, value: str):
        """
        Type: file upload
        """
        self.__data['source'] = value


    @property
    def source_url(self) -> str:
        return self.__data['source_url']


    @source_url.setter
    def source_url(self, value: str):
        self.__data['source_url'] = value




class VideoSource:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'VideoSource(id={self.id!r})'


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
    def urls(self) -> List:
        """
        Default value: []
        """
        return self.__data['urls']


    @required
    @readonly
    @property
    def duration(self) -> int:
        """
        Default value: 0
        """
        return self.__data['duration']


    @readonly
    @property
    def status(self) -> str:
        return self.__data['status']


    @property
    def upload_date(self) -> str:
        """
        Type: datetime
        """
        return self.__data['upload_date']


    @upload_date.setter
    def upload_date(self, value: str):
        """
        Type: datetime
        """
        self.__data['upload_date'] = value


    @property
    def filename(self) -> str:
        return self.__data['filename']


    @filename.setter
    def filename(self, value: str):
        self.__data['filename'] = value


