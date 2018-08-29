# This file is generated
from typing import List

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class TodoItem:
    _resources_name = 'todo-items'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'TodoItem(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model TodoItem are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @property
    def course(self) -> str:
        return self._data['course']


    @course.setter
    def course(self, value: str):
        self._data['course'] = value


    @required
    @property
    def kind(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('kind', "None")


    @kind.setter
    def kind(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self._data['kind'] = value


    @property
    def is_complete(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['is_complete']


    @is_complete.setter
    def is_complete(self, value: bool):
        """
        Default value: ``False``
        """
        self._data['is_complete'] = value


    @property
    def context(self) -> str:
        """
        Enter a valid JSON object

        Default value: ``{}``
        """
        return self._data['context']


    @context.setter
    def context(self, value: str):
        """
        Enter a valid JSON object

        Default value: ``{}``
        """
        self._data['context'] = value


    @readonly
    @property
    def create_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('create_date', "None")


    @readonly
    @property
    def update_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('update_date', "None")


