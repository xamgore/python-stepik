# This file is generated
from common import required, readonly
from typing import List


class WriteAnnouncement:
    def __init__(self, data):
        self.__data = data


    @property
    def course(self) -> str:
        return self.__data['course']


    @course.setter
    def course(self, value: str):
        self.__data['course'] = value


    @property
    def user(self) -> str:
        return self.__data['user']


    @user.setter
    def user(self, value: str):
        self.__data['user'] = value


    @required
    @property
    def subject(self) -> str:
        return self.__data['subject']


    @subject.setter
    def subject(self, value: str):
        self.__data['subject'] = value


    @required
    @property
    def text(self) -> str:
        return self.__data['text']


    @text.setter
    def text(self, value: str):
        self.__data['text'] = value


    @property
    def is_restricted_by_score(self) -> bool:
        """
        default value: False
        """
        return self.__data['is_restricted_by_score']


    @is_restricted_by_score.setter
    def is_restricted_by_score(self, value: bool):
        """
        default value: False
        """
        self.__data['is_restricted_by_score'] = value


    @required
    @property
    def score_percent_min(self) -> int:
        """
        default value: 0
        """
        return self.__data['score_percent_min']


    @score_percent_min.setter
    def score_percent_min(self, value: int):
        """
        default value: 0
        """
        self.__data['score_percent_min'] = value


    @required
    @property
    def score_percent_max(self) -> int:
        """
        default value: 100
        """
        return self.__data.setdefault('score_percent_max', 100)


    @score_percent_max.setter
    def score_percent_max(self, value: int):
        """
        default value: 100
        """
        self.__data['score_percent_max'] = value


    @property
    def email_template(self) -> str:
        return self.__data['email_template']


    @email_template.setter
    def email_template(self, value: str):
        self.__data['email_template'] = value


    @property
    def is_scheduled(self) -> bool:
        """
        default value: False
        """
        return self.__data['is_scheduled']


    @is_scheduled.setter
    def is_scheduled(self, value: bool):
        """
        default value: False
        """
        self.__data['is_scheduled'] = value


    @property
    def start_date(self) -> str:
        """
        Type: datetime
        """
        return self.__data['start_date']


    @start_date.setter
    def start_date(self, value: str):
        """
        Type: datetime
        """
        self.__data['start_date'] = value


    @required
    @property
    def mail_period_days(self) -> int:
        """
        default value: 7
        """
        return self.__data.setdefault('mail_period_days', 7)


    @mail_period_days.setter
    def mail_period_days(self, value: int):
        """
        default value: 7
        """
        self.__data['mail_period_days'] = value


    @required
    @property
    def mail_quantity(self) -> int:
        """
        default value: 1
        """
        return self.__data.setdefault('mail_quantity', 1)


    @mail_quantity.setter
    def mail_quantity(self, value: int):
        """
        default value: 1
        """
        self.__data['mail_quantity'] = value


    @property
    def is_infinite(self) -> bool:
        """
        default value: False
        """
        return self.__data['is_infinite']


    @is_infinite.setter
    def is_infinite(self, value: bool):
        """
        default value: False
        """
        self.__data['is_infinite'] = value


    @property
    def on_enroll(self) -> bool:
        """
        default value: False
        """
        return self.__data['on_enroll']


    @on_enroll.setter
    def on_enroll(self, value: bool):
        """
        default value: False
        """
        self.__data['on_enroll'] = value


class Announcement:
    def __init__(self, data):
        self.__data = data


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @property
    def course(self) -> str:
        return self.__data['course']


    @course.setter
    def course(self, value: str):
        self.__data['course'] = value


    @property
    def user(self) -> str:
        return self.__data['user']


    @user.setter
    def user(self, value: str):
        self.__data['user'] = value


    @required
    @property
    def subject(self) -> str:
        return self.__data['subject']


    @subject.setter
    def subject(self, value: str):
        self.__data['subject'] = value


    @required
    @property
    def text(self) -> str:
        return self.__data['text']


    @text.setter
    def text(self, value: str):
        self.__data['text'] = value


    @readonly
    @property
    def create_date(self) -> str:
        """
        Type: datetime
        """
        return self.__data['create_date']


    @readonly
    @property
    def next_date(self) -> str:
        """
        Type: datetime
        """
        return self.__data['next_date']


    @readonly
    @property
    def sent_date(self) -> str:
        """
        Type: datetime
        """
        return self.__data['sent_date']


    @readonly
    @property
    def status(self) -> str:
        """
        Type: choice
        """
        return self.__data['status']


    @property
    def is_restricted_by_score(self) -> bool:
        """
        default value: False
        """
        return self.__data['is_restricted_by_score']


    @is_restricted_by_score.setter
    def is_restricted_by_score(self, value: bool):
        """
        default value: False
        """
        self.__data['is_restricted_by_score'] = value


    @required
    @property
    def score_percent_min(self) -> int:
        """
        default value: 0
        """
        return self.__data['score_percent_min']


    @score_percent_min.setter
    def score_percent_min(self, value: int):
        """
        default value: 0
        """
        self.__data['score_percent_min'] = value


    @required
    @property
    def score_percent_max(self) -> int:
        """
        default value: 100
        """
        return self.__data.setdefault('score_percent_max', 100)


    @score_percent_max.setter
    def score_percent_max(self, value: int):
        """
        default value: 100
        """
        self.__data['score_percent_max'] = value


    @property
    def email_template(self) -> str:
        return self.__data['email_template']


    @email_template.setter
    def email_template(self, value: str):
        self.__data['email_template'] = value


    @property
    def is_scheduled(self) -> bool:
        """
        default value: False
        """
        return self.__data['is_scheduled']


    @is_scheduled.setter
    def is_scheduled(self, value: bool):
        """
        default value: False
        """
        self.__data['is_scheduled'] = value


    @property
    def start_date(self) -> str:
        """
        Type: datetime
        """
        return self.__data['start_date']


    @start_date.setter
    def start_date(self, value: str):
        """
        Type: datetime
        """
        self.__data['start_date'] = value


    @required
    @property
    def mail_period_days(self) -> int:
        """
        default value: 7
        """
        return self.__data.setdefault('mail_period_days', 7)


    @mail_period_days.setter
    def mail_period_days(self, value: int):
        """
        default value: 7
        """
        self.__data['mail_period_days'] = value


    @required
    @property
    def mail_quantity(self) -> int:
        """
        default value: 1
        """
        return self.__data.setdefault('mail_quantity', 1)


    @mail_quantity.setter
    def mail_quantity(self, value: int):
        """
        default value: 1
        """
        self.__data['mail_quantity'] = value


    @property
    def is_infinite(self) -> bool:
        """
        default value: False
        """
        return self.__data['is_infinite']


    @is_infinite.setter
    def is_infinite(self, value: bool):
        """
        default value: False
        """
        self.__data['is_infinite'] = value


    @property
    def on_enroll(self) -> bool:
        """
        default value: False
        """
        return self.__data['on_enroll']


    @on_enroll.setter
    def on_enroll(self, value: bool):
        """
        default value: False
        """
        self.__data['on_enroll'] = value


    @required
    @readonly
    @property
    def publish_count(self) -> int:
        """
        default value: 0
        """
        return self.__data['publish_count']


    @required
    @readonly
    @property
    def queue_count(self) -> int:
        """
        default value: 0
        """
        return self.__data['queue_count']


    @required
    @readonly
    @property
    def sent_count(self) -> int:
        """
        default value: 0
        """
        return self.__data['sent_count']


    @required
    @readonly
    @property
    def open_count(self) -> int:
        """
        default value: 0
        """
        return self.__data['open_count']


    @required
    @readonly
    @property
    def click_count(self) -> int:
        """
        default value: 0
        """
        return self.__data['click_count']


    @readonly
    @property
    def estimated_start_date(self) -> str:
        return self.__data['estimated_start_date']


    @readonly
    @property
    def estimated_finish_date(self) -> str:
        return self.__data['estimated_finish_date']


    @readonly
    @property
    def notice_dates(self) -> str:
        return self.__data['notice_dates']


