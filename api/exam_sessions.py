# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class ExamSession:
    _resources_name = 'exam-sessions'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'ExamSession(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model ExamSession are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @readonly
    @property
    def user(self) -> str:
        return self._data['user']


    @required
    @property
    def section(self) -> str:
        return self._data['section']


    @section.setter
    def section(self, value: str):
        self._data['section'] = value


    @required
    @readonly
    @property
    def begin_date(self) -> str:
        """
        Default value: ``"2018-08-26T00:35:19.469Z"``

        Type: str
        """
        return self._data.setdefault('begin_date', "2018-08-26T00:35:19.469Z")




class ListOfExamSessions:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> ExamSession:
        return ExamSession(self._stepik, self._stepik._fetch_object(ExamSession, id))


    def get_all(self, ids: List[int], keep_order=False) -> Iterable[ExamSession]:
        objects = self._stepik._fetch_objects(ExamSession, ids)
        iterable = (ExamSession(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)


    def create(self, section: str) -> ExamSession:
        vars = locals().copy()
        data = {'exam-session': {k: v for k, v in vars.items() if k != 'self' and v is not None}}

        resources_name = 'exam-sessions'
        response = self._stepik._post(resources_name, data)

        if resources_name not in response:
            raise StepikError(response)

        return ExamSession(self._stepik, response[resources_name][0])
