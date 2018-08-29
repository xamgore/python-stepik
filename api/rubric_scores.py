# This file is generated
from typing import List

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class RubricScore:
    _resources_name = 'rubric-scores'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'RubricScore(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model RubricScore are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @readonly
    @property
    def review(self) -> str:
        return self._data['review']


    @required
    @readonly
    @property
    def rubric(self) -> str:
        return self._data['rubric']


    @required
    @property
    def score(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['score']


    @score.setter
    def score(self, value: int):
        """
        Default value: ``0``
        """
        self._data['score'] = value


    @property
    def text(self) -> str:
        return self._data['text']


    @text.setter
    def text(self, value: str):
        self._data['text'] = value


