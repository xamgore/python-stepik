# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class CourseReviewSummary:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'CourseReviewSummary(id={self.id!r})'


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
        Default value: ``"0"``

        Type: str
        """
        return self.__data.setdefault('average', "0")


    @required
    @readonly
    @property
    def count(self) -> int:
        """
        Default value: ``0``
        """
        return self.__data['count']


    @readonly
    @property
    def distribution(self) -> str:
        """
        Enter a valid JSON object

        Default value: ``[0, 0, 0, 0, 0]``
        """
        return self.__data.setdefault('distribution', [0, 0, 0, 0, 0])


