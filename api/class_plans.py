# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class ClassPlan:
    _resources_name = 'class-plans'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'ClassPlan(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model ClassPlan are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @property
    def user(self) -> str:
        return self._data['user']


    @user.setter
    def user(self, value: str):
        self._data['user'] = value


    @required
    @property
    def allowed_students_count(self) -> int:
        return self._data['allowed_students_count']


    @allowed_students_count.setter
    def allowed_students_count(self, value: int):
        self._data['allowed_students_count'] = value


    @required
    @property
    def students_count(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['students_count']


    @students_count.setter
    def students_count(self, value: int):
        """
        Default value: ``0``
        """
        self._data['students_count'] = value


    @readonly
    @property
    def is_access_restricted(self) -> str:
        return self._data['is_access_restricted']




class ListOfClassPlans:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> ClassPlan:
        return ClassPlan(self._stepik, self._stepik._fetch_object(ClassPlan, id))


    def get_all(self, ids: List[int], keep_order=False) -> Iterable[ClassPlan]:
        objects = self._stepik._fetch_objects(ClassPlan, ids)
        iterable = (ClassPlan(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)
