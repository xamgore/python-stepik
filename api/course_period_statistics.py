# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class CoursePeriodStatistics:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'CoursePeriodStatistics(id={self.id!r})'


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @required
    @property
    def course(self) -> str:
        return self.__data['course']


    @course.setter
    def course(self, value: str):
        self.__data['course'] = value


    @property
    def from_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('from_date', "None")


    @from_date.setter
    def from_date(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self.__data['from_date'] = value


    @property
    def to_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('to_date', "None")


    @to_date.setter
    def to_date(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self.__data['to_date'] = value


    @required
    @property
    def active_learners_count(self) -> int:
        """
        Default value: ``0``
        """
        return self.__data['active_learners_count']


    @active_learners_count.setter
    def active_learners_count(self, value: int):
        """
        Default value: ``0``
        """
        self.__data['active_learners_count'] = value


    @required
    @property
    def active_learners_delta(self) -> int:
        """
        Default value: ``0``
        """
        return self.__data['active_learners_delta']


    @active_learners_delta.setter
    def active_learners_delta(self, value: int):
        """
        Default value: ``0``
        """
        self.__data['active_learners_delta'] = value


    @required
    @property
    def submissions_count(self) -> int:
        """
        Default value: ``0``
        """
        return self.__data['submissions_count']


    @submissions_count.setter
    def submissions_count(self, value: int):
        """
        Default value: ``0``
        """
        self.__data['submissions_count'] = value


    @required
    @property
    def submissions_delta(self) -> int:
        """
        Default value: ``0``
        """
        return self.__data['submissions_delta']


    @submissions_delta.setter
    def submissions_delta(self, value: int):
        """
        Default value: ``0``
        """
        self.__data['submissions_delta'] = value


    @required
    @property
    def certificates_count(self) -> int:
        """
        Default value: ``0``
        """
        return self.__data['certificates_count']


    @certificates_count.setter
    def certificates_count(self, value: int):
        """
        Default value: ``0``
        """
        self.__data['certificates_count'] = value


    @required
    @property
    def certificates_delta(self) -> int:
        """
        Default value: ``0``
        """
        return self.__data['certificates_delta']


    @certificates_delta.setter
    def certificates_delta(self, value: int):
        """
        Default value: ``0``
        """
        self.__data['certificates_delta'] = value


    @required
    @property
    def comments_count(self) -> int:
        """
        Default value: ``0``
        """
        return self.__data['comments_count']


    @comments_count.setter
    def comments_count(self, value: int):
        """
        Default value: ``0``
        """
        self.__data['comments_count'] = value


    @required
    @property
    def comments_delta(self) -> int:
        """
        Default value: ``0``
        """
        return self.__data['comments_delta']


    @comments_delta.setter
    def comments_delta(self, value: int):
        """
        Default value: ``0``
        """
        self.__data['comments_delta'] = value


    @required
    @property
    def enrollments_count(self) -> int:
        """
        Default value: ``0``
        """
        return self.__data['enrollments_count']


    @enrollments_count.setter
    def enrollments_count(self, value: int):
        """
        Default value: ``0``
        """
        self.__data['enrollments_count'] = value


    @required
    @property
    def enrollments_delta(self) -> int:
        """
        Default value: ``0``
        """
        return self.__data['enrollments_delta']


    @enrollments_delta.setter
    def enrollments_delta(self, value: int):
        """
        Default value: ``0``
        """
        self.__data['enrollments_delta'] = value


    @required
    @property
    def dropouts_count(self) -> int:
        """
        Default value: ``0``
        """
        return self.__data['dropouts_count']


    @dropouts_count.setter
    def dropouts_count(self, value: int):
        """
        Default value: ``0``
        """
        self.__data['dropouts_count'] = value


    @required
    @property
    def dropouts_delta(self) -> int:
        """
        Default value: ``0``
        """
        return self.__data['dropouts_delta']


    @dropouts_delta.setter
    def dropouts_delta(self, value: int):
        """
        Default value: ``0``
        """
        self.__data['dropouts_delta'] = value


    @readonly
    @property
    def update_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('update_date', "None")


