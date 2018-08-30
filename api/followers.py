# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class Follower:
    _resources_name = 'followers'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'Follower(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model Follower are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @property
    def followee(self) -> str:
        return self._data['followee']


    @followee.setter
    def followee(self, value: str):
        self._data['followee'] = value


    @required
    @readonly
    @property
    def user(self) -> str:
        return self._data['user']


    @required
    @readonly
    @property
    def date_joined(self) -> str:
        """
        Default value: ``"2018-08-26T00:35:20.667Z"``

        Type: str
        """
        return self._data.setdefault('date_joined', "2018-08-26T00:35:20.667Z")




class ListOfFollowers:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> Follower:
        return Follower(self._stepik, self._stepik._fetch_object(Follower, id))


    def get_all(self, ids: List[int], keep_order=False) -> Iterable[Follower]:
        objects = self._stepik._fetch_objects(Follower, ids)
        iterable = (Follower(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)


    def create(self, followee: str) -> Follower:
        vars = locals().copy()
        data = {'follower': {k: v for k, v in vars.items() if k != 'self' and v is not None}}

        resources_name = 'followers'
        response = self._stepik._post(resources_name, data)

        if resources_name not in response:
            raise StepikError(response)

        return Follower(self._stepik, response[resources_name][0])


    def delete(self, id: int) -> dict:
        return self._stepik._delete('followers', id)
