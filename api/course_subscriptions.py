# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class CourseSubscription:
    _resources_name = 'course-subscriptions'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'CourseSubscription(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model CourseSubscription are missing')


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
    @readonly
    @property
    def course(self) -> str:
        return self._data['course']


    @property
    def to_reminders(self) -> bool:
        """
        Default value: ``True``
        """
        return self._data.setdefault('to_reminders', True)


    @to_reminders.setter
    def to_reminders(self, value: bool):
        """
        Default value: ``True``
        """
        self._data['to_reminders'] = value


    @property
    def to_announcements(self) -> bool:
        """
        Default value: ``True``
        """
        return self._data.setdefault('to_announcements', True)


    @to_announcements.setter
    def to_announcements(self, value: bool):
        """
        Default value: ``True``
        """
        self._data['to_announcements'] = value


    @property
    def to_comments(self) -> bool:
        """
        Default value: ``True``
        """
        return self._data.setdefault('to_comments', True)


    @to_comments.setter
    def to_comments(self, value: bool):
        """
        Default value: ``True``
        """
        self._data['to_comments'] = value




class ListOfCourseSubscriptions:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> CourseSubscription:
        return CourseSubscription(self._stepik, self._stepik._fetch_object(CourseSubscription, id))


    def get_all(self, ids: List[int], keep_order=False) -> Iterable[CourseSubscription]:
        objects = self._stepik._fetch_objects(CourseSubscription, ids)
        iterable = (CourseSubscription(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)
