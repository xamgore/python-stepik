# This file is generated
from typing import List

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class Rubric:
    _resources_name = 'rubrics'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'Rubric(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model Rubric are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @property
    def instruction(self) -> str:
        return self._data['instruction']


    @instruction.setter
    def instruction(self, value: str):
        self._data['instruction'] = value


    @required
    @property
    def text(self) -> str:
        return self._data['text']


    @text.setter
    def text(self, value: str):
        self._data['text'] = value


    @required
    @property
    def cost(self) -> int:
        return self._data['cost']


    @cost.setter
    def cost(self, value: int):
        self._data['cost'] = value


    @required
    @property
    def position(self) -> int:
        """
        Default value: ``1``
        """
        return self._data.setdefault('position', 1)


    @position.setter
    def position(self, value: int):
        """
        Default value: ``1``
        """
        self._data['position'] = value


