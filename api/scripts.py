# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class Script:
    _resources_name = 'scripts'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'Script(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model Script are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @property
    def code(self) -> str:
        return self._data['code']


    @code.setter
    def code(self, value: str):
        self._data['code'] = value


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
    def status(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('status', "None")




class ListOfScripts:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> Script:
        return Script(self._stepik, self._stepik._fetch_object(Script, id))


    def create(self, code: str) -> Script:
        vars = locals().copy()
        data = {'script': {k: v for k, v in vars.items() if k != 'self' and v is not None}}

        resources_name = 'scripts'
        response = self._stepik._post(resources_name, data)

        if resources_name not in response:
            raise StepikError(response)

        return Script(self._stepik, response[resources_name][0])
