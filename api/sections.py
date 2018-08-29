# This file is generated
from typing import List

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList
from api.units import Unit


class Section:
    _resources_name = 'sections'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'Section(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model Section are missing')


    @property
    def units(self) -> ResourcesList[Unit]:
        return ResourcesList[Unit]\
            (Unit, self._stepik, holder=self, field_with_ids='units_ids')


    @readonly
    @property
    def id(self) -> int:
        """
        Unique identifier of sections

        The object of type ``Section`` can be accessed through ``stepik.sections.get(id)`` function.
        """
        return self._data['id']


    @required
    @property
    def course(self) -> int:
        """
        Id of the course
        """
        return self._data['course']


    @course.setter
    def course(self, value: int):
        """
        Id of the course
        """
        self._data['course'] = value


    @required
    @property
    def position(self) -> int:
        """
        Position in the syllabus

        Default value: ``1``
        """
        return self._data.setdefault('position', 1)


    @position.setter
    def position(self, value: int):
        """
        Position in the syllabus

        Default value: ``1``
        """
        self._data['position'] = value


    @property
    def discounting_policy(self) -> str:
        """
        How to change points depending on number of tries:

        * ``"no_discount"`` — do not change
        * ``"inverse"`` — decrease to 1/N
        * ``"first_one"`` — zero after first attempt
        * ``"first_third"`` — zero after third attempt

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('discounting_policy', "None")


    @discounting_policy.setter
    def discounting_policy(self, value: str):
        """
        How to change points depending on number of tries:

        * ``"no_discount"`` — do not change
        * ``"inverse"`` — decrease to 1/N
        * ``"first_one"`` — zero after first attempt
        * ``"first_third"`` — zero after third attempt

        Default value: ``"None"``

        Type: str
        """
        self._data['discounting_policy'] = value


    @readonly
    @property
    def progress(self) -> str:
        """
        The :class:`Progress` object identifier
        """
        return self._data['progress']


    @readonly
    @property
    def actions(self) -> dict:
        """
        Contains a dict of ``<action : link to the page>``

        On the summer 2018 contains only ``test_section`` if user has the `test` permission (is a tester).

        Type: dict
        """
        return self._data['actions']


    @property
    def required_section(self) -> int:
        """
        Section will be closed until a user won't complete the `required_section` (`required_percent` from the total score)
        """
        return self._data['required_section']


    @required_section.setter
    def required_section(self, value: int):
        """
        Section will be closed until a user won't complete the `required_section` (`required_percent` from the total score)
        """
        self._data['required_section'] = value


    @required
    @property
    def required_percent(self) -> int:
        """
        Section will be closed until a user won't complete the `required_section` (`required_percent` from the total score)

        Default value: ``100``
        """
        return self._data.setdefault('required_percent', 100)


    @required_percent.setter
    def required_percent(self, value: int):
        """
        Section will be closed until a user won't complete the `required_section` (`required_percent` from the total score)

        Default value: ``100``
        """
        self._data['required_percent'] = value


    @readonly
    @property
    def is_requirement_satisfied(self) -> bool:
        """
        Whether the section is open for a user. True if the score in the `required_section` is more than `required_percent` from the total score.
        """
        return self._data['is_requirement_satisfied']


    @property
    def is_exam(self) -> bool:
        """
        Whether the section is exam

        Default value: ``False``
        """
        return self._data['is_exam']


    @is_exam.setter
    def is_exam(self, value: bool):
        """
        Whether the section is exam

        Default value: ``False``
        """
        self._data['is_exam'] = value


    @required
    @property
    def exam_duration_minutes(self) -> int:
        """
        Duration of the exam. Used when ``is_exam`` is true

        Default value: ``60``
        """
        return self._data.setdefault('exam_duration_minutes', 60)


    @exam_duration_minutes.setter
    def exam_duration_minutes(self, value: int):
        """
        Duration of the exam. Used when ``is_exam`` is true

        Default value: ``60``
        """
        self._data['exam_duration_minutes'] = value


    @readonly
    @property
    def exam_session(self) -> int:
        """
        Unique identifier of the :class:`ExamSession`
        """
        return self._data['exam_session']


    @readonly
    @property
    def proctor_session(self) -> int:
        """
        Unique identifier of the :class:`ProctorSession`.

        It is used to control the user that he does not cheat during the exam.
        """
        return self._data['proctor_session']


    @property
    def description(self) -> str:
        """
        Description is display on the "Syllabus" page of the course, under the title

        Default value: ``""``
        """
        return self._data.setdefault('description', "")


    @description.setter
    def description(self, value: str):
        """
        Description is display on the "Syllabus" page of the course, under the title

        Default value: ``""``
        """
        self._data['description'] = value


    @required
    @property
    def title(self) -> str:
        """
        Title is displayed on the "Syllabus" page of the course
        """
        return self._data['title']


    @title.setter
    def title(self, value: str):
        """
        Title is displayed on the "Syllabus" page of the course
        """
        self._data['title'] = value


    @readonly
    @property
    def slug(self) -> str:
        """
        A string of format "title-id", with hyphens instead of spaces
        """
        return self._data['slug']


    @readonly
    @property
    def begin_date(self) -> str:
        """
        Open date: when the module starts for enrolled users.

        Inherited property, so `begin_date_source` can be undefined, while `begin_date` can be gotten by hierarchy. Use `begin_date_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('begin_date', "None")


    @readonly
    @property
    def end_date(self) -> str:
        """
        Close date: when the module will be disabled (close date is usually left empty).

        Inherited property, so `end_date_source` can be undefined, while `end_date` can be gotten by hierarchy. Use `end_date_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('end_date', "None")


    @readonly
    @property
    def soft_deadline(self) -> str:
        """
        Soft deadline: when the cost of every step will be reduced.

        Inherited property, so `soft_deadline_source` can be undefined, while `soft_deadline` can be gotten by hierarchy. Use `soft_deadline_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('soft_deadline', "None")


    @readonly
    @property
    def hard_deadline(self) -> str:
        """
        Hard deadline: when the cost of every step will be zero.

        Inherited property, so `hard_deadline_source` can be undefined, while `hard_deadline` can be gotten by hierarchy. Use `hard_deadline_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('hard_deadline', "None")


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

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('grading_policy', "None")


    @property
    def begin_date_source(self) -> str:
        """
        Open date: when the module starts for enrolled users

        Inherited property, so `begin_date_source` can be undefined, while `begin_date` can be gotten by hierarchy. Use `begin_date_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('begin_date_source', "None")


    @begin_date_source.setter
    def begin_date_source(self, value: str):
        """
        Open date: when the module starts for enrolled users

        Inherited property, so `begin_date_source` can be undefined, while `begin_date` can be gotten by hierarchy. Use `begin_date_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        self._data['begin_date_source'] = value


    @property
    def end_date_source(self) -> str:
        """
        Close date: when the module will be disabled (close date is usually left empty).

        Inherited property, so `end_date_source` can be undefined, while `end_date` can be gotten by hierarchy. Use `end_date_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('end_date_source', "None")


    @end_date_source.setter
    def end_date_source(self, value: str):
        """
        Close date: when the module will be disabled (close date is usually left empty).

        Inherited property, so `end_date_source` can be undefined, while `end_date` can be gotten by hierarchy. Use `end_date_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        self._data['end_date_source'] = value


    @property
    def soft_deadline_source(self) -> str:
        """
        Soft deadline: when the cost of every step will be reduced.

        Inherited property, so `soft_deadline_source` can be undefined, while `soft_deadline` can be gotten by hierarchy. Use `soft_deadline_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('soft_deadline_source', "None")


    @soft_deadline_source.setter
    def soft_deadline_source(self, value: str):
        """
        Soft deadline: when the cost of every step will be reduced.

        Inherited property, so `soft_deadline_source` can be undefined, while `soft_deadline` can be gotten by hierarchy. Use `soft_deadline_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        self._data['soft_deadline_source'] = value


    @property
    def hard_deadline_source(self) -> str:
        """
        Hard deadline: when the cost of every step will be zero.

        Inherited property, so `hard_deadline_source` can be undefined, while `hard_deadline` can be gotten by hierarchy. Use `hard_deadline_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('hard_deadline_source', "None")


    @hard_deadline_source.setter
    def hard_deadline_source(self, value: str):
        """
        Hard deadline: when the cost of every step will be zero.

        Inherited property, so `hard_deadline_source` can be undefined, while `hard_deadline` can be gotten by hierarchy. Use `hard_deadline_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        self._data['hard_deadline_source'] = value


    @property
    def grading_policy_source(self) -> str:
        """
        Policy can be one of these:

        * ``None`` — default for the course
        * ``"no_deadlines"`` — no deadlines
        * ``"halved"`` — half points
        * ``"linear"`` — linear descending

        Inherited property, so `grading_policy_source` can be undefined, while `grading_policy` can be gotten by hierarchy. Use `grading_policy_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('grading_policy_source', "None")


    @grading_policy_source.setter
    def grading_policy_source(self, value: str):
        """
        Policy can be one of these:

        * ``None`` — default for the course
        * ``"no_deadlines"`` — no deadlines
        * ``"halved"`` — half points
        * ``"linear"`` — linear descending

        Inherited property, so `grading_policy_source` can be undefined, while `grading_policy` can be gotten by hierarchy. Use `grading_policy_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        self._data['grading_policy_source'] = value


    @readonly
    @property
    def is_active(self) -> bool:
        """
        True, if the section is open, i.e. the server's current date is between `begin_date` and `end_date`
        """
        return self._data['is_active']


    @readonly
    @property
    def create_date(self) -> str:
        """
        Creation time

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('create_date', "None")


    @readonly
    @property
    def update_date(self) -> str:
        """
        Time of the last update

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('update_date', "None")


    @required
    @property
    def units_ids(self) -> List[int]:
        """
        Type: List[int]
        """
        return self._data['units']


    @units_ids.setter
    def units_ids(self, value: List[int]):
        """
        Type: List[int]
        """
        self._data['units'] = value


