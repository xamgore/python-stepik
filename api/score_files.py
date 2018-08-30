# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class ScoreFile:
    _resources_name = 'score-files'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'ScoreFile(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model ScoreFile are missing')


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


    @required
    @property
    def file(self) -> str:
        return self._data['file']


    @file.setter
    def file(self, value: str):
        self._data['file'] = value


    @readonly
    @property
    def error(self) -> str:
        return self._data['error']


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
    def process_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('process_date', "None")




class ListOfScoreFiles:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> ScoreFile:
        return ScoreFile(self._stepik, self._stepik._fetch_object(ScoreFile, id))


    def get_all(self, ids: List[int], keep_order=False) -> Iterable[ScoreFile]:
        objects = self._stepik._fetch_objects(ScoreFile, ids)
        iterable = (ScoreFile(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)


    def create(self, session: str, file: str) -> ScoreFile:
        vars = locals().copy()
        data = {'score-file': {k: v for k, v in vars.items() if k != 'self' and v is not None}}

        resources_name = 'score-files'
        response = self._stepik._post(resources_name, data)

        if resources_name not in response:
            raise StepikError(response)

        return ScoreFile(self._stepik, response[resources_name][0])
