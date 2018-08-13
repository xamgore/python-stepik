# This file is generated
from common import required, readonly
from typing import List


class WriteCourseReviewSummary:
    def __init__(self, data):
        self.__data = data


class CourseReviewSummary:
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
    def average(self) -> str:
        """
        default value: "0"
        """
        return self.__data.setdefault('average', "0")


    @required
    @readonly
    @property
    def count(self) -> int:
        """
        default value: 0
        """
        return self.__data['count']


    @readonly
    @property
    def distribution(self) -> List:
        """
        default value: [0, 0, 0, 0, 0]
        """
        return self.__data.setdefault('distribution', [0, 0, 0, 0, 0])


