# This file is generated
from typing import List

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class Review:
    _resources_name = 'reviews'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'Review(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model Review are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @property
    def session(self) -> str:
        return self._data['session']


    @session.setter
    def session(self, value: str):
        self._data['session'] = value


    @property
    def target_session(self) -> str:
        return self._data['target_session']


    @target_session.setter
    def target_session(self, value: str):
        self._data['target_session'] = value


    @property
    def text(self) -> str:
        return self._data['text']


    @text.setter
    def text(self, value: str):
        self._data['text'] = value


    @required
    @property
    def rubric_scores(self) -> str:
        return self._data['rubric_scores']


    @rubric_scores.setter
    def rubric_scores(self, value: str):
        self._data['rubric_scores'] = value


    @readonly
    @property
    def submission(self) -> int:
        return self._data['submission']


    @readonly
    @property
    def when_finished(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('when_finished', "None")


    @readonly
    @property
    def is_verified(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['is_verified']


