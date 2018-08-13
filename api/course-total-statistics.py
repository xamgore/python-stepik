# This file is generated
from common import required, readonly
from typing import List


class WriteCourseTotalStatistics:
    def __init__(self, data):
        self.__data = data


    @required
    @property
    def course(self) -> str:
        return self.__data['course']


    @course.setter
    def course(self, value: str):
        self.__data['course'] = value


    @required
    @property
    def learners_count(self) -> int:
        """
        default value: 0
        """
        return self.__data['learners_count']


    @learners_count.setter
    def learners_count(self, value: int):
        """
        default value: 0
        """
        self.__data['learners_count'] = value


    @required
    @property
    def moderators_count(self) -> int:
        """
        default value: 0
        """
        return self.__data['moderators_count']


    @moderators_count.setter
    def moderators_count(self, value: int):
        """
        default value: 0
        """
        self.__data['moderators_count'] = value


    @required
    @property
    def testers_count(self) -> int:
        """
        default value: 0
        """
        return self.__data['testers_count']


    @testers_count.setter
    def testers_count(self, value: int):
        """
        default value: 0
        """
        self.__data['testers_count'] = value


    @required
    @property
    def enrollments_count(self) -> int:
        """
        default value: 0
        """
        return self.__data['enrollments_count']


    @enrollments_count.setter
    def enrollments_count(self, value: int):
        """
        default value: 0
        """
        self.__data['enrollments_count'] = value


    @required
    @property
    def dropouts_count(self) -> int:
        """
        default value: 0
        """
        return self.__data['dropouts_count']


    @dropouts_count.setter
    def dropouts_count(self, value: int):
        """
        default value: 0
        """
        self.__data['dropouts_count'] = value


    @required
    @property
    def certificates_count(self) -> int:
        """
        default value: 0
        """
        return self.__data['certificates_count']


    @certificates_count.setter
    def certificates_count(self, value: int):
        """
        default value: 0
        """
        self.__data['certificates_count'] = value


class CourseTotalStatistics:
    def __init__(self, data):
        self.__data = data


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


    @required
    @property
    def learners_count(self) -> int:
        """
        default value: 0
        """
        return self.__data['learners_count']


    @learners_count.setter
    def learners_count(self, value: int):
        """
        default value: 0
        """
        self.__data['learners_count'] = value


    @required
    @property
    def moderators_count(self) -> int:
        """
        default value: 0
        """
        return self.__data['moderators_count']


    @moderators_count.setter
    def moderators_count(self, value: int):
        """
        default value: 0
        """
        self.__data['moderators_count'] = value


    @required
    @property
    def testers_count(self) -> int:
        """
        default value: 0
        """
        return self.__data['testers_count']


    @testers_count.setter
    def testers_count(self, value: int):
        """
        default value: 0
        """
        self.__data['testers_count'] = value


    @required
    @property
    def enrollments_count(self) -> int:
        """
        default value: 0
        """
        return self.__data['enrollments_count']


    @enrollments_count.setter
    def enrollments_count(self, value: int):
        """
        default value: 0
        """
        self.__data['enrollments_count'] = value


    @required
    @property
    def dropouts_count(self) -> int:
        """
        default value: 0
        """
        return self.__data['dropouts_count']


    @dropouts_count.setter
    def dropouts_count(self, value: int):
        """
        default value: 0
        """
        self.__data['dropouts_count'] = value


    @required
    @property
    def certificates_count(self) -> int:
        """
        default value: 0
        """
        return self.__data['certificates_count']


    @certificates_count.setter
    def certificates_count(self, value: int):
        """
        default value: 0
        """
        self.__data['certificates_count'] = value


    @readonly
    @property
    def update_date(self) -> str:
        """
        Type: datetime
        """
        return self.__data['update_date']


