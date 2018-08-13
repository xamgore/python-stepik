# This file is generated
from common import required, readonly
from typing import List


class WriteLesson:
    def __init__(self, data):
        self.__data = data


    @required
    @property
    def steps(self) -> str:
        return self.__data['steps']


    @steps.setter
    def steps(self, value: str):
        self.__data['steps'] = value


    @property
    def cover_url(self) -> str:
        """
        Type: url
        """
        return self.__data['cover_url']


    @cover_url.setter
    def cover_url(self, value: str):
        """
        Type: url
        """
        self.__data['cover_url'] = value


    @property
    def is_comments_enabled(self) -> bool:
        """
        default value: True
        """
        return self.__data.setdefault('is_comments_enabled', True)


    @is_comments_enabled.setter
    def is_comments_enabled(self, value: bool):
        """
        default value: True
        """
        self.__data['is_comments_enabled'] = value


    @required
    @property
    def language(self) -> str:
        """
        default value: "en"
        """
        return self.__data.setdefault('language', "en")


    @language.setter
    def language(self, value: str):
        """
        default value: "en"
        """
        self.__data['language'] = value


    @property
    def is_public(self) -> bool:
        return self.__data['is_public']


    @is_public.setter
    def is_public(self, value: bool):
        self.__data['is_public'] = value


    @required
    @property
    def title(self) -> str:
        return self.__data['title']


    @title.setter
    def title(self, value: str):
        self.__data['title'] = value


    @property
    def lti_consumer_key(self) -> str:
        return self.__data['lti_consumer_key']


    @lti_consumer_key.setter
    def lti_consumer_key(self, value: str):
        self.__data['lti_consumer_key'] = value


    @property
    def lti_secret_key(self) -> str:
        return self.__data['lti_secret_key']


    @lti_secret_key.setter
    def lti_secret_key(self, value: str):
        self.__data['lti_secret_key'] = value


class Lesson:
    def __init__(self, data):
        self.__data = data


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @required
    @property
    def steps(self) -> str:
        return self.__data['steps']


    @steps.setter
    def steps(self, value: str):
        self.__data['steps'] = value


    @readonly
    @property
    def actions(self) -> str:
        return self.__data['actions']


    @readonly
    @property
    def progress(self) -> str:
        return self.__data['progress']


    @readonly
    @property
    def subscriptions(self) -> str:
        return self.__data['subscriptions']


    @readonly
    @property
    def viewed_by(self) -> str:
        return self.__data['viewed_by']


    @readonly
    @property
    def passed_by(self) -> str:
        return self.__data['passed_by']


    @readonly
    @property
    def time_to_complete(self) -> str:
        return self.__data['time_to_complete']


    @property
    def cover_url(self) -> str:
        """
        Type: url
        """
        return self.__data['cover_url']


    @cover_url.setter
    def cover_url(self, value: str):
        """
        Type: url
        """
        self.__data['cover_url'] = value


    @property
    def is_comments_enabled(self) -> bool:
        """
        default value: True
        """
        return self.__data.setdefault('is_comments_enabled', True)


    @is_comments_enabled.setter
    def is_comments_enabled(self, value: bool):
        """
        default value: True
        """
        self.__data['is_comments_enabled'] = value


    @readonly
    @property
    def owner(self) -> str:
        return self.__data['owner']


    @required
    @property
    def language(self) -> str:
        """
        default value: "en"
        """
        return self.__data.setdefault('language', "en")


    @language.setter
    def language(self, value: str):
        """
        default value: "en"
        """
        self.__data['language'] = value


    @readonly
    @property
    def is_featured(self) -> bool:
        """
        default value: False
        """
        return self.__data['is_featured']


    @property
    def is_public(self) -> bool:
        return self.__data['is_public']


    @is_public.setter
    def is_public(self, value: bool):
        self.__data['is_public'] = value


    @required
    @property
    def title(self) -> str:
        return self.__data['title']


    @title.setter
    def title(self, value: str):
        self.__data['title'] = value


    @readonly
    @property
    def slug(self) -> str:
        return self.__data['slug']


    @readonly
    @property
    def create_date(self) -> str:
        """
        Type: datetime
        """
        return self.__data['create_date']


    @readonly
    @property
    def update_date(self) -> str:
        """
        Type: datetime
        """
        return self.__data['update_date']


    @readonly
    @property
    def learners_group(self) -> str:
        return self.__data['learners_group']


    @readonly
    @property
    def testers_group(self) -> str:
        return self.__data['testers_group']


    @readonly
    @property
    def moderators_group(self) -> str:
        return self.__data['moderators_group']


    @readonly
    @property
    def teachers_group(self) -> str:
        return self.__data['teachers_group']


    @readonly
    @property
    def admins_group(self) -> str:
        return self.__data['admins_group']


    @readonly
    @property
    def discussions_count(self) -> str:
        return self.__data['discussions_count']


    @readonly
    @property
    def discussion_proxy(self) -> str:
        return self.__data['discussion_proxy']


    @readonly
    @property
    def discussion_threads(self) -> str:
        return self.__data['discussion_threads']


    @readonly
    @property
    def epic_count(self) -> int:
        return self.__data['epic_count']


    @readonly
    @property
    def abuse_count(self) -> int:
        return self.__data['abuse_count']


    @readonly
    @property
    def vote(self) -> str:
        return self.__data['vote']


    @property
    def lti_consumer_key(self) -> str:
        return self.__data['lti_consumer_key']


    @lti_consumer_key.setter
    def lti_consumer_key(self, value: str):
        self.__data['lti_consumer_key'] = value


    @property
    def lti_secret_key(self) -> str:
        return self.__data['lti_secret_key']


    @lti_secret_key.setter
    def lti_secret_key(self, value: str):
        self.__data['lti_secret_key'] = value


