# This file is generated
from common import required, readonly
from typing import List



class WriteUnit:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'WriteUnit(id={self.id!r})'


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
        Default value: 1
        """
        return self.__data.setdefault('position', 1)


    @position.setter
    def position(self, value: int):
        """
        Default value: 1
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


from api.assignments import Assignment


class Unit:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'Unit(id={self.id!r})'


    def assignments(self) -> List[Assignment]:
        for obj in self.__stepik.fetch_objects('assignment', self.__data['assignments']):
            yield Assignment(self.__stepik, obj)


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @required
    @property
    def section(self) -> int:
        """
        Id of the section
        """
        return self.__data['section']


    @section.setter
    def section(self, value: int):
        """
        Id of the section
        """
        self.__data['section'] = value


    @required
    @property
    def lesson(self) -> int:
        """
        Id of the lesson associated with the unit
        """
        return self.__data['lesson']


    @lesson.setter
    def lesson(self, value: int):
        """
        Id of the lesson associated with the unit
        """
        self.__data['lesson'] = value


    @required
    @property
    def position(self) -> int:
        """
        Position in the syllabus

        Default value: 1
        """
        return self.__data.setdefault('position', 1)


    @position.setter
    def position(self, value: int):
        """
        Position in the syllabus

        Default value: 1
        """
        self.__data['position'] = value


    @readonly
    @property
    def progress(self) -> str:
        """
        The progress object identifier, for internal needs.
        """
        return self.__data['progress']


    @readonly
    @property
    def begin_date(self) -> str:
        """
        Open date: when the module starts for enrolled users.

        Inherited property, so `begin_date_source` can be undefined, while `begin_date` can be gotten by hierarchy. Use `begin_date_source` to update the value.

        Type: datetime
        """
        return self.__data['begin_date']


    @readonly
    @property
    def end_date(self) -> str:
        """
        Close date: when the module will be disabled (close date is usually left empty).

        Inherited property, so `end_date_source` can be undefined, while `end_date` can be gotten by hierarchy. Use `end_date_source` to update the value.

        Type: datetime
        """
        return self.__data['end_date']


    @readonly
    @property
    def soft_deadline(self) -> str:
        """
        Soft deadline: when the cost of every step will be reduced.

        Inherited property, so `soft_deadline_source` can be undefined, while `soft_deadline` can be gotten by hierarchy. Use `soft_deadline_source` to update the value.

        Type: datetime
        """
        return self.__data['soft_deadline']


    @readonly
    @property
    def hard_deadline(self) -> str:
        """
        Hard deadline: when the cost of every step will be zero.

        Inherited property, so `hard_deadline_source` can be undefined, while `hard_deadline` can be gotten by hierarchy. Use `hard_deadline_source` to update the value.

        Type: datetime
        """
        return self.__data['hard_deadline']


    @readonly
    @property
    def grading_policy(self) -> str:
        """
        Policy can be one of these:

        * ``None`` — default for the course
        * ``"no_deadlines"`` — no deadlines
        * ``"halved"`` — half points
        * ``"linear"`` — linear descending

        Inherited property, so `grading_policy_source` can be undefined, while `grading_policy` can be gotten by hierarchy. Use `grading_policy_source` to update the value.

        Type: choice
        """
        return self.__data['grading_policy']


    @property
    def begin_date_source(self) -> str:
        """
        Open date: when the module starts for enrolled users.

        Inherited property, so `begin_date_source` can be undefined, while `begin_date` can be gotten by hierarchy. Use `begin_date_source` to update the value.

        Type: datetime
        """
        return self.__data['begin_date_source']


    @begin_date_source.setter
    def begin_date_source(self, value: str):
        """
        Open date: when the module starts for enrolled users.

        Inherited property, so `begin_date_source` can be undefined, while `begin_date` can be gotten by hierarchy. Use `begin_date_source` to update the value.

        Type: datetime
        """
        self.__data['begin_date_source'] = value


    @property
    def end_date_source(self) -> str:
        """
        Close date: when the module will be disabled (close date is usually left empty).

        Inherited property, so `end_date_source` can be undefined, while `end_date` can be gotten by hierarchy. Use `end_date_source` to update the value.

        Type: datetime
        """
        return self.__data['end_date_source']


    @end_date_source.setter
    def end_date_source(self, value: str):
        """
        Close date: when the module will be disabled (close date is usually left empty).

        Inherited property, so `end_date_source` can be undefined, while `end_date` can be gotten by hierarchy. Use `end_date_source` to update the value.

        Type: datetime
        """
        self.__data['end_date_source'] = value


    @property
    def soft_deadline_source(self) -> str:
        """
        Soft deadline: when the cost of every step will be reduced.

        Inherited property, so `soft_deadline_source` can be undefined, while `soft_deadline` can be gotten by hierarchy. Use `soft_deadline_source` to update the value.

        Type: datetime
        """
        return self.__data['soft_deadline_source']


    @soft_deadline_source.setter
    def soft_deadline_source(self, value: str):
        """
        Soft deadline: when the cost of every step will be reduced.

        Inherited property, so `soft_deadline_source` can be undefined, while `soft_deadline` can be gotten by hierarchy. Use `soft_deadline_source` to update the value.

        Type: datetime
        """
        self.__data['soft_deadline_source'] = value


    @property
    def hard_deadline_source(self) -> str:
        """
        Hard deadline: when the cost of every step will be zero.

        Inherited property, so `hard_deadline_source` can be undefined, while `hard_deadline` can be gotten by hierarchy. Use `hard_deadline_source` to update the value.

        Type: datetime
        """
        return self.__data['hard_deadline_source']


    @hard_deadline_source.setter
    def hard_deadline_source(self, value: str):
        """
        Hard deadline: when the cost of every step will be zero.

        Inherited property, so `hard_deadline_source` can be undefined, while `hard_deadline` can be gotten by hierarchy. Use `hard_deadline_source` to update the value.

        Type: datetime
        """
        self.__data['hard_deadline_source'] = value


    @property
    def grading_policy_source(self) -> str:
        """
        Policy can be one of these:

        * ``None`` — default for the course
        * ``"no_deadlines"`` — no deadlines
        * ``"halved"`` — half points
        * ``"linear"`` — linear descending

        Inherited property, so `grading_policy_source` can be undefined, while `grading_policy` can be gotten by hierarchy. Use `grading_policy_source` to update the value.

        Type: choice
        """
        return self.__data['grading_policy_source']


    @grading_policy_source.setter
    def grading_policy_source(self, value: str):
        """
        Policy can be one of these:

        * ``None`` — default for the course
        * ``"no_deadlines"`` — no deadlines
        * ``"halved"`` — half points
        * ``"linear"`` — linear descending

        Inherited property, so `grading_policy_source` can be undefined, while `grading_policy` can be gotten by hierarchy. Use `grading_policy_source` to update the value.

        Type: choice
        """
        self.__data['grading_policy_source'] = value


    @readonly
    @property
    def is_active(self) -> bool:
        """
        True, if the section is open, i.e. the server's current date is between `begin_date` and `end_date`
        """
        return self.__data['is_active']


    @readonly
    @property
    def create_date(self) -> str:
        """
        Creation time

        Type: datetime
        """
        return self.__data['create_date']


    @readonly
    @property
    def update_date(self) -> str:
        """
        Time of the last update

        Type: datetime
        """
        return self.__data['update_date']


    @required
    @property
    def assignments_ids(self) -> List[int]:
        return self.__data['assignments_ids']


    @assignments_ids.setter
    def assignments_ids(self, value: List[int]):
        self.__data['assignments_ids'] = value


