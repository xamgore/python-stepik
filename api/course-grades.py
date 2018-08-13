# This file is generated
from common import required, readonly
from typing import List


class WriteCourseGrade:
    def __init__(self, data):
        self.__data = data


class CourseGrade:
    def __init__(self, data):
        self.__data = data


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @required
    @readonly
    @property
    def course(self) -> str:
        return self.__data['course']


    @required
    @readonly
    @property
    def user(self) -> str:
        return self.__data['user']


    @readonly
    @property
    def results(self) -> str:
        return self.__data['results']


    @required
    @readonly
    @property
    def score(self) -> str:
        """
        default value: "0"
        """
        return self.__data.setdefault('score', "0")


    @readonly
    @property
    def rank(self) -> int:
        return self.__data['rank']


    @readonly
    @property
    def rank_max(self) -> int:
        return self.__data['rank_max']


    @readonly
    @property
    def rank_position(self) -> int:
        return self.__data['rank_position']


    @readonly
    @property
    def users_count(self) -> int:
        return self.__data['users_count']


    @readonly
    @property
    def is_teacher(self) -> bool:
        """
        default value: False
        """
        return self.__data['is_teacher']


    @readonly
    @property
    def date_joined(self) -> str:
        """
        Type: datetime
        """
        return self.__data['date_joined']


    @readonly
    @property
    def last_viewed(self) -> str:
        """
        Type: datetime
        """
        return self.__data['last_viewed']


    @readonly
    @property
    def certificate_issue_date(self) -> str:
        return self.__data['certificate_issue_date']


    @readonly
    @property
    def certificate_issue_regular_date(self) -> str:
        return self.__data['certificate_issue_regular_date']


    @readonly
    @property
    def certificate_issue_distinction_date(self) -> str:
        return self.__data['certificate_issue_distinction_date']


    @readonly
    @property
    def certificate_update_date(self) -> str:
        return self.__data['certificate_update_date']


    @readonly
    @property
    def certificate_url(self) -> str:
        return self.__data['certificate_url']


