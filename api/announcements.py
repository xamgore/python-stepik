# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class Announcement:
    _resources_name = 'announcements'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'Announcement(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model Announcement are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @property
    def course(self) -> str:
        return self._data['course']


    @course.setter
    def course(self, value: str):
        self._data['course'] = value


    @property
    def user(self) -> str:
        return self._data['user']


    @user.setter
    def user(self, value: str):
        self._data['user'] = value


    @required
    @property
    def subject(self) -> str:
        return self._data['subject']


    @subject.setter
    def subject(self, value: str):
        self._data['subject'] = value


    @required
    @property
    def text(self) -> str:
        return self._data['text']


    @text.setter
    def text(self, value: str):
        self._data['text'] = value


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
    def next_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('next_date', "None")


    @readonly
    @property
    def sent_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('sent_date', "None")


    @readonly
    @property
    def status(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('status', "None")


    @property
    def is_restricted_by_score(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['is_restricted_by_score']


    @is_restricted_by_score.setter
    def is_restricted_by_score(self, value: bool):
        """
        Default value: ``False``
        """
        self._data['is_restricted_by_score'] = value


    @required
    @property
    def score_percent_min(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['score_percent_min']


    @score_percent_min.setter
    def score_percent_min(self, value: int):
        """
        Default value: ``0``
        """
        self._data['score_percent_min'] = value


    @required
    @property
    def score_percent_max(self) -> int:
        """
        Default value: ``100``
        """
        return self._data.setdefault('score_percent_max', 100)


    @score_percent_max.setter
    def score_percent_max(self, value: int):
        """
        Default value: ``100``
        """
        self._data['score_percent_max'] = value


    @property
    def email_template(self) -> str:
        return self._data['email_template']


    @email_template.setter
    def email_template(self, value: str):
        self._data['email_template'] = value


    @property
    def is_scheduled(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['is_scheduled']


    @is_scheduled.setter
    def is_scheduled(self, value: bool):
        """
        Default value: ``False``
        """
        self._data['is_scheduled'] = value


    @property
    def start_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('start_date', "None")


    @start_date.setter
    def start_date(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self._data['start_date'] = value


    @required
    @property
    def mail_period_days(self) -> int:
        """
        Default value: ``7``
        """
        return self._data.setdefault('mail_period_days', 7)


    @mail_period_days.setter
    def mail_period_days(self, value: int):
        """
        Default value: ``7``
        """
        self._data['mail_period_days'] = value


    @required
    @property
    def mail_quantity(self) -> int:
        """
        Default value: ``1``
        """
        return self._data.setdefault('mail_quantity', 1)


    @mail_quantity.setter
    def mail_quantity(self, value: int):
        """
        Default value: ``1``
        """
        self._data['mail_quantity'] = value


    @property
    def is_infinite(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['is_infinite']


    @is_infinite.setter
    def is_infinite(self, value: bool):
        """
        Default value: ``False``
        """
        self._data['is_infinite'] = value


    @property
    def on_enroll(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['on_enroll']


    @on_enroll.setter
    def on_enroll(self, value: bool):
        """
        Default value: ``False``
        """
        self._data['on_enroll'] = value


    @required
    @readonly
    @property
    def publish_count(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['publish_count']


    @required
    @readonly
    @property
    def queue_count(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['queue_count']


    @required
    @readonly
    @property
    def sent_count(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['sent_count']


    @required
    @readonly
    @property
    def open_count(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['open_count']


    @required
    @readonly
    @property
    def click_count(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['click_count']


    @readonly
    @property
    def estimated_start_date(self) -> str:
        return self._data['estimated_start_date']


    @readonly
    @property
    def estimated_finish_date(self) -> str:
        return self._data['estimated_finish_date']


    @readonly
    @property
    def notice_dates(self) -> str:
        return self._data['notice_dates']




class ListOfAnnouncements:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> Announcement:
        return Announcement(self._stepik, self._stepik._fetch_object(Announcement, id))


    def get_all(self, ids: List[int], keep_order=False) -> Iterable[Announcement]:
        objects = self._stepik._fetch_objects(Announcement, ids)
        iterable = (Announcement(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)


    def create(self, subject: str, text: str, course: str = None, user: str = None, is_restricted_by_score: bool = None, score_percent_min: int = None, score_percent_max: int = None, email_template: str = None, is_scheduled: bool = None, start_date: str = None, mail_period_days: int = None, mail_quantity: int = None, is_infinite: bool = None, on_enroll: bool = None) -> Announcement:
        vars = locals().copy()
        data = {'announcement': {k: v for k, v in vars.items() if k != 'self' and v is not None}}

        resources_name = 'announcements'
        response = self._stepik._post(resources_name, data)

        if resources_name not in response:
            raise StepikError(response)

        return Announcement(self._stepik, response[resources_name][0])


    def delete(self, id: int) -> dict:
        return self._stepik._delete('announcements', id)
