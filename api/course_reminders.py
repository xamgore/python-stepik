# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class CourseReminder:
    _resources_name = 'course-reminders'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'CourseReminder(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model CourseReminder are missing')


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
    def course(self) -> str:
        return self._data['course']


    @course.setter
    def course(self, value: str):
        self._data['course'] = value


    @readonly
    @property
    def create_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('create_date', "None")


    @property
    def is_active(self) -> bool:
        """
        Default value: ``True``
        """
        return self._data.setdefault('is_active', True)


    @is_active.setter
    def is_active(self, value: bool):
        """
        Default value: ``True``
        """
        self._data['is_active'] = value


    @readonly
    @property
    def payload(self) -> str:
        return self._data['payload']




class ListOfCourseReminders:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> CourseReminder:
        return CourseReminder(self._stepik, self._stepik._fetch_object(CourseReminder, id))


    def get_all(self, ids: List[int], keep_order=False) -> Iterable[CourseReminder]:
        objects = self._stepik._fetch_objects(CourseReminder, ids)
        iterable = (CourseReminder(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)


    def create(self, course: str, is_active: bool = None) -> CourseReminder:
        vars = locals().copy()
        data = {'course-reminder': {k: v for k, v in vars.items() if k != 'self' and v is not None}}

        resources_name = 'course-reminders'
        response = self._stepik._post(resources_name, data)

        if resources_name not in response:
            raise StepikError(response)

        return CourseReminder(self._stepik, response[resources_name][0])


    def delete(self, id: int) -> dict:
        return self._stepik._delete('course-reminders', id)
