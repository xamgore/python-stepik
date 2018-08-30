# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class Certificate:
    _resources_name = 'certificates'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'Certificate(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model Certificate are missing')


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
    @readonly
    @property
    def course(self) -> str:
        return self._data['course']


    @required
    @readonly
    @property
    def issue_date(self) -> str:
        """
        Default value: ``"2018-08-26T00:35:04.162Z"``

        Type: str
        """
        return self._data.setdefault('issue_date', "2018-08-26T00:35:04.162Z")


    @readonly
    @property
    def update_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('update_date', "None")


    @readonly
    @property
    def grade(self) -> str:
        return self._data['grade']


    @readonly
    @property
    def type(self) -> str:
        return self._data['type']


    @readonly
    @property
    def url(self) -> str:
        return self._data['url']


    @readonly
    @property
    def preview_url(self) -> str:
        return self._data['preview_url']


    @property
    def is_public(self) -> bool:
        """
        Default value: ``True``
        """
        return self._data.setdefault('is_public', True)


    @is_public.setter
    def is_public(self, value: bool):
        """
        Default value: ``True``
        """
        self._data['is_public'] = value


    @readonly
    @property
    def user_rank(self) -> str:
        return self._data['user_rank']


    @readonly
    @property
    def user_rank_max(self) -> str:
        return self._data['user_rank_max']


    @readonly
    @property
    def leaderboard_size(self) -> str:
        return self._data['leaderboard_size']




class ListOfCertificates:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> Certificate:
        return Certificate(self._stepik, self._stepik._fetch_object(Certificate, id))


    def get_all(self, ids: List[int], keep_order=False) -> Iterable[Certificate]:
        objects = self._stepik._fetch_objects(Certificate, ids)
        iterable = (Certificate(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)
