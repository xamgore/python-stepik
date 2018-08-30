# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList
from api.users import User
from api.groups import Group
from api.steps import Step
from api.subscriptions import Subscription


class Lesson:
    _resources_name = 'lessons'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'Lesson(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model Lesson are missing')


    @property
    def subscriptions(self) -> ResourcesList[Subscription]:
        return ResourcesList[Subscription]\
            (Subscription, self._stepik, holder=self, field_with_ids='subscriptions_ids')


    @property
    def steps(self) -> ResourcesList[Step]:
        return ResourcesList[Step]\
            (Step, self._stepik, holder=self, field_with_ids='steps_ids')


    def moderators_group(self) -> Group:
        return Group(self._stepik, self._stepik._fetch_object(Group, self.moderators_group_id))


    def owner(self) -> User:
        return User(self._stepik, self._stepik._fetch_object(User, self.owner_id))


    def admins_group(self) -> Group:
        return Group(self._stepik, self._stepik._fetch_object(Group, self.admins_group_id))


    def testers_group(self) -> Group:
        return Group(self._stepik, self._stepik._fetch_object(Group, self.testers_group_id))


    def learners_group(self) -> Group:
        return Group(self._stepik, self._stepik._fetch_object(Group, self.learners_group_id))


    def teachers_group(self) -> Group:
        return Group(self._stepik, self._stepik._fetch_object(Group, self.teachers_group_id))


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @readonly
    @property
    def actions(self) -> dict:
        """
        Contains a dict of ``<action : link to the page>``

        Type: dict
        """
        return self._data['actions']


    @readonly
    @property
    def progress(self) -> str:
        """
        The :class:`Progress` object identifier
        """
        return self._data['progress']


    @readonly
    @property
    def viewed_by(self) -> int:
        """
        Number of users who checked out the lesson
        """
        return self._data['viewed_by']


    @readonly
    @property
    def passed_by(self) -> int:
        """
        Number of users who completed the lesson
        """
        return self._data['passed_by']


    @readonly
    @property
    def time_to_complete(self) -> int:
        """
        Approximate time `in seconds` to complete the lesson.

        May be ``None``.
        """
        return self._data['time_to_complete']


    @property
    def cover_url(self) -> str:
        """
        Direct link to the cover image of size 180×180. None, if there is no video steps in the lesson

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('cover_url', "None")


    @cover_url.setter
    def cover_url(self, value: str):
        """
        Direct link to the cover image of size 180×180. None, if there is no video steps in the lesson

        Default value: ``"None"``

        Type: str
        """
        self._data['cover_url'] = value


    @property
    def is_comments_enabled(self) -> bool:
        """
        Default value: ``True``
        """
        return self._data.setdefault('is_comments_enabled', True)


    @is_comments_enabled.setter
    def is_comments_enabled(self, value: bool):
        """
        Default value: ``True``
        """
        self._data['is_comments_enabled'] = value


    @required
    @property
    def language(self) -> str:
        """
        Language code

        One of these: ``af`` / ``ar`` / ``ast`` / ``az`` / ``bg`` / ``be`` / ``bn`` / ``br`` / ``bs`` / ``ca`` / ``cs`` / ``cy`` / ``da`` / ``de`` / ``dsb`` / ``el`` / ``en`` / ``en-au`` / ``en-gb`` / ``eo`` / ``es`` / ``es-ar`` / ``es-co`` / ``es-mx`` / ``es-ni`` / ``es-ve`` / ``et`` / ``eu`` / ``fa`` / ``fi`` / ``fr`` / ``fy`` / ``ga`` / ``gd`` / ``gl`` / ``he`` / ``hi`` / ``hr`` / ``hsb`` / ``hu`` / ``ia`` / ``id`` / ``io`` / ``is`` / ``it`` / ``ja`` / ``ka`` / ``kk`` / ``km`` / ``kn`` / ``ko`` / ``lb`` / ``lt`` / ``lv`` / ``mk`` / ``ml`` / ``mn`` / ``mr`` / ``my`` / ``nb`` / ``ne`` / ``nl`` / ``nn`` / ``os`` / ``pa`` / ``pl`` / ``pt`` / ``pt-br`` / ``ro`` / ``ru`` / ``sk`` / ``sl`` / ``sq`` / ``sr`` / ``sr-latn`` / ``sv`` / ``sw`` / ``ta`` / ``te`` / ``th`` / ``tr`` / ``tt`` / ``udm`` / ``uk`` / ``ur`` / ``vi`` / ``zh-hans`` / ``zh-hant``

        Default value: ``"en"``

        Type: str
        """
        return self._data.setdefault('language', "en")


    @language.setter
    def language(self, value: str):
        """
        Language code

        One of these: ``af`` / ``ar`` / ``ast`` / ``az`` / ``bg`` / ``be`` / ``bn`` / ``br`` / ``bs`` / ``ca`` / ``cs`` / ``cy`` / ``da`` / ``de`` / ``dsb`` / ``el`` / ``en`` / ``en-au`` / ``en-gb`` / ``eo`` / ``es`` / ``es-ar`` / ``es-co`` / ``es-mx`` / ``es-ni`` / ``es-ve`` / ``et`` / ``eu`` / ``fa`` / ``fi`` / ``fr`` / ``fy`` / ``ga`` / ``gd`` / ``gl`` / ``he`` / ``hi`` / ``hr`` / ``hsb`` / ``hu`` / ``ia`` / ``id`` / ``io`` / ``is`` / ``it`` / ``ja`` / ``ka`` / ``kk`` / ``km`` / ``kn`` / ``ko`` / ``lb`` / ``lt`` / ``lv`` / ``mk`` / ``ml`` / ``mn`` / ``mr`` / ``my`` / ``nb`` / ``ne`` / ``nl`` / ``nn`` / ``os`` / ``pa`` / ``pl`` / ``pt`` / ``pt-br`` / ``ro`` / ``ru`` / ``sk`` / ``sl`` / ``sq`` / ``sr`` / ``sr-latn`` / ``sv`` / ``sw`` / ``ta`` / ``te`` / ``th`` / ``tr`` / ``tt`` / ``udm`` / ``uk`` / ``ur`` / ``vi`` / ``zh-hans`` / ``zh-hant``

        Default value: ``"en"``

        Type: str
        """
        self._data['language'] = value


    @readonly
    @property
    def is_featured(self) -> bool:
        """
        Default value: ``False``
        """
        import warnings; warnings.warn('This function is deprecated', DeprecationWarning)
        return self._data['is_featured']


    @property
    def is_public(self) -> bool:
        """
        Any user can access and learn `public` lesson. If lesson is private, then learners need to use invitation link or be added by user ID.
        """
        return self._data['is_public']


    @is_public.setter
    def is_public(self, value: bool):
        """
        Any user can access and learn `public` lesson. If lesson is private, then learners need to use invitation link or be added by user ID.
        """
        self._data['is_public'] = value


    @required
    @property
    def title(self) -> str:
        """
        Title of the lesson
        """
        return self._data['title']


    @title.setter
    def title(self, value: str):
        """
        Title of the lesson
        """
        self._data['title'] = value


    @readonly
    @property
    def slug(self) -> str:
        """
        A string of format "title-id", with hyphens instead of spaces
        """
        return self._data['slug']


    @readonly
    @property
    def create_date(self) -> str:
        """
        Creation time

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('create_date', "None")


    @readonly
    @property
    def update_date(self) -> str:
        """
        Time of the last update

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('update_date', "None")


    @readonly
    @property
    def discussions_count(self) -> int:
        """
        Number of comment trees

        Default value: ``0``
        """
        return self._data['discussions_count']


    @readonly
    @property
    def discussion_proxy(self) -> str:
        """
        Discussion tree's identifier
        """
        return self._data['discussion_proxy']


    @readonly
    @property
    def discussion_threads(self) -> List[str]:
        """
        Same as ``discussion_proxy`` in most cases

        Type: List[str]
        """
        return self._data['discussion_threads']


    @readonly
    @property
    def epic_count(self) -> int:
        """
        Number of likes
        """
        return self._data['epic_count']


    @readonly
    @property
    def abuse_count(self) -> int:
        """
        Number of dislikes
        """
        return self._data['abuse_count']


    @readonly
    @property
    def vote_delta(self) -> int:
        return self._data['vote_delta']


    @readonly
    @property
    def vote(self) -> str:
        """
        The :class:`Vote` object identifier
        """
        return self._data['vote']


    @property
    def lti_consumer_key(self) -> str:
        return self._data['lti_consumer_key']


    @lti_consumer_key.setter
    def lti_consumer_key(self, value: str):
        self._data['lti_consumer_key'] = value


    @property
    def lti_secret_key(self) -> str:
        return self._data['lti_secret_key']


    @lti_secret_key.setter
    def lti_secret_key(self, value: str):
        self._data['lti_secret_key'] = value


    @property
    def lti_private_profile(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['lti_private_profile']


    @lti_private_profile.setter
    def lti_private_profile(self, value: bool):
        """
        Default value: ``False``
        """
        self._data['lti_private_profile'] = value


    @readonly
    @property
    def moderators_group_id(self) -> int:
        """
        :class:`Group`'s id. Equals ``None`` if user isn't lesson's owner or admin.
        """
        return self._data['moderators_group']


    @readonly
    @property
    def owner_id(self) -> int:
        """
        :class:`User`'s id of the lesson's owner
        """
        return self._data['owner']


    @readonly
    @property
    def admins_group_id(self) -> int:
        """
        :class:`Group`'s id. Equals ``None`` if user isn't lesson's owner or admin.
        """
        return self._data['admins_group']


    @readonly
    @property
    def testers_group_id(self) -> int:
        """
        :class:`Group`'s id. Equals ``None`` if user isn't lesson's owner or admin.
        """
        return self._data['testers_group']


    @readonly
    @property
    def subscriptions_ids(self) -> str:
        """
        List[int]
        """
        return self._data['subscriptions']


    @readonly
    @property
    def learners_group_id(self) -> int:
        """
        :class:`Group`'s id. Equals ``None`` if user isn't lesson's owner or admin.
        """
        return self._data['learners_group']


    @required
    @property
    def steps_ids(self) -> List[int]:
        """
        Type: List[int]
        """
        return self._data['steps']


    @steps_ids.setter
    def steps_ids(self, value: List[int]):
        """
        Type: List[int]
        """
        self._data['steps'] = value


    @readonly
    @property
    def teachers_group_id(self) -> int:
        """
        :class:`Group`'s id. Equals ``None`` if user isn't lesson's owner or admin.
        """
        return self._data['teachers_group']




class ListOfLessons:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> Lesson:
        return Lesson(self._stepik, self._stepik._fetch_object(Lesson, id))


    def get_all(self, ids: List[int], keep_order=False) -> Iterable[Lesson]:
        objects = self._stepik._fetch_objects(Lesson, ids)
        iterable = (Lesson(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)


    def create(self, title: str, steps: List[int] = None, cover_url: str = None, is_comments_enabled: bool = None, language: str = None, is_public: bool = None, lti_consumer_key: str = None, lti_secret_key: str = None, lti_private_profile: bool = None) -> Lesson:
        vars = locals().copy()
        data = {'lesson': {k: v for k, v in vars.items() if k != 'self' and v is not None}}

        resources_name = 'lessons'
        response = self._stepik._post(resources_name, data)

        if resources_name not in response:
            raise StepikError(response)

        return Lesson(self._stepik, response[resources_name][0])


    def delete(self, id: int) -> dict:
        return self._stepik._delete('lessons', id)
