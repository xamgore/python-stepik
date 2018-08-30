# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class SocialAccount:
    _resources_name = 'social-accounts'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'SocialAccount(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model SocialAccount are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @property
    def user(self) -> str:
        return self._data['user']


    @user.setter
    def user(self, value: str):
        self._data['user'] = value


    @required
    @property
    def provider(self) -> str:
        return self._data['provider']


    @provider.setter
    def provider(self, value: str):
        self._data['provider'] = value


    @required
    @property
    def uid(self) -> str:
        return self._data['uid']


    @uid.setter
    def uid(self, value: str):
        self._data['uid'] = value




class ListOfSocialAccounts:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> SocialAccount:
        return SocialAccount(self._stepik, self._stepik._fetch_object(SocialAccount, id))


    def get_all(self, ids: List[int], keep_order=False) -> Iterable[SocialAccount]:
        objects = self._stepik._fetch_objects(SocialAccount, ids)
        iterable = (SocialAccount(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)


    def create(self, provider: str, uid: str, user: str = None) -> SocialAccount:
        vars = locals().copy()
        data = {'social-account': {k: v for k, v in vars.items() if k != 'self' and v is not None}}

        resources_name = 'social-accounts'
        response = self._stepik._post(resources_name, data)

        if resources_name not in response:
            raise StepikError(response)

        return SocialAccount(self._stepik, response[resources_name][0])


    def delete(self, id: int) -> dict:
        return self._stepik._delete('social-accounts', id)
