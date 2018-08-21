# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class WriteSection:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'WriteSection(id={self.id!r})'


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
        Default value: ``1``
        """
        return self.__data.setdefault('position', 1)


    @position.setter
    def position(self, value: int):
        """
        Default value: ``1``
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
        Default value: ``100``
        """
        return self.__data.setdefault('required_percent', 100)


    @required_percent.setter
    def required_percent(self, value: int):
        """
        Default value: ``100``
        """
        self.__data['required_percent'] = value


    @property
    def is_exam(self) -> bool:
        """
        Default value: ``False``
        """
        return self.__data['is_exam']


    @is_exam.setter
    def is_exam(self, value: bool):
        """
        Default value: ``False``
        """
        self.__data['is_exam'] = value


    @required
    @property
    def exam_duration_minutes(self) -> int:
        """
        Default value: ``60``
        """
        return self.__data.setdefault('exam_duration_minutes', 60)


    @exam_duration_minutes.setter
    def exam_duration_minutes(self, value: int):
        """
        Default value: ``60``
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


from api.units import Unit


class Section:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'Section(id={self.id!r})'


    @property
    def units(self) -> ResourcesList[Unit]:
        return ResourcesList[Unit](Unit, self.__stepik, self, 'units_ids')


    @readonly
    @property
    def id(self) -> int:
        """
        Unique identifier of sections

        The object of type ``Section`` can be accessed through ``stepik.sections.get(id)`` function.
        """
        return self.__data['id']


    @required
    @property
    def course(self) -> int:
        """
        Id of the course
        """
        return self.__data['course']


    @course.setter
    def course(self, value: int):
        """
        Id of the course
        """
        self.__data['course'] = value


    @required
    @property
    def position(self) -> int:
        """
        Position in the syllabus

        Default value: ``1``
        """
        return self.__data.setdefault('position', 1)


    @position.setter
    def position(self, value: int):
        """
        Position in the syllabus

        Default value: ``1``
        """
        self.__data['position'] = value


    @property
    def discounting_policy(self) -> str:
        """
        How to change points depending on number of tries:

        * ``"no_discount"`` — do not change
        * ``"inverse"`` — decrease to 1/N
        * ``"first_one"`` — zero after first attempt
        * ``"first_third"`` — zero after third attempt

        Type: choice
        """
        return self.__data['discounting_policy']


    @discounting_policy.setter
    def discounting_policy(self, value: str):
        """
        How to change points depending on number of tries:

        * ``"no_discount"`` — do not change
        * ``"inverse"`` — decrease to 1/N
        * ``"first_one"`` — zero after first attempt
        * ``"first_third"`` — zero after third attempt

        Type: choice
        """
        self.__data['discounting_policy'] = value


    @readonly
    @property
    def progress(self) -> str:
        """
        The :class:`Progress` object identifier
        """
        return self.__data['progress']


    @readonly
    @property
    def actions(self) -> dict:
        """
        Contains a dict of ``<action : link to the page>``

        On the summer 2018 contains only ``test_section`` if user has the `test` permission (is a tester).
        """
        return self.__data['actions']


    @property
    def required_section(self) -> int:
        """
        Section will be closed until a user won't complete the `required_section` (`required_percent` from the total score)
        """
        return self.__data['required_section']


    @required_section.setter
    def required_section(self, value: int):
        """
        Section will be closed until a user won't complete the `required_section` (`required_percent` from the total score)
        """
        self.__data['required_section'] = value


    @required
    @property
    def required_percent(self) -> int:
        """
        Section will be closed until a user won't complete the `required_section` (`required_percent` from the total score)

        Default value: ``100``
        """
        return self.__data.setdefault('required_percent', 100)


    @required_percent.setter
    def required_percent(self, value: int):
        """
        Section will be closed until a user won't complete the `required_section` (`required_percent` from the total score)

        Default value: ``100``
        """
        self.__data['required_percent'] = value


    @readonly
    @property
    def is_requirement_satisfied(self) -> bool:
        """
        Whether the section is open for a user. True if the score in the `required_section` is more than `required_percent` from the total score.
        """
        return self.__data['is_requirement_satisfied']


    @property
    def is_exam(self) -> bool:
        """
        Whether the section is exam

        Default value: ``False``
        """
        return self.__data['is_exam']


    @is_exam.setter
    def is_exam(self, value: bool):
        """
        Whether the section is exam

        Default value: ``False``
        """
        self.__data['is_exam'] = value


    @required
    @property
    def exam_duration_minutes(self) -> int:
        """
        Duration of the exam. Used when ``is_exam`` is true

        Default value: ``60``
        """
        return self.__data.setdefault('exam_duration_minutes', 60)


    @exam_duration_minutes.setter
    def exam_duration_minutes(self, value: int):
        """
        Duration of the exam. Used when ``is_exam`` is true

        Default value: ``60``
        """
        self.__data['exam_duration_minutes'] = value


    @readonly
    @property
    def exam_session(self) -> int:
        """
        Unique identifier of the :class:`ExamSession`
        """
        return self.__data['exam_session']


    @readonly
    @property
    def proctor_session(self) -> int:
        """
        Unique identifier of the :class:`ProctorSession`.

        It is used to control the user that he does not cheat during the exam.
        """
        return self.__data['proctor_session']


    @property
    def description(self) -> str:
        """
        Description is display on the "Syllabus" page of the course, under the title

        Default value: ``""``
        """
        return self.__data.setdefault('description', "")


    @description.setter
    def description(self, value: str):
        """
        Description is display on the "Syllabus" page of the course, under the title

        Default value: ``""``
        """
        self.__data['description'] = value


    @required
    @property
    def title(self) -> str:
        """
        Title is displayed on the "Syllabus" page of the course
        """
        return self.__data['title']


    @title.setter
    def title(self, value: str):
        """
        Title is displayed on the "Syllabus" page of the course
        """
        self.__data['title'] = value


    @readonly
    @property
    def slug(self) -> str:
        """
        A string of format "title-id", with hyphens instead of spaces
        """
        return self.__data['slug']


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
        Open date: when the module starts for enrolled users

        Inherited property, so `begin_date_source` can be undefined, while `begin_date` can be gotten by hierarchy. Use `begin_date_source` to update the value.

        Type: datetime
        """
        return self.__data['begin_date_source']


    @begin_date_source.setter
    def begin_date_source(self, value: str):
        """
        Open date: when the module starts for enrolled users

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
    def units_ids(self) -> List[int]:
        return self.__data['units']


    @units_ids.setter
    def units_ids(self, value: List[int]):
        self.__data['units'] = value


