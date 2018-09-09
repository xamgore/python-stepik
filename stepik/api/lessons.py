# This file is generated
from typing import List, Iterable, Any, Optional

from stepik.errors import StepikError
from stepik.common import required, readonly
from stepik.resources_list import ResourcesList
from .groups import Group
from .subscriptions import Subscription
from .steps import Step
from .users import User


class Lesson:
    """
    Lesson resource.
    Lesson is a collection of steps.
    """

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


    def admins_group(self) -> Group:
        return Group(self._stepik, self._stepik._fetch_object(Group, self.admins_group_id))


    def learners_group(self) -> Group:
        return Group(self._stepik, self._stepik._fetch_object(Group, self.learners_group_id))


    def teachers_group(self) -> Group:
        return Group(self._stepik, self._stepik._fetch_object(Group, self.teachers_group_id))


    def moderators_group(self) -> Group:
        return Group(self._stepik, self._stepik._fetch_object(Group, self.moderators_group_id))


    def owner(self) -> User:
        return User(self._stepik, self._stepik._fetch_object(User, self.owner_id))


    def testers_group(self) -> Group:
        return Group(self._stepik, self._stepik._fetch_object(Group, self.testers_group_id))


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
    def subscriptions_ids(self) -> str:
        """
        List[int]
        """
        return self._data['subscriptions']


    @readonly
    @property
    def admins_group_id(self) -> int:
        """
        :class:`Group`'s id. Equals ``None`` if user isn't lesson's owner or admin.
        """
        return self._data['admins_group']


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
    def testers_group_id(self) -> int:
        """
        :class:`Group`'s id. Equals ``None`` if user isn't lesson's owner or admin.
        """
        return self._data['testers_group']




class ListOfLessons:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> Lesson:
        obj = self._stepik._fetch_object(Lesson, id)
        return Lesson(self._stepik, obj)


    def get_all(self, ids: Iterable[int], keep_order=False) -> Iterable[Lesson]:
        """
        Grab a bunch of ids, usually 20 objects per request.
        """
        if keep_order:
            ids = list(ids)

        objects = self._stepik._fetch_objects(Lesson, ids)
        iterable = (Lesson(self._stepik, o) for o in objects)

        return iterable if not keep_order \
            else sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))


    def iterate(self,
                is_featured: bool = None,
                language: str = None,
                owner: Any = None,
                course: Any = None,
                by_vote_epic: bool = None,
                by_create_date: bool = None,
                by_id: bool = None,
                by_update_date: bool = None,
                by_vote_delta: bool = None,
                by_vote_abuse: bool = None,
                skip: int = 0, limit: Optional[int] = 20) -> Iterable[Lesson]:
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
            page = self._stepik._get(f'lessons?{params}&page={page_idx}&order={ordering}')

            for obj in page['lessons']:
                if limit and count >= limit:
                    break

                yield Lesson(self._stepik, obj)
                count += 1

            if not page['meta']['has_next']:
                break

            page_idx += 1


    def __iter__(self):
        yield from self.iterate(limit=None)


    def create(self,
               title: str,
               steps: List[int] = None,
               cover_url: str = None,
               is_comments_enabled: bool = None,
               language: str = None,
               is_public: bool = None,
               lti_consumer_key: str = None,
               lti_secret_key: str = None,
               lti_private_profile: bool = None,
               **kwargs) -> Lesson:
        vars = locals().copy()
        data = {'lesson':
                    {k: v for k, v in {**vars, **kwargs}.items()
                     if k != 'self' and v is not None}}

        response = self._stepik._post('lessons', data)
        if 'lessons' not in response:
            raise StepikError(response)

        return Lesson(self._stepik, response['lessons'][0])


    def delete(self, id: int) -> dict:
        """Delete the object by its id. Returns the server's response"""
        return self._stepik._delete('lessons', id)


    def update(self, obj: Lesson) -> Lesson:
        required = ['title', 'steps', 'cover_url', 'is_comments_enabled', 'language', 'is_public', 'lti_consumer_key', 'lti_secret_key', 'lti_private_profile']
        vars = obj._data
        data = {'lesson':
                    {k: v for k, v in vars.items()
                     if k != 'self' and v is not None and k in required }}

        response = self._stepik._put(f'lessons/{ obj.id }', data)
        if 'lessons' not in response:
            raise StepikError(response)

        return Lesson(self._stepik, response['lessons'][0])

