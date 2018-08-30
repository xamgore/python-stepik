# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class Member:
    _resources_name = 'members'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'Member(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model Member are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @property
    def group(self) -> str:
        return self._data['group']


    @group.setter
    def group(self, value: str):
        self._data['group'] = value


    @property
    def user(self) -> str:
        return self._data['user']


    @user.setter
    def user(self, value: str):
        self._data['user'] = value


    @required
    @readonly
    @property
    def date_joined(self) -> str:
        """
        Default value: ``"2018-08-26T00:35:27.146Z"``

        Type: str
        """
        return self._data.setdefault('date_joined', "2018-08-26T00:35:27.146Z")


    @property
    def is_synced(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['is_synced']


    @is_synced.setter
    def is_synced(self, value: bool):
        """
        Default value: ``False``
        """
        self._data['is_synced'] = value




class ListOfMembers:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> Member:
        return Member(self._stepik, self._stepik._fetch_object(Member, id))


    def get_all(self, ids: List[int], keep_order=False) -> Iterable[Member]:
        objects = self._stepik._fetch_objects(Member, ids)
        iterable = (Member(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)


    def create(self, group: str, user: str = None, is_synced: bool = None) -> Member:
        vars = locals().copy()
        data = {'member': {k: v for k, v in vars.items() if k != 'self' and v is not None}}

        resources_name = 'members'
        response = self._stepik._post(resources_name, data)

        if resources_name not in response:
            raise StepikError(response)

        return Member(self._stepik, response[resources_name][0])


    def delete(self, id: int) -> dict:
        return self._stepik._delete('members', id)
