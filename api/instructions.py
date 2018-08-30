# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class Instruction:
    _resources_name = 'instructions'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'Instruction(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model Instruction are missing')


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
    def min_reviews(self) -> int:
        """
        Default value: ``3``
        """
        return self._data.setdefault('min_reviews', 3)


    @min_reviews.setter
    def min_reviews(self, value: int):
        """
        Default value: ``3``
        """
        self._data['min_reviews'] = value


    @property
    def strategy_type(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('strategy_type', "None")


    @strategy_type.setter
    def strategy_type(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self._data['strategy_type'] = value


    @required
    @property
    def rubrics(self) -> str:
        return self._data['rubrics']


    @rubrics.setter
    def rubrics(self, value: str):
        self._data['rubrics'] = value


    @readonly
    @property
    def is_frozen(self) -> bool:
        return self._data['is_frozen']


    @property
    def text(self) -> str:
        return self._data['text']


    @text.setter
    def text(self, value: str):
        self._data['text'] = value




class ListOfInstructions:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> Instruction:
        return Instruction(self._stepik, self._stepik._fetch_object(Instruction, id))


    def get_all(self, ids: List[int], keep_order=False) -> Iterable[Instruction]:
        objects = self._stepik._fetch_objects(Instruction, ids)
        iterable = (Instruction(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)


    def create(self, step: str, min_reviews: int = None, strategy_type: str = None, rubrics: str = None, text: str = None) -> Instruction:
        vars = locals().copy()
        data = {'instruction': {k: v for k, v in vars.items() if k != 'self' and v is not None}}

        resources_name = 'instructions'
        response = self._stepik._post(resources_name, data)

        if resources_name not in response:
            raise StepikError(response)

        return Instruction(self._stepik, response[resources_name][0])


    def delete(self, id: int) -> dict:
        return self._stepik._delete('instructions', id)
