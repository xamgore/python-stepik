# This file is generated
from typing import List, Iterable, Any, Optional

from stepik.errors import StepikError
from stepik.common import required, readonly
from stepik.resources_list import ResourcesList


class Video:
    _resources_name = 'videos'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'Video(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model Video are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @readonly
    @property
    def thumbnail(self) -> str:
        return self._data['thumbnail']


    @required
    @readonly
    @property
    def urls(self) -> str:
        """
        Enter a valid JSON object

        Default value: ``[]``
        """
        return self._data['urls']


    @required
    @readonly
    @property
    def duration(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['duration']


    @readonly
    @property
    def status(self) -> str:
        return self._data['status']


    @property
    def upload_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('upload_date', "None")


    @upload_date.setter
    def upload_date(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self._data['upload_date'] = value


    @property
    def filename(self) -> str:
        return self._data['filename']


    @filename.setter
    def filename(self, value: str):
        self._data['filename'] = value




class ListOfVideos:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik

