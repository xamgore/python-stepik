# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class Device:
    _resources_name = 'devices'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'Device(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model Device are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @property
    def registration_id(self) -> str:
        return self._data['registration_id']


    @registration_id.setter
    def registration_id(self, value: str):
        self._data['registration_id'] = value


    @required
    @readonly
    @property
    def user(self) -> str:
        return self._data['user']


    @required
    @property
    def description(self) -> str:
        return self._data['description']


    @description.setter
    def description(self, value: str):
        self._data['description'] = value


    @required
    @property
    def client_type(self) -> str:
        """
        Default value: ``"ios"``

        Type: str
        """
        return self._data.setdefault('client_type', "ios")


    @client_type.setter
    def client_type(self, value: str):
        """
        Default value: ``"ios"``

        Type: str
        """
        self._data['client_type'] = value


    @property
    def is_badges_enabled(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['is_badges_enabled']


    @is_badges_enabled.setter
    def is_badges_enabled(self, value: bool):
        """
        Default value: ``False``
        """
        self._data['is_badges_enabled'] = value




class ListOfDevices:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> Device:
        return Device(self._stepik, self._stepik._fetch_object(Device, id))


    def get_all(self, ids: List[int], keep_order=False) -> Iterable[Device]:
        objects = self._stepik._fetch_objects(Device, ids)
        iterable = (Device(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)


    def create(self, registration_id: str, description: str, client_type: str = None, is_badges_enabled: bool = None) -> Device:
        vars = locals().copy()
        data = {'device': {k: v for k, v in vars.items() if k != 'self' and v is not None}}

        resources_name = 'devices'
        response = self._stepik._post(resources_name, data)

        if resources_name not in response:
            raise StepikError(response)

        return Device(self._stepik, response[resources_name][0])


    def delete(self, id: int) -> dict:
        return self._stepik._delete('devices', id)
