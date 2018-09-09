# This file is generated
from typing import List, Iterable, Any, Optional

from stepik.errors import StepikError
from stepik.common import required, readonly
from stepik.resources_list import ResourcesList


class UserLicense:
    _resources_name = 'licenses'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'UserLicense(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model UserLicense are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @readonly
    @property
    def activation_code(self) -> str:
        return self._data['activation_code']


    @readonly
    @property
    def expire_date(self) -> str:
        return self._data['expire_date']


    @readonly
    @property
    def is_personal(self) -> str:
        return self._data['is_personal']


    @required
    @readonly
    @property
    def user(self) -> str:
        return self._data['user']




class ListOfLicenses:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> UserLicense:
        obj = self._stepik._fetch_object(UserLicense, id)
        return UserLicense(self._stepik, obj)

