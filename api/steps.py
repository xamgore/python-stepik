# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class Step:
    _resources_name = 'steps'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'Step(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model Step are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @readonly
    @property
    def lesson(self) -> int:
        """
        :class:`Lesson`'s id 
        """
        return self._data['lesson']


    @required
    @property
    def position(self) -> int:
        """
        Position in the lesson's syllabus

        Default value: ``1``
        """
        return self._data.setdefault('position', 1)


    @position.setter
    def position(self, value: int):
        """
        Position in the lesson's syllabus

        Default value: ``1``
        """
        self._data['position'] = value


    @readonly
    @property
    def status(self) -> str:
        """
        May take one of the following values:

        * ``"preparing"
        * ``"ready"``
        * ``"error"``

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('status', "None")


    @readonly
    @property
    def block(self) -> dict:
        """
        TODO

        Type: dict
        """
        return self._data['block']


    @readonly
    @property
    def actions(self) -> dict:
        """
        Contains a dict of ``<action : link to the page>``

        Type: dict
        """
        return self._data['actions']


    @readonly
    @property
    def progress(self) -> str:
        """
        The :class:`Progress` object identifier
        """
        return self._data['progress']


    @readonly
    @property
    def subscriptions(self) -> List[str]:
        """
        List of subscriptions' ids

        Type: List[str]
        """
        return self._data['subscriptions']


    @required
    @readonly
    @property
    def instruction(self) -> str:
        """
        Something connected with exams and peer review. Maybe take ``None`` value.
        """
        return self._data['instruction']


    @readonly
    @property
    def session(self) -> str:
        """
        Something connected with exams and peer review. Maybe take ``None`` value.
        """
        return self._data['session']


    @readonly
    @property
    def instruction_type(self) -> str:
        """
        Something connected with exams and peer review. Maybe take ``None`` value.
        """
        return self._data['instruction_type']


    @readonly
    @property
    def viewed_by(self) -> int:
        """
        Number of users who checked out the step
        """
        return self._data['viewed_by']


    @readonly
    @property
    def passed_by(self) -> int:
        """
        Number of users who completed the lesson
        """
        return self._data['passed_by']


    @readonly
    @property
    def correct_ratio(self) -> float:
        """
        Percent of correct submissions.

        May take ``None`` value.
        """
        return self._data['correct_ratio']


    @readonly
    @property
    def worth(self) -> int:
        """
        Part of an adaptive system. Equals to 1 or 0. TODO
        """
        return self._data['worth']


    @property
    def is_solutions_unlocked(self) -> bool:
        """
        If true, solutions discussion tree will be opened after ``solutions_unlocked_attempts`` incorrect submissions. Otherwise, a correct submission is required. Note: Admins and teachers always have solutions forum unlocked

        Default value: ``False``
        """
        return self._data['is_solutions_unlocked']


    @is_solutions_unlocked.setter
    def is_solutions_unlocked(self, value: bool):
        """
        If true, solutions discussion tree will be opened after ``solutions_unlocked_attempts`` incorrect submissions. Otherwise, a correct submission is required. Note: Admins and teachers always have solutions forum unlocked

        Default value: ``False``
        """
        self._data['is_solutions_unlocked'] = value


    @required
    @property
    def solutions_unlocked_attempts(self) -> int:
        """
        Number of submissions to automatically open solutions discussion tree. Works only if ``is_solutions_unlocked`` equals ``True``.

        Default value: ``3``
        """
        return self._data.setdefault('solutions_unlocked_attempts', 3)


    @solutions_unlocked_attempts.setter
    def solutions_unlocked_attempts(self, value: int):
        """
        Number of submissions to automatically open solutions discussion tree. Works only if ``is_solutions_unlocked`` equals ``True``.

        Default value: ``3``
        """
        self._data['solutions_unlocked_attempts'] = value


    @property
    def has_submissions_restrictions(self) -> bool:
        """
        Limits for number of submissions. If true, then students will be allowed to send not more than ``max_submissions_count`` submissions. Note: these limits works only for learners, testers and moderators. Admins and teachers always have unlimited submissions.

        Default value: ``False``
        """
        return self._data['has_submissions_restrictions']


    @has_submissions_restrictions.setter
    def has_submissions_restrictions(self, value: bool):
        """
        Limits for number of submissions. If true, then students will be allowed to send not more than ``max_submissions_count`` submissions. Note: these limits works only for learners, testers and moderators. Admins and teachers always have unlimited submissions.

        Default value: ``False``
        """
        self._data['has_submissions_restrictions'] = value


    @required
    @property
    def max_submissions_count(self) -> int:
        """
        Number of submissions allowed to send. Works only if ``has_submissions_restrictions`` equals ``True``.

        Default value: ``3``
        """
        return self._data.setdefault('max_submissions_count', 3)


    @max_submissions_count.setter
    def max_submissions_count(self, value: int):
        """
        Number of submissions allowed to send. Works only if ``has_submissions_restrictions`` equals ``True``.

        Default value: ``3``
        """
        self._data['max_submissions_count'] = value


    @readonly
    @property
    def variation(self) -> str:
        import warnings; warnings.warn('This function is deprecated', DeprecationWarning)
        return self._data['variation']


    @readonly
    @property
    def variations_count(self) -> str:
        import warnings; warnings.warn('This function is deprecated', DeprecationWarning)
        return self._data['variations_count']


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


    @readonly
    @property
    def discussions_count(self) -> int:
        """
        Number of comment trees

        Default value: ``0``
        """
        return self._data['discussions_count']


    @readonly
    @property
    def discussion_proxy(self) -> str:
        """
        Discussion tree's identifier
        """
        return self._data['discussion_proxy']


    @readonly
    @property
    def discussion_threads(self) -> List[str]:
        """
        Same as ``discussion_proxy`` in most cases

        Type: List[str]
        """
        return self._data['discussion_threads']




class BlockView:
    _resources_name = 'steps'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'BlockView(id={self.name!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model BlockView are missing')


    @required
    @property
    def name(self) -> str:
        return self._data['name']


    @name.setter
    def name(self, value: str):
        self._data['name'] = value


    @property
    def text(self) -> str:
        return self._data['text']


    @text.setter
    def text(self, value: str):
        self._data['text'] = value


    @property
    def video(self) -> str:
        return self._data['video']


    @video.setter
    def video(self, value: str):
        self._data['video'] = value


    @property
    def animation(self) -> str:
        return self._data['animation']


    @animation.setter
    def animation(self, value: str):
        self._data['animation'] = value


    @readonly
    @property
    def options(self) -> str:
        """
        Enter a valid JSON object

        Default value: ``{}``
        """
        return self._data['options']


    @readonly
    @property
    def subtitle_files(self) -> str:
        return self._data['subtitle_files']




class ListOfSteps:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> Step:
        return Step(self._stepik, self._stepik._fetch_object(Step, id))


    def get_all(self, ids: List[int], keep_order=False) -> Iterable[Step]:
        objects = self._stepik._fetch_objects(Step, ids)
        iterable = (Step(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)
