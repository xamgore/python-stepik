# This file is generated
from common import required, readonly
from typing import List


class WriteSection:
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
    def units(self) -> str:
        return self.__data['units']


    @units.setter
    def units(self, value: str):
        self.__data['units'] = value


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
    def discounting_policy(self) -> str:
        """
        Type: choice
        """
        return self.__data['discounting_policy']


    @discounting_policy.setter
    def discounting_policy(self, value: str):
        """
        Type: choice
        """
        self.__data['discounting_policy'] = value


    @property
    def required_section(self) -> str:
        return self.__data['required_section']


    @required_section.setter
    def required_section(self, value: str):
        self.__data['required_section'] = value


    @required
    @property
    def required_percent(self) -> int:
        """
        default value: 100
        """
        return self.__data.setdefault('required_percent', 100)


    @required_percent.setter
    def required_percent(self, value: int):
        """
        default value: 100
        """
        self.__data['required_percent'] = value


    @property
    def is_exam(self) -> bool:
        """
        default value: False
        """
        return self.__data['is_exam']


    @is_exam.setter
    def is_exam(self, value: bool):
        """
        default value: False
        """
        self.__data['is_exam'] = value


    @required
    @property
    def exam_duration_minutes(self) -> int:
        """
        default value: 60
        """
        return self.__data.setdefault('exam_duration_minutes', 60)


    @exam_duration_minutes.setter
    def exam_duration_minutes(self, value: int):
        """
        default value: 60
        """
        self.__data['exam_duration_minutes'] = value


    @property
    def description(self) -> str:
        return self.__data['description']


    @description.setter
    def description(self, value: str):
        self.__data['description'] = value


    @required
    @property
    def title(self) -> str:
        return self.__data['title']


    @title.setter
    def title(self, value: str):
        self.__data['title'] = value


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


class Section:
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
    def units(self) -> str:
        return self.__data['units']


    @units.setter
    def units(self, value: str):
        self.__data['units'] = value


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
    def discounting_policy(self) -> str:
        """
        Type: choice
        """
        return self.__data['discounting_policy']


    @discounting_policy.setter
    def discounting_policy(self, value: str):
        """
        Type: choice
        """
        self.__data['discounting_policy'] = value


    @readonly
    @property
    def progress(self) -> str:
        return self.__data['progress']


    @readonly
    @property
    def actions(self) -> str:
        return self.__data['actions']


    @property
    def required_section(self) -> str:
        return self.__data['required_section']


    @required_section.setter
    def required_section(self, value: str):
        self.__data['required_section'] = value


    @required
    @property
    def required_percent(self) -> int:
        """
        default value: 100
        """
        return self.__data.setdefault('required_percent', 100)


    @required_percent.setter
    def required_percent(self, value: int):
        """
        default value: 100
        """
        self.__data['required_percent'] = value


    @readonly
    @property
    def is_requirement_satisfied(self) -> str:
        return self.__data['is_requirement_satisfied']


    @property
    def is_exam(self) -> bool:
        """
        default value: False
        """
        return self.__data['is_exam']


    @is_exam.setter
    def is_exam(self, value: bool):
        """
        default value: False
        """
        self.__data['is_exam'] = value


    @required
    @property
    def exam_duration_minutes(self) -> int:
        """
        default value: 60
        """
        return self.__data.setdefault('exam_duration_minutes', 60)


    @exam_duration_minutes.setter
    def exam_duration_minutes(self, value: int):
        """
        default value: 60
        """
        self.__data['exam_duration_minutes'] = value


    @readonly
    @property
    def exam_session(self) -> str:
        return self.__data['exam_session']


    @readonly
    @property
    def proctor_session(self) -> str:
        return self.__data['proctor_session']


    @property
    def description(self) -> str:
        return self.__data['description']


    @description.setter
    def description(self, value: str):
        self.__data['description'] = value


    @required
    @property
    def title(self) -> str:
        return self.__data['title']


    @title.setter
    def title(self, value: str):
        self.__data['title'] = value


    @readonly
    @property
    def slug(self) -> str:
        return self.__data['slug']


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


