# This file is generated
from typing import List

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class StepIssue:
    _resources_name = 'step-issues'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'StepIssue(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model StepIssue are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @property
    def step(self) -> str:
        return self._data['step']


    @step.setter
    def step(self, value: str):
        self._data['step'] = value


    @required
    @property
    def epoch_time(self) -> str:
        """
        Default value: ``"2018-08-26T00:35:43.217Z"``

        Type: str
        """
        return self._data.setdefault('epoch_time', "2018-08-26T00:35:43.217Z")


    @epoch_time.setter
    def epoch_time(self, value: str):
        """
        Default value: ``"2018-08-26T00:35:43.217Z"``

        Type: str
        """
        self._data['epoch_time'] = value


    @property
    def has_quiz_error(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['has_quiz_error']


    @has_quiz_error.setter
    def has_quiz_error(self, value: bool):
        """
        Default value: ``False``
        """
        self._data['has_quiz_error'] = value


    @property
    def has_quiz_warning(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['has_quiz_warning']


    @has_quiz_warning.setter
    def has_quiz_warning(self, value: bool):
        """
        Default value: ``False``
        """
        self._data['has_quiz_warning'] = value


    @required
    @property
    def unique_views(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['unique_views']


    @unique_views.setter
    def unique_views(self, value: int):
        """
        Default value: ``0``
        """
        self._data['unique_views'] = value


    @required
    @property
    def total_views(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['total_views']


    @total_views.setter
    def total_views(self, value: int):
        """
        Default value: ``0``
        """
        self._data['total_views'] = value


    @required
    @property
    def unique_successes(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['unique_successes']


    @unique_successes.setter
    def unique_successes(self, value: int):
        """
        Default value: ``0``
        """
        self._data['unique_successes'] = value


    @required
    @property
    def unique_failures(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['unique_failures']


    @unique_failures.setter
    def unique_failures(self, value: int):
        """
        Default value: ``0``
        """
        self._data['unique_failures'] = value


    @required
    @property
    def unique_attempts(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['unique_attempts']


    @unique_attempts.setter
    def unique_attempts(self, value: int):
        """
        Default value: ``0``
        """
        self._data['unique_attempts'] = value


    @required
    @property
    def unique_correct_ratio(self) -> str:
        """
        Default value: ``"0"``

        Type: str
        """
        return self._data.setdefault('unique_correct_ratio', "0")


    @unique_correct_ratio.setter
    def unique_correct_ratio(self, value: str):
        """
        Default value: ``"0"``

        Type: str
        """
        self._data['unique_correct_ratio'] = value


    @required
    @property
    def total_successes(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['total_successes']


    @total_successes.setter
    def total_successes(self, value: int):
        """
        Default value: ``0``
        """
        self._data['total_successes'] = value


    @required
    @property
    def total_failures(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['total_failures']


    @total_failures.setter
    def total_failures(self, value: int):
        """
        Default value: ``0``
        """
        self._data['total_failures'] = value


    @required
    @property
    def total_attempts(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['total_attempts']


    @total_attempts.setter
    def total_attempts(self, value: int):
        """
        Default value: ``0``
        """
        self._data['total_attempts'] = value


    @required
    @property
    def total_correct_ratio(self) -> str:
        """
        Default value: ``"0"``

        Type: str
        """
        return self._data.setdefault('total_correct_ratio', "0")


    @total_correct_ratio.setter
    def total_correct_ratio(self, value: str):
        """
        Default value: ``"0"``

        Type: str
        """
        self._data['total_correct_ratio'] = value


    @required
    @property
    def total_comments(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['total_comments']


    @total_comments.setter
    def total_comments(self, value: int):
        """
        Default value: ``0``
        """
        self._data['total_comments'] = value


    @required
    @property
    def pending_comments(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['pending_comments']


    @pending_comments.setter
    def pending_comments(self, value: int):
        """
        Default value: ``0``
        """
        self._data['pending_comments'] = value


    @required
    @property
    def deleted_comments(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['deleted_comments']


    @deleted_comments.setter
    def deleted_comments(self, value: int):
        """
        Default value: ``0``
        """
        self._data['deleted_comments'] = value


    @required
    @property
    def epic_comment_votes(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['epic_comment_votes']


    @epic_comment_votes.setter
    def epic_comment_votes(self, value: int):
        """
        Default value: ``0``
        """
        self._data['epic_comment_votes'] = value


    @required
    @property
    def abuse_comment_votes(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['abuse_comment_votes']


    @abuse_comment_votes.setter
    def abuse_comment_votes(self, value: int):
        """
        Default value: ``0``
        """
        self._data['abuse_comment_votes'] = value


    @required
    @property
    def total_reviews(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['total_reviews']


    @total_reviews.setter
    def total_reviews(self, value: int):
        """
        Default value: ``0``
        """
        self._data['total_reviews'] = value


    @required
    @property
    def reviews_outliers(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['reviews_outliers']


    @reviews_outliers.setter
    def reviews_outliers(self, value: int):
        """
        Default value: ``0``
        """
        self._data['reviews_outliers'] = value


    @required
    @property
    def plagiarized_submissions(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['plagiarized_submissions']


    @plagiarized_submissions.setter
    def plagiarized_submissions(self, value: int):
        """
        Default value: ``0``
        """
        self._data['plagiarized_submissions'] = value


    @required
    @property
    def magic(self) -> str:
        """
        Default value: ``"0"``

        Type: str
        """
        return self._data.setdefault('magic', "0")


    @magic.setter
    def magic(self, value: str):
        """
        Default value: ``"0"``

        Type: str
        """
        self._data['magic'] = value


    @required
    @property
    def discrimination(self) -> str:
        """
        Default value: ``"0"``

        Type: str
        """
        return self._data.setdefault('discrimination', "0")


    @discrimination.setter
    def discrimination(self, value: str):
        """
        Default value: ``"0"``

        Type: str
        """
        self._data['discrimination'] = value


