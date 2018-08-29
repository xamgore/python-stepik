# This file is generated
from typing import List

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class UserCodeRun:
    _resources_name = 'user-code-runs'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'UserCodeRun(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model UserCodeRun are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @property
    def user(self) -> str:
        return self._data['user']


    @user.setter
    def user(self, value: str):
        self._data['user'] = value


    @required
    @property
    def step(self) -> str:
        return self._data['step']


    @step.setter
    def step(self, value: str):
        self._data['step'] = value


    @required
    @property
    def language(self) -> str:
        return self._data['language']


    @language.setter
    def language(self, value: str):
        self._data['language'] = value


    @required
    @property
    def code(self) -> str:
        return self._data['code']


    @code.setter
    def code(self, value: str):
        self._data['code'] = value


    @readonly
    @property
    def status(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('status', "None")


    @required
    @property
    def stdin(self) -> str:
        return self._data['stdin']


    @stdin.setter
    def stdin(self, value: str):
        self._data['stdin'] = value


    @required
    @readonly
    @property
    def stdout(self) -> str:
        return self._data['stdout']


    @required
    @readonly
    @property
    def stderr(self) -> str:
        return self._data['stderr']


    @readonly
    @property
    def time_limit_exceeded(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['time_limit_exceeded']


    @readonly
    @property
    def memory_limit_exceeded(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['memory_limit_exceeded']


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


