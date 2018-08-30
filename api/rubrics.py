# This file is generated
from typing import List, Iterable, Any

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




class ListOfRubrics:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> Rubric:
        return Rubric(self._stepik, self._stepik._fetch_object(Rubric, id))


    def get_all(self, ids: List[int], keep_order=False) -> Iterable[Rubric]:
        objects = self._stepik._fetch_objects(Rubric, ids)
        iterable = (Rubric(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)


    def create(self, instruction: str, text: str, cost: int, position: int = None) -> Rubric:
        vars = locals().copy()
        data = {'rubric': {k: v for k, v in vars.items() if k != 'self' and v is not None}}

        resources_name = 'rubrics'
        response = self._stepik._post(resources_name, data)

        if resources_name not in response:
            raise StepikError(response)

        return Rubric(self._stepik, response[resources_name][0])


    def delete(self, id: int) -> dict:
        return self._stepik._delete('rubrics', id)
