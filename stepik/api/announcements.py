# This file is generated
from typing import List, Iterable, Any, Optional

from stepik.errors import StepikError
from stepik.common import required, readonly
from stepik.resources_list import ResourcesList


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
        obj = self._stepik._fetch_object(Announcement, id)
        return Announcement(self._stepik, obj)


    def get_all(self, ids: Iterable[int], keep_order=False) -> Iterable[Announcement]:
        """
        Grab a bunch of ids, usually 20 objects per request.
        """
        if keep_order:
            ids = list(ids)

        objects = self._stepik._fetch_objects(Announcement, ids)
        iterable = (Announcement(self._stepik, o) for o in objects)

        return iterable if not keep_order \
            else sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))


    def iterate(self,
                skip: int = 0, limit: Optional[int] = 20) -> Iterable[Announcement]:
        """
        There are base fields, like ``language``, that can be used to filter out
        objects. Also there are ordering fields, that starts with ``by_`` prefix.
        They are not used in queries if their value is ``None``. If ``True``
        objects are sorted in straight order, if ``False`` in reversed.
        The sorting is done on the server side, there is no guarantees will it be
        in ascending or descending order.

        ``skip`` parameter means how much objects to skip from the beginning.

        ``limit`` means how much objects to take. It can be set to ``None``,
        all objects will be fetched (not recommended, actually).
        """

        assert skip >= 0, 'skip must be positive'
        assert limit is None or limit >= 0, 'limit must be positive'

        vars = locals().copy()
        args, order = [], []

        for k, v in vars.items():
            is_ordering = k.startswith('by_')
            is_special = k in ['self', 'skip']

            if not v is None and not is_ordering and not is_special:
                args.append((k, v))

            if not v is None and is_ordering:
                sign = '-' if v else ''
                order.append(sign + k[3:])

        from urllib.parse import urlencode
        params = urlencode(args, doseq=True)
        ordering = ','.join(order)

        skip = 0 if skip is None else skip
        page_idx, count = divmod(skip, 20)
        page_idx += 1  # stepik counts from 1

        while True:
            page = self._stepik._get(f'announcements?{params}&page={page_idx}&order={ordering}')

            for obj in page['announcements']:
                if limit and count >= limit:
                    break

                yield Announcement(self._stepik, obj)
                count += 1

            if not page['meta']['has_next']:
                break

            page_idx += 1


    def __iter__(self):
        yield from self.iterate(limit=None)


    def create(self,
               subject: str,
               text: str,
               course: str = None,
               user: str = None,
               is_restricted_by_score: bool = None,
               score_percent_min: int = None,
               score_percent_max: int = None,
               email_template: str = None,
               is_scheduled: bool = None,
               start_date: str = None,
               mail_period_days: int = None,
               mail_quantity: int = None,
               is_infinite: bool = None,
               on_enroll: bool = None,
               **kwargs) -> Announcement:
        vars = locals().copy()
        data = {'announcement':
                    {k: v for k, v in {**vars, **kwargs}.items()
                     if k != 'self' and v is not None}}

        response = self._stepik._post('announcements', data)
        if 'announcements' not in response:
            raise StepikError(response)

        return Announcement(self._stepik, response['announcements'][0])


    def delete(self, id: int) -> dict:
        """Delete the object by its id. Returns the server's response"""
        return self._stepik._delete('announcements', id)


    def update(self, obj: Announcement) -> Announcement:
        required = ['subject', 'text', 'course', 'user', 'is_restricted_by_score', 'score_percent_min', 'score_percent_max', 'email_template', 'is_scheduled', 'start_date', 'mail_period_days', 'mail_quantity', 'is_infinite', 'on_enroll']
        vars = obj._data
        data = {'announcement':
                    {k: v for k, v in vars.items()
                     if k != 'self' and v is not None and k in required }}

        response = self._stepik._put(f'announcements/{ obj.id }', data)
        if 'announcements' not in response:
            raise StepikError(response)

        return Announcement(self._stepik, response['announcements'][0])

