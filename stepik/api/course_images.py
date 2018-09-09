# This file is generated
from typing import List, Iterable, Any, Optional

from stepik.errors import StepikError
from stepik.common import required, readonly
from stepik.resources_list import ResourcesList


class CourseImage:
    _resources_name = 'course-images'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'CourseImage(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model CourseImage are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @property
    def certificate_footer(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('certificate_footer', "None")


    @certificate_footer.setter
    def certificate_footer(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self._data['certificate_footer'] = value


    @property
    def certificate_cover_org(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('certificate_cover_org', "None")


    @certificate_cover_org.setter
    def certificate_cover_org(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self._data['certificate_cover_org'] = value


    @property
    def cover(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('cover', "None")


    @cover.setter
    def cover(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self._data['cover'] = value




class ListOfCourseImages:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik

