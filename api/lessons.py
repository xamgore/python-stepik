# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class WriteLesson:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'WriteLesson(id={self.id!r})'


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
        Default value: ``True``
        """
        return self.__data.setdefault('is_comments_enabled', True)


    @is_comments_enabled.setter
    def is_comments_enabled(self, value: bool):
        """
        Default value: ``True``
        """
        self.__data['is_comments_enabled'] = value


    @required
    @property
    def language(self) -> str:
        """
        Default value: ``"en"``
        """
        return self.__data.setdefault('language', "en")


    @language.setter
    def language(self, value: str):
        """
        Default value: ``"en"``
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


    @property
    def lti_private_profile(self) -> bool:
        """
        Default value: ``False``
        """
        return self.__data['lti_private_profile']


    @lti_private_profile.setter
    def lti_private_profile(self, value: bool):
        """
        Default value: ``False``
        """
        self.__data['lti_private_profile'] = value


from api.subscriptions import Subscription
from api.users import User
from api.groups import Group
from api.steps import Step


class Lesson:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'Lesson(id={self.id!r})'


    @property
    def steps(self) -> ResourcesList[Step]:
        return ResourcesList[Step](Step, self.__stepik, self, 'steps_ids')


    @property
    def subscriptions(self) -> ResourcesList[Subscription]:
        return ResourcesList[Subscription](Subscription, self.__stepik, self, 'subscriptions_ids')


    def owner(self) -> User:
        return User(self.__stepik, self.__stepik.fetch_object('User', self.owner_id))


    def learners_group(self) -> Group:
        return Group(self.__stepik, self.__stepik.fetch_object('Group', self.learners_group_id))


    def testers_group(self) -> Group:
        return Group(self.__stepik, self.__stepik.fetch_object('Group', self.testers_group_id))


    def moderators_group(self) -> Group:
        return Group(self.__stepik, self.__stepik.fetch_object('Group', self.moderators_group_id))


    def teachers_group(self) -> Group:
        return Group(self.__stepik, self.__stepik.fetch_object('Group', self.teachers_group_id))


    def admins_group(self) -> Group:
        return Group(self.__stepik, self.__stepik.fetch_object('Group', self.admins_group_id))


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @readonly
    @property
    def actions(self) -> dict:
        """
        Contains a dict of ``<action : link to the page>``
        """
        return self.__data['actions']


    @readonly
    @property
    def progress(self) -> str:
        """
        The :class:`Progress` object identifier
        """
        return self.__data['progress']


    @readonly
    @property
    def viewed_by(self) -> int:
        """
        Number of users who checked out the lesson
        """
        return self.__data['viewed_by']


    @readonly
    @property
    def passed_by(self) -> int:
        """
        Number of users who completed the lesson
        """
        return self.__data['passed_by']


    @readonly
    @property
    def time_to_complete(self) -> int:
        """
        Approximate time `in seconds` to complete the lesson.

        May be ``None``.
        """
        return self.__data['time_to_complete']


    @property
    def cover_url(self) -> str:
        """
        Direct link to the cover image of size 180×180. None, if there is no video steps in the lesson

        Type: url
        """
        return self.__data['cover_url']


    @cover_url.setter
    def cover_url(self, value: str):
        """
        Direct link to the cover image of size 180×180. None, if there is no video steps in the lesson

        Type: url
        """
        self.__data['cover_url'] = value


    @property
    def is_comments_enabled(self) -> bool:
        """
        Default value: ``True``
        """
        return self.__data.setdefault('is_comments_enabled', True)


    @is_comments_enabled.setter
    def is_comments_enabled(self, value: bool):
        """
        Default value: ``True``
        """
        self.__data['is_comments_enabled'] = value


    @required
    @property
    def language(self) -> str:
        """
        Language code

        One of these: ``af`` / ``ar`` / ``ast`` / ``az`` / ``bg`` / ``be`` / ``bn`` / ``br`` / ``bs`` / ``ca`` / ``cs`` / ``cy`` / ``da`` / ``de`` / ``dsb`` / ``el`` / ``en`` / ``en-au`` / ``en-gb`` / ``eo`` / ``es`` / ``es-ar`` / ``es-co`` / ``es-mx`` / ``es-ni`` / ``es-ve`` / ``et`` / ``eu`` / ``fa`` / ``fi`` / ``fr`` / ``fy`` / ``ga`` / ``gd`` / ``gl`` / ``he`` / ``hi`` / ``hr`` / ``hsb`` / ``hu`` / ``ia`` / ``id`` / ``io`` / ``is`` / ``it`` / ``ja`` / ``ka`` / ``kk`` / ``km`` / ``kn`` / ``ko`` / ``lb`` / ``lt`` / ``lv`` / ``mk`` / ``ml`` / ``mn`` / ``mr`` / ``my`` / ``nb`` / ``ne`` / ``nl`` / ``nn`` / ``os`` / ``pa`` / ``pl`` / ``pt`` / ``pt-br`` / ``ro`` / ``ru`` / ``sk`` / ``sl`` / ``sq`` / ``sr`` / ``sr-latn`` / ``sv`` / ``sw`` / ``ta`` / ``te`` / ``th`` / ``tr`` / ``tt`` / ``udm`` / ``uk`` / ``ur`` / ``vi`` / ``zh-hans`` / ``zh-hant``

        Default value: ``"en"``
        """
        return self.__data.setdefault('language', "en")


    @language.setter
    def language(self, value: str):
        """
        Language code

        One of these: ``af`` / ``ar`` / ``ast`` / ``az`` / ``bg`` / ``be`` / ``bn`` / ``br`` / ``bs`` / ``ca`` / ``cs`` / ``cy`` / ``da`` / ``de`` / ``dsb`` / ``el`` / ``en`` / ``en-au`` / ``en-gb`` / ``eo`` / ``es`` / ``es-ar`` / ``es-co`` / ``es-mx`` / ``es-ni`` / ``es-ve`` / ``et`` / ``eu`` / ``fa`` / ``fi`` / ``fr`` / ``fy`` / ``ga`` / ``gd`` / ``gl`` / ``he`` / ``hi`` / ``hr`` / ``hsb`` / ``hu`` / ``ia`` / ``id`` / ``io`` / ``is`` / ``it`` / ``ja`` / ``ka`` / ``kk`` / ``km`` / ``kn`` / ``ko`` / ``lb`` / ``lt`` / ``lv`` / ``mk`` / ``ml`` / ``mn`` / ``mr`` / ``my`` / ``nb`` / ``ne`` / ``nl`` / ``nn`` / ``os`` / ``pa`` / ``pl`` / ``pt`` / ``pt-br`` / ``ro`` / ``ru`` / ``sk`` / ``sl`` / ``sq`` / ``sr`` / ``sr-latn`` / ``sv`` / ``sw`` / ``ta`` / ``te`` / ``th`` / ``tr`` / ``tt`` / ``udm`` / ``uk`` / ``ur`` / ``vi`` / ``zh-hans`` / ``zh-hant``

        Default value: ``"en"``
        """
        self.__data['language'] = value


    @readonly
    @property
    def is_featured(self) -> bool:
        """
        Default value: ``False``
        """
        import warnings; warnings.warn('This function is deprecated', DeprecationWarning)
        return self.__data['is_featured']


    @property
    def is_public(self) -> bool:
        """
        Any user can access and learn `public` lesson. If lesson is private, then learners need to use invitation link or be added by user ID.
        """
        return self.__data['is_public']


    @is_public.setter
    def is_public(self, value: bool):
        """
        Any user can access and learn `public` lesson. If lesson is private, then learners need to use invitation link or be added by user ID.
        """
        self.__data['is_public'] = value


    @required
    @property
    def title(self) -> str:
        """
        Title of the lesson
        """
        return self.__data['title']


    @title.setter
    def title(self, value: str):
        """
        Title of the lesson
        """
        self.__data['title'] = value


    @readonly
    @property
    def slug(self) -> str:
        """
        A string of format "title-id", with hyphens instead of spaces
        """
        return self.__data['slug']


    @readonly
    @property
    def create_date(self) -> str:
        """
        Creation time

        Type: datetime
        """
        return self.__data['create_date']


    @readonly
    @property
    def update_date(self) -> str:
        """
        Time of the last update

        Type: datetime
        """
        return self.__data['update_date']


    @readonly
    @property
    def discussions_count(self) -> int:
        """
        Number of comment trees

        Default value: ``0``
        """
        return self.__data['discussions_count']


    @readonly
    @property
    def discussion_proxy(self) -> str:
        """
        Discussion tree's identifier
        """
        return self.__data['discussion_proxy']


    @readonly
    @property
    def discussion_threads(self) -> List[str]:
        """
        Same as ``discussion_proxy`` in most cases
        """
        return self.__data['discussion_threads']


    @readonly
    @property
    def epic_count(self) -> int:
        """
        Number of likes
        """
        return self.__data['epic_count']


    @readonly
    @property
    def abuse_count(self) -> int:
        """
        Number of dislikes
        """
        return self.__data['abuse_count']


    @readonly
    @property
    def vote_delta(self) -> int:
        return self.__data['vote_delta']


    @readonly
    @property
    def vote(self) -> str:
        """
        The :class:`Vote` object identifier
        """
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


    @property
    def lti_private_profile(self) -> bool:
        """
        Default value: ``False``
        """
        return self.__data['lti_private_profile']


    @lti_private_profile.setter
    def lti_private_profile(self, value: bool):
        """
        Default value: ``False``
        """
        self.__data['lti_private_profile'] = value


    @required
    @property
    def steps_ids(self) -> List[int]:
        return self.__data['steps']


    @steps_ids.setter
    def steps_ids(self, value: List[int]):
        self.__data['steps'] = value


    @readonly
    @property
    def subscriptions_ids(self) -> str:
        """
        List[int]
        """
        return self.__data['subscriptions']


    @readonly
    @property
    def owner_id(self) -> int:
        """
        :class:`User`'s id of the lesson's owner
        """
        return self.__data['owner']


    @readonly
    @property
    def learners_group_id(self) -> int:
        """
        :class:`Group`'s id. Equals ``None`` if user isn't lesson's owner or admin.
        """
        return self.__data['learners_group']


    @readonly
    @property
    def testers_group_id(self) -> int:
        """
        :class:`Group`'s id. Equals ``None`` if user isn't lesson's owner or admin.
        """
        return self.__data['testers_group']


    @readonly
    @property
    def moderators_group_id(self) -> int:
        """
        :class:`Group`'s id. Equals ``None`` if user isn't lesson's owner or admin.
        """
        return self.__data['moderators_group']


    @readonly
    @property
    def teachers_group_id(self) -> int:
        """
        :class:`Group`'s id. Equals ``None`` if user isn't lesson's owner or admin.
        """
        return self.__data['teachers_group']


    @readonly
    @property
    def admins_group_id(self) -> int:
        """
        :class:`Group`'s id. Equals ``None`` if user isn't lesson's owner or admin.
        """
        return self.__data['admins_group']


