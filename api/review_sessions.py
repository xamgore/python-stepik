# This file is generated
from typing import List

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class Session:
    _resources_name = 'review-sessions'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'Session(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model Session are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @property
    def instruction(self) -> str:
        return self._data['instruction']


    @instruction.setter
    def instruction(self, value: str):
        self._data['instruction'] = value


    @property
    def submission(self) -> str:
        return self._data['submission']


    @submission.setter
    def submission(self, value: str):
        self._data['submission'] = value


    @readonly
    @property
    def given_reviews(self) -> str:
        return self._data['given_reviews']


    @readonly
    @property
    def is_giving_started(self) -> str:
        return self._data['is_giving_started']


    @readonly
    @property
    def is_giving_finished(self) -> str:
        return self._data['is_giving_finished']


    @readonly
    @property
    def taken_reviews(self) -> str:
        return self._data['taken_reviews']


    @readonly
    @property
    def is_taking_started(self) -> str:
        return self._data['is_taking_started']


    @readonly
    @property
    def is_taking_finished(self) -> str:
        return self._data['is_taking_finished']


    @readonly
    @property
    def is_taking_finished_by_teacher(self) -> str:
        return self._data['is_taking_finished_by_teacher']


    @readonly
    @property
    def when_taking_finished_by_teacher(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('when_taking_finished_by_teacher', "None")


    @readonly
    @property
    def is_review_available(self) -> str:
        return self._data['is_review_available']


    @readonly
    @property
    def is_finished(self) -> str:
        return self._data['is_finished']


    @required
    @readonly
    @property
    def score(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['score']


    @readonly
    @property
    def available_reviews_count(self) -> str:
        return self._data['available_reviews_count']


    @readonly
    @property
    def active_review(self) -> str:
        return self._data['active_review']


    @readonly
    @property
    def actions(self) -> str:
        return self._data['actions']


