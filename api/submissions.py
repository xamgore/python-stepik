# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class Submission:
    _resources_name = 'submissions'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'Submission(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model Submission are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @readonly
    @property
    def status(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('status', "None")


    @required
    @readonly
    @property
    def score(self) -> str:
        """
        Default value: ``"0"``

        Type: str
        """
        return self._data.setdefault('score', "0")


    @readonly
    @property
    def hint(self) -> str:
        return self._data['hint']


    @readonly
    @property
    def feedback(self) -> str:
        return self._data['feedback']


    @readonly
    @property
    def time(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('time', "None")


    @property
    def reply(self) -> str:
        """
        Default value: ``{}``
        """
        return self._data['reply']


    @reply.setter
    def reply(self, value: str):
        """
        Default value: ``{}``
        """
        self._data['reply'] = value


    @readonly
    @property
    def reply_url(self) -> str:
        return self._data['reply_url']


    @required
    @property
    def attempt(self) -> str:
        return self._data['attempt']


    @attempt.setter
    def attempt(self, value: str):
        self._data['attempt'] = value


    @required
    @readonly
    @property
    def session(self) -> str:
        return self._data['session']


    @readonly
    @property
    def eta(self) -> int:
        return self._data['eta']




class ListOfSubmissions:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> Submission:
        return Submission(self._stepik, self._stepik._fetch_object(Submission, id))


    def get_all(self, ids: List[int], keep_order=False) -> Iterable[Submission]:
        objects = self._stepik._fetch_objects(Submission, ids)
        iterable = (Submission(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)


    def create(self, attempt: str, reply: str = None) -> Submission:
        vars = locals().copy()
        data = {'submission': {k: v for k, v in vars.items() if k != 'self' and v is not None}}

        resources_name = 'submissions'
        response = self._stepik._post(resources_name, data)

        if resources_name not in response:
            raise StepikError(response)

        return Submission(self._stepik, response[resources_name][0])
