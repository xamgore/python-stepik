# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class Class:
    _resources_name = 'classes'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'Class(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model Class are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @property
    def course(self) -> str:
        return self._data['course']


    @course.setter
    def course(self, value: str):
        self._data['course'] = value


    @required
    @readonly
    @property
    def owner(self) -> str:
        return self._data['owner']


    @property
    def title(self) -> str:
        return self._data['title']


    @title.setter
    def title(self, value: str):
        self._data['title'] = value


    @property
    def description(self) -> str:
        return self._data['description']


    @description.setter
    def description(self, value: str):
        self._data['description'] = value


    @required
    @readonly
    @property
    def invitation_key(self) -> str:
        return self._data['invitation_key']


    @readonly
    @property
    def is_access_restricted(self) -> str:
        return self._data['is_access_restricted']


    @readonly
    @property
    def actions(self) -> str:
        return self._data['actions']


    @readonly
    @property
    def create_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('create_date', "None")


    @readonly
    @property
    def update_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('update_date', "None")




class ListOfClasses:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> Class:
        return Class(self._stepik, self._stepik._fetch_object(Class, id))


    def get_all(self, ids: List[int], keep_order=False) -> Iterable[Class]:
        objects = self._stepik._fetch_objects(Class, ids)
        iterable = (Class(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)


    def create(self, course: str, title: str = None, description: str = None) -> Class:
        vars = locals().copy()
        data = {'class': {k: v for k, v in vars.items() if k != 'self' and v is not None}}

        resources_name = 'classes'
        response = self._stepik._post(resources_name, data)

        if resources_name not in response:
            raise StepikError(response)

        return Class(self._stepik, response[resources_name][0])


    def delete(self, id: int) -> dict:
        return self._stepik._delete('classes', id)
