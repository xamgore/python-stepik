# This file is generated
from typing import List

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class CourseTotalStatistics:
    _resources_name = 'course-total-statistics'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'CourseTotalStatistics(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model CourseTotalStatistics are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @property
    def course(self) -> str:
        return self._data['course']


    @course.setter
    def course(self, value: str):
        self._data['course'] = value


    @required
    @property
    def learners_count(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['learners_count']


    @learners_count.setter
    def learners_count(self, value: int):
        """
        Default value: ``0``
        """
        self._data['learners_count'] = value


    @required
    @property
    def moderators_count(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['moderators_count']


    @moderators_count.setter
    def moderators_count(self, value: int):
        """
        Default value: ``0``
        """
        self._data['moderators_count'] = value


    @required
    @property
    def testers_count(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['testers_count']


    @testers_count.setter
    def testers_count(self, value: int):
        """
        Default value: ``0``
        """
        self._data['testers_count'] = value


    @required
    @property
    def enrollments_count(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['enrollments_count']


    @enrollments_count.setter
    def enrollments_count(self, value: int):
        """
        Default value: ``0``
        """
        self._data['enrollments_count'] = value


    @required
    @property
    def dropouts_count(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['dropouts_count']


    @dropouts_count.setter
    def dropouts_count(self, value: int):
        """
        Default value: ``0``
        """
        self._data['dropouts_count'] = value


    @required
    @property
    def certificates_count(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['certificates_count']


    @certificates_count.setter
    def certificates_count(self, value: int):
        """
        Default value: ``0``
        """
        self._data['certificates_count'] = value


    @readonly
    @property
    def update_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('update_date', "None")


