# This file is generated
from common import required, readonly
from typing import List


class WriteSession:
    def __init__(self, data):
        self.__data = data


    @property
    def instruction(self) -> str:
        return self.__data['instruction']


    @instruction.setter
    def instruction(self, value: str):
        self.__data['instruction'] = value


    @property
    def submission(self) -> str:
        return self.__data['submission']


    @submission.setter
    def submission(self, value: str):
        self.__data['submission'] = value


class Session:
    def __init__(self, data):
        self.__data = data


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @property
    def instruction(self) -> str:
        return self.__data['instruction']


    @instruction.setter
    def instruction(self, value: str):
        self.__data['instruction'] = value


    @property
    def submission(self) -> str:
        return self.__data['submission']


    @submission.setter
    def submission(self, value: str):
        self.__data['submission'] = value


    @readonly
    @property
    def given_reviews(self) -> str:
        return self.__data['given_reviews']


    @readonly
    @property
    def is_giving_started(self) -> str:
        return self.__data['is_giving_started']


    @readonly
    @property
    def is_giving_finished(self) -> str:
        return self.__data['is_giving_finished']


    @readonly
    @property
    def taken_reviews(self) -> str:
        return self.__data['taken_reviews']


    @readonly
    @property
    def is_taking_started(self) -> str:
        return self.__data['is_taking_started']


    @readonly
    @property
    def is_taking_finished(self) -> str:
        return self.__data['is_taking_finished']


    @readonly
    @property
    def is_taking_finished_by_teacher(self) -> str:
        return self.__data['is_taking_finished_by_teacher']


    @readonly
    @property
    def when_taking_finished_by_teacher(self) -> str:
        """
        Type: datetime
        """
        return self.__data['when_taking_finished_by_teacher']


    @readonly
    @property
    def is_review_available(self) -> str:
        return self.__data['is_review_available']


    @readonly
    @property
    def is_finished(self) -> str:
        return self.__data['is_finished']


    @required
    @readonly
    @property
    def score(self) -> int:
        """
        default value: 0
        """
        return self.__data['score']


    @readonly
    @property
    def available_reviews_count(self) -> str:
        return self.__data['available_reviews_count']


    @readonly
    @property
    def active_review(self) -> str:
        return self.__data['active_review']


    @readonly
    @property
    def actions(self) -> str:
        return self.__data['actions']


