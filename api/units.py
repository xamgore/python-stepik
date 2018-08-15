# This file is generated
from common import required, readonly
from typing import List


class WriteUnit:
    def __init__(self, data):
        self.__data = data


    @required
    @property
    def section(self) -> str:
        return self.__data['section']


    @section.setter
    def section(self, value: str):
        self.__data['section'] = value


    @required
    @property
    def lesson(self) -> str:
        return self.__data['lesson']


    @lesson.setter
    def lesson(self, value: str):
        self.__data['lesson'] = value


    @required
    @property
    def assignments(self) -> str:
        return self.__data['assignments']


    @assignments.setter
    def assignments(self, value: str):
        self.__data['assignments'] = value


    @required
    @property
    def position(self) -> int:
        """
        default value: 1
        """
        return self.__data.setdefault('position', 1)


    @position.setter
    def position(self, value: int):
        """
        default value: 1
        """
        self.__data['position'] = value


    @property
    def begin_date_source(self) -> str:
        """
        Type: datetime
        """
        return self.__data['begin_date_source']


    @begin_date_source.setter
    def begin_date_source(self, value: str):
        """
        Type: datetime
        """
        self.__data['begin_date_source'] = value


    @property
    def end_date_source(self) -> str:
        """
        Type: datetime
        """
        return self.__data['end_date_source']


    @end_date_source.setter
    def end_date_source(self, value: str):
        """
        Type: datetime
        """
        self.__data['end_date_source'] = value


    @property
    def soft_deadline_source(self) -> str:
        """
        Type: datetime
        """
        return self.__data['soft_deadline_source']


    @soft_deadline_source.setter
    def soft_deadline_source(self, value: str):
        """
        Type: datetime
        """
        self.__data['soft_deadline_source'] = value


    @property
    def hard_deadline_source(self) -> str:
        """
        Type: datetime
        """
        return self.__data['hard_deadline_source']


    @hard_deadline_source.setter
    def hard_deadline_source(self, value: str):
        """
        Type: datetime
        """
        self.__data['hard_deadline_source'] = value


    @property
    def grading_policy_source(self) -> str:
        """
        Type: choice
        """
        return self.__data['grading_policy_source']


    @grading_policy_source.setter
    def grading_policy_source(self, value: str):
        """
        Type: choice
        """
        self.__data['grading_policy_source'] = value


class Unit:
    def __init__(self, data):
        self.__data = data


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @required
    @property
    def section(self) -> str:
        return self.__data['section']


    @section.setter
    def section(self, value: str):
        self.__data['section'] = value


    @required
    @property
    def lesson(self) -> int:
        """
        Lesson id, associated with the unit
        """
        return self.__data['lesson']


    @lesson.setter
    def lesson(self, value: int):
        """
        Lesson id, associated with the unit
        """
        self.__data['lesson'] = value


    @required
    @property
    def assignments(self) -> str:
        return self.__data['assignments']


    @assignments.setter
    def assignments(self, value: str):
        self.__data['assignments'] = value


    @required
    @property
    def position(self) -> int:
        """
        default value: 1
        """
        return self.__data.setdefault('position', 1)


    @position.setter
    def position(self, value: int):
        """
        default value: 1
        """
        self.__data['position'] = value


    @readonly
    @property
    def progress(self) -> str:
        return self.__data['progress']


    @readonly
    @property
    def begin_date(self) -> str:
        """
        Type: datetime
        """
        return self.__data['begin_date']


    @readonly
    @property
    def end_date(self) -> str:
        """
        Type: datetime
        """
        return self.__data['end_date']


    @readonly
    @property
    def soft_deadline(self) -> str:
        """
        Type: datetime
        """
        return self.__data['soft_deadline']


    @readonly
    @property
    def hard_deadline(self) -> str:
        """
        Type: datetime
        """
        return self.__data['hard_deadline']


    @readonly
    @property
    def grading_policy(self) -> str:
        """
        Type: choice
        """
        return self.__data['grading_policy']


    @property
    def begin_date_source(self) -> str:
        """
        Type: datetime
        """
        return self.__data['begin_date_source']


    @begin_date_source.setter
    def begin_date_source(self, value: str):
        """
        Type: datetime
        """
        self.__data['begin_date_source'] = value


    @property
    def end_date_source(self) -> str:
        """
        Type: datetime
        """
        return self.__data['end_date_source']


    @end_date_source.setter
    def end_date_source(self, value: str):
        """
        Type: datetime
        """
        self.__data['end_date_source'] = value


    @property
    def soft_deadline_source(self) -> str:
        """
        Type: datetime
        """
        return self.__data['soft_deadline_source']


    @soft_deadline_source.setter
    def soft_deadline_source(self, value: str):
        """
        Type: datetime
        """
        self.__data['soft_deadline_source'] = value


    @property
    def hard_deadline_source(self) -> str:
        """
        Type: datetime
        """
        return self.__data['hard_deadline_source']


    @hard_deadline_source.setter
    def hard_deadline_source(self, value: str):
        """
        Type: datetime
        """
        self.__data['hard_deadline_source'] = value


    @property
    def grading_policy_source(self) -> str:
        """
        Type: choice
        """
        return self.__data['grading_policy_source']


    @grading_policy_source.setter
    def grading_policy_source(self, value: str):
        """
        Type: choice
        """
        self.__data['grading_policy_source'] = value


    @readonly
    @property
    def is_active(self) -> bool:
        return self.__data['is_active']


    @readonly
    @property
    def create_date(self) -> str:
        """
        Type: datetime
        """
        return self.__data['create_date']


    @readonly
    @property
    def update_date(self) -> str:
        """
        Type: datetime
        """
        return self.__data['update_date']


