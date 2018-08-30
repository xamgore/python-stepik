# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class EmailAddress:
    _resources_name = 'email-addresses'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'EmailAddress(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model EmailAddress are missing')


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
    def email(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('email', "None")


    @email.setter
    def email(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self._data['email'] = value


    @readonly
    @property
    def is_verified(self) -> bool:
        return self._data['is_verified']


    @readonly
    @property
    def is_primary(self) -> bool:
        return self._data['is_primary']




class ListOfEmailAddresses:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> EmailAddress:
        return EmailAddress(self._stepik, self._stepik._fetch_object(EmailAddress, id))


    def get_all(self, ids: List[int], keep_order=False) -> Iterable[EmailAddress]:
        objects = self._stepik._fetch_objects(EmailAddress, ids)
        iterable = (EmailAddress(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)


    def create(self, email: str) -> EmailAddress:
        vars = locals().copy()
        data = {'email-address': {k: v for k, v in vars.items() if k != 'self' and v is not None}}

        resources_name = 'email-addresses'
        response = self._stepik._post(resources_name, data)

        if resources_name not in response:
            raise StepikError(response)

        return EmailAddress(self._stepik, response[resources_name][0])


    def delete(self, id: int) -> dict:
        return self._stepik._delete('email-addresses', id)
