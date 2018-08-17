# This file is generated
from common import required, readonly
from typing import List



class WriteCourseSubscription:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'WriteCourseSubscription(id={self.id!r})'


    @property
    def to_reminders(self) -> bool:
        """
        Default value: True
        """
        return self.__data.setdefault('to_reminders', True)


    @to_reminders.setter
    def to_reminders(self, value: bool):
        """
        Default value: True
        """
        self.__data['to_reminders'] = value


    @property
    def to_announcements(self) -> bool:
        """
        Default value: True
        """
        return self.__data.setdefault('to_announcements', True)


    @to_announcements.setter
    def to_announcements(self, value: bool):
        """
        Default value: True
        """
        self.__data['to_announcements'] = value


    @property
    def to_comments(self) -> bool:
        """
        Default value: True
        """
        return self.__data.setdefault('to_comments', True)


    @to_comments.setter
    def to_comments(self, value: bool):
        """
        Default value: True
        """
        self.__data['to_comments'] = value




class CourseSubscription:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'CourseSubscription(id={self.id!r})'


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @required
    @readonly
    @property
    def user(self) -> str:
        return self.__data['user']


    @required
    @readonly
    @property
    def course(self) -> str:
        return self.__data['course']


    @property
    def to_reminders(self) -> bool:
        """
        Default value: True
        """
        return self.__data.setdefault('to_reminders', True)


    @to_reminders.setter
    def to_reminders(self, value: bool):
        """
        Default value: True
        """
        self.__data['to_reminders'] = value


    @property
    def to_announcements(self) -> bool:
        """
        Default value: True
        """
        return self.__data.setdefault('to_announcements', True)


    @to_announcements.setter
    def to_announcements(self, value: bool):
        """
        Default value: True
        """
        self.__data['to_announcements'] = value


    @property
    def to_comments(self) -> bool:
        """
        Default value: True
        """
        return self.__data.setdefault('to_comments', True)


    @to_comments.setter
    def to_comments(self, value: bool):
        """
        Default value: True
        """
        self.__data['to_comments'] = value


