# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class SocialProfile:
    _resources_name = 'social-profiles'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'SocialProfile(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model SocialProfile are missing')


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
    def provider(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('provider', "None")


    @provider.setter
    def provider(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self._data['provider'] = value


    @required
    @property
    def name(self) -> str:
        return self._data['name']


    @name.setter
    def name(self, value: str):
        self._data['name'] = value


    @readonly
    @property
    def url(self) -> str:
        return self._data['url']




class ListOfSocialProfiles:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> SocialProfile:
        return SocialProfile(self._stepik, self._stepik._fetch_object(SocialProfile, id))


    def get_all(self, ids: List[int], keep_order=False) -> Iterable[SocialProfile]:
        objects = self._stepik._fetch_objects(SocialProfile, ids)
        iterable = (SocialProfile(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)


    def create(self, provider: str, name: str) -> SocialProfile:
        vars = locals().copy()
        data = {'social-profile': {k: v for k, v in vars.items() if k != 'self' and v is not None}}

        resources_name = 'social-profiles'
        response = self._stepik._post(resources_name, data)

        if resources_name not in response:
            raise StepikError(response)

        return SocialProfile(self._stepik, response[resources_name][0])


    def delete(self, id: int) -> dict:
        return self._stepik._delete('social-profiles', id)
