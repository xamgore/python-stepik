# This file is generated
from typing import List, Iterable, Any, Optional

from stepik.errors import StepikError
from stepik.common import required, readonly
from stepik.resources_list import ResourcesList
from .groups import Group
from .tags import Tag
from .sections import Section
from .users import User


class Course:
    """
    Course resource.
    Course is a list of lessons.
    """

    _resources_name = 'courses'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'Course(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model Course are missing')


    @property
    def sections(self) -> ResourcesList[Section]:
        return ResourcesList[Section]\
            (Section, self._stepik, holder=self, field_with_ids='sections_ids')


    @property
    def authors(self) -> ResourcesList[User]:
        return ResourcesList[User]\
            (User, self._stepik, holder=self, field_with_ids='authors_ids')


    @property
    def tags(self) -> ResourcesList[Tag]:
        return ResourcesList[Tag]\
            (Tag, self._stepik, holder=self, field_with_ids='tags_ids')


    def owner(self) -> User:
        return User(self._stepik, self._stepik._fetch_object(User, self.owner_id))


    def learners_group(self) -> Group:
        return Group(self._stepik, self._stepik._fetch_object(Group, self.learners_group_id))


    def testers_group(self) -> Group:
        return Group(self._stepik, self._stepik._fetch_object(Group, self.testers_group_id))


    def moderators_group(self) -> Group:
        return Group(self._stepik, self._stepik._fetch_object(Group, self.moderators_group_id))


    def teachers_group(self) -> Group:
        return Group(self._stepik, self._stepik._fetch_object(Group, self.teachers_group_id))


    def admins_group(self) -> Group:
        return Group(self._stepik, self._stepik._fetch_object(Group, self.admins_group_id))


    @readonly
    @property
    def id(self) -> int:
        """
        Course's unique identifier
        """
        return self._data['id']


    @property
    def summary(self) -> str:
        """
        Short description about the course, may contain HTML tags
        """
        return self._data['summary']


    @summary.setter
    def summary(self, value: str):
        """
        Short description about the course, may contain HTML tags
        """
        self._data['summary'] = value


    @property
    def workload(self) -> str:
        return self._data['workload']


    @workload.setter
    def workload(self, value: str):
        self._data['workload'] = value


    @readonly
    @property
    def cover(self) -> str:
        """
        Path to the cover image, without the hostname, i.e. ``/media/...1c67c.png``.

        May take ``None`` value.

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('cover', "None")


    @property
    def intro(self) -> str:
        """
        Link to the introduction video (with html5 player), that may explain what is the course about.

        Default value: ``""``

        Type: str
        """
        return self._data.setdefault('intro', "")


    @intro.setter
    def intro(self, value: str):
        """
        Link to the introduction video (with html5 player), that may explain what is the course about.

        Default value: ``""``

        Type: str
        """
        self._data['intro'] = value


    @property
    def course_format(self) -> str:
        """
        Default value: ````
        """
        return self._data['course_format']


    @course_format.setter
    def course_format(self, value: str):
        """
        Default value: ````
        """
        self._data['course_format'] = value


    @property
    def target_audience(self) -> str:
        """
        Default value: ````
        """
        return self._data['target_audience']


    @target_audience.setter
    def target_audience(self, value: str):
        """
        Default value: ````
        """
        self._data['target_audience'] = value


    @readonly
    @property
    def certificate_footer(self) -> str:
        """
        May take ``None`` value.

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('certificate_footer', "None")


    @readonly
    @property
    def certificate_cover_org(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('certificate_cover_org', "None")


    @property
    def is_certificate_auto_issued(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['is_certificate_auto_issued']


    @is_certificate_auto_issued.setter
    def is_certificate_auto_issued(self, value: bool):
        """
        Default value: ``False``
        """
        self._data['is_certificate_auto_issued'] = value


    @property
    def certificate_regular_threshold(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['certificate_regular_threshold']


    @certificate_regular_threshold.setter
    def certificate_regular_threshold(self, value: int):
        """
        Default value: ``0``
        """
        self._data['certificate_regular_threshold'] = value


    @property
    def certificate_distinction_threshold(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['certificate_distinction_threshold']


    @certificate_distinction_threshold.setter
    def certificate_distinction_threshold(self, value: int):
        """
        Default value: ``0``
        """
        self._data['certificate_distinction_threshold'] = value


    @property
    def instructors(self) -> List[int]:
        """
        Type: List[int]
        """
        return self._data['instructors']


    @instructors.setter
    def instructors(self, value: List[int]):
        """
        Type: List[int]
        """
        self._data['instructors'] = value


    @property
    def certificate(self) -> str:
        return self._data['certificate']


    @certificate.setter
    def certificate(self, value: str):
        self._data['certificate'] = value


    @property
    def requirements(self) -> str:
        return self._data['requirements']


    @requirements.setter
    def requirements(self, value: str):
        self._data['requirements'] = value


    @property
    def description(self) -> str:
        """
        Full description about the course, may contain HTML tags
        """
        return self._data['description']


    @description.setter
    def description(self, value: str):
        """
        Full description about the course, may contain HTML tags
        """
        self._data['description'] = value


    @readonly
    @property
    def total_units(self) -> int:
        """
        Total number of units
        """
        return self._data['total_units']


    @readonly
    @property
    def enrollment(self) -> int:
        """
        Enrollment id (which usually is equals to course id), if user enrolled. If not, ``None``.
        """
        return self._data['enrollment']


    @readonly
    @property
    def is_favorite(self) -> bool:
        """
        Is the course is favourite. See ``favorite_courses`` list.
        """
        return self._data['is_favorite']


    @readonly
    @property
    def actions(self) -> dict:
        """
        Contains a dict of ``<action : link to the page>``. If user is not an admin or the course owner, dict is empty.

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
    def first_lesson(self) -> int:
        return self._data['first_lesson']


    @readonly
    @property
    def first_unit(self) -> str:
        return self._data['first_unit']


    @readonly
    @property
    def certificate_link(self) -> str:
        return self._data['certificate_link']


    @readonly
    @property
    def certificate_regular_link(self) -> str:
        return self._data['certificate_regular_link']


    @readonly
    @property
    def certificate_distinction_link(self) -> str:
        return self._data['certificate_distinction_link']


    @readonly
    @property
    def schedule_link(self) -> str:
        """
        Path to the ``ics``, without the host name
        """
        return self._data['schedule_link']


    @readonly
    @property
    def schedule_long_link(self) -> str:
        """
        Path to the ``ics``, without the host name
        """
        return self._data['schedule_long_link']


    @readonly
    @property
    def first_deadline(self) -> str:
        return self._data['first_deadline']


    @readonly
    @property
    def last_deadline(self) -> str:
        return self._data['last_deadline']


    @readonly
    @property
    def subscriptions(self) -> List[str]:
        """
        Type: List[str]
        """
        return self._data['subscriptions']


    @readonly
    @property
    def announcements(self) -> List[str]:
        """
        Type: List[str]
        """
        return self._data['announcements']


    @readonly
    @property
    def is_contest(self) -> bool:
        return self._data['is_contest']


    @readonly
    @property
    def is_self_paced(self) -> bool:
        """
        Completely open course, without deadlines and other things
        """
        return self._data['is_self_paced']


    @property
    def is_adaptive(self) -> bool:
        """
        Adaptive means that course is based on tasks, which can be marked as easy or hard. Stepik will give better tasks next time.

        Default value: ``False``
        """
        return self._data['is_adaptive']


    @is_adaptive.setter
    def is_adaptive(self, value: bool):
        """
        Adaptive means that course is based on tasks, which can be marked as easy or hard. Stepik will give better tasks next time.

        Default value: ``False``
        """
        self._data['is_adaptive'] = value


    @property
    def is_idea_compatible(self) -> bool:
        """
        Default value: ``False``
        """
        import warnings; warnings.warn('This function is deprecated', DeprecationWarning)
        return self._data['is_idea_compatible']


    @is_idea_compatible.setter
    def is_idea_compatible(self, value: bool):
        """
        Default value: ``False``
        """
        import warnings; warnings.warn('This function is deprecated', DeprecationWarning)
        self._data['is_idea_compatible'] = value


    @readonly
    @property
    def last_step(self) -> int:
        return self._data['last_step']


    @property
    def intro_video(self) -> dict:
        """
        Dict with following fields:

        * thumbnail — full url to image
        * urls — list of ``{quality, url}``
        * duration — in seconds
        * upload_date — isoformat
        * filename

        Type: dict
        """
        return self._data['intro_video']


    @intro_video.setter
    def intro_video(self, value: dict):
        """
        Dict with following fields:

        * thumbnail — full url to image
        * urls — list of ``{quality, url}``
        * duration — in seconds
        * upload_date — isoformat
        * filename

        Type: dict
        """
        self._data['intro_video'] = value


    @readonly
    @property
    def social_providers(self) -> str:
        return self._data['social_providers']


    @readonly
    @property
    def has_tutors(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['has_tutors']


    @readonly
    @property
    def is_promoted(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['is_promoted']


    @property
    def is_enabled(self) -> bool:
        """
        Default value: ``True``
        """
        return self._data.setdefault('is_enabled', True)


    @is_enabled.setter
    def is_enabled(self, value: bool):
        """
        Default value: ``True``
        """
        self._data['is_enabled'] = value


    @readonly
    @property
    def is_proctored(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['is_proctored']


    @readonly
    @property
    def proctor_url(self) -> str:
        """
        May take ``None`` value.

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('proctor_url', "None")


    @required
    @readonly
    @property
    def review_summary(self) -> int:
        return self._data['review_summary']


    @readonly
    @property
    def schedule_type(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('schedule_type', "None")


    @required
    @readonly
    @property
    def certificates_count(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['certificates_count']


    @required
    @readonly
    @property
    def learners_count(self) -> int:
        """
        Number of learners enrolled

        Default value: ``0``
        """
        return self._data['learners_count']


    @readonly
    @property
    def time_to_complete(self) -> int:
        """
        Average time to complete the course
        """
        return self._data['time_to_complete']


    @readonly
    @property
    def is_popular(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['is_popular']


    @readonly
    @property
    def similar_courses(self) -> List[int]:
        """
        Type: List[int]
        """
        return self._data['similar_courses']


    @readonly
    @property
    def is_unsuitable(self) -> bool:
        """
        Does course contain information unsuitable for a wide audience? (how to drink alcohol at work)

        Default value: ``False``
        """
        return self._data['is_unsuitable']


    @readonly
    @property
    def is_paid(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['is_paid']


    @readonly
    @property
    def price(self) -> float:
        """
        Default value: ``"None"``
        """
        return self._data.setdefault('price', "None")


    @readonly
    @property
    def currency_code(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('currency_code', "None")


    @readonly
    @property
    def display_price(self) -> str:
        return self._data['display_price']


    @readonly
    @property
    def continue_url(self) -> str:
        return self._data['continue_url']


    @required
    @readonly
    @property
    def readiness(self) -> str:
        """
        Default value: ``"0"``

        Type: str
        """
        return self._data.setdefault('readiness', "0")


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
        Course will be shown in the catalogue, the field is set by admins.

        Default value: ``False``
        """
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
        Title of the course
        """
        return self._data['title']


    @title.setter
    def title(self, value: str):
        """
        Title of the course
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
    def begin_date(self) -> str:
        """
        Open date: when the course starts for enrolled users.

        Use `begin_date_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('begin_date', "None")


    @readonly
    @property
    def end_date(self) -> str:
        """
        Close date: when the module will be disabled (close date is usually left empty).

        Use `end_date_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('end_date', "None")


    @readonly
    @property
    def soft_deadline(self) -> str:
        """
        Soft deadline: when the cost of every step will be reduced.

        Use `soft_deadline_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('soft_deadline', "None")


    @readonly
    @property
    def hard_deadline(self) -> str:
        """
        Hard deadline: when the cost of every step will be zero.

        Use `hard_deadline_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('hard_deadline', "None")


    @readonly
    @property
    def grading_policy(self) -> str:
        """
        Policy can be one of these:

        * ``None`` — default for the course
        * ``"no_deadlines"`` — no deadlines
        * ``"halved"`` — half points
        * ``"linear"`` — linear descending

        Use `grading_policy_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('grading_policy', "None")


    @property
    def begin_date_source(self) -> str:
        """
        Open date: when the module starts for enrolled users

        Use `begin_date_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('begin_date_source', "None")


    @begin_date_source.setter
    def begin_date_source(self, value: str):
        """
        Open date: when the module starts for enrolled users

        Use `begin_date_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        self._data['begin_date_source'] = value


    @property
    def end_date_source(self) -> str:
        """
        Close date: when the module will be disabled (close date is usually left empty).

        Use `end_date_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('end_date_source', "None")


    @end_date_source.setter
    def end_date_source(self, value: str):
        """
        Close date: when the module will be disabled (close date is usually left empty).

        Use `end_date_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        self._data['end_date_source'] = value


    @property
    def soft_deadline_source(self) -> str:
        """
        Soft deadline: when the cost of every step will be reduced.

        Use `soft_deadline_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('soft_deadline_source', "None")


    @soft_deadline_source.setter
    def soft_deadline_source(self, value: str):
        """
        Soft deadline: when the cost of every step will be reduced.

        Use `soft_deadline_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        self._data['soft_deadline_source'] = value


    @property
    def hard_deadline_source(self) -> str:
        """
        Hard deadline: when the cost of every step will be zero.

        Use `hard_deadline_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('hard_deadline_source', "None")


    @hard_deadline_source.setter
    def hard_deadline_source(self, value: str):
        """
        Hard deadline: when the cost of every step will be zero.

        Use `hard_deadline_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        self._data['hard_deadline_source'] = value


    @property
    def grading_policy_source(self) -> str:
        """
        Policy can be one of these:

        * ``None`` — default for the course
        * ``"no_deadlines"`` — no deadlines
        * ``"halved"`` — half points
        * ``"linear"`` — linear descending

        Use `grading_policy_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('grading_policy_source', "None")


    @grading_policy_source.setter
    def grading_policy_source(self, value: str):
        """
        Policy can be one of these:

        * ``None`` — default for the course
        * ``"no_deadlines"`` — no deadlines
        * ``"halved"`` — half points
        * ``"linear"`` — linear descending

        Use `grading_policy_source` to update the value.

        Default value: ``"None"``

        Type: str
        """
        self._data['grading_policy_source'] = value


    @readonly
    @property
    def is_active(self) -> bool:
        return self._data['is_active']


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
    def owner_id(self) -> int:
        """
        :class:`User`'s id of the lesson's owner
        """
        return self._data['owner']


    @required
    @property
    def sections_ids(self) -> List[int]:
        """
        List of sections

        Type: List[int]
        """
        return self._data['sections']


    @sections_ids.setter
    def sections_ids(self, value: List[int]):
        """
        List of sections

        Type: List[int]
        """
        self._data['sections'] = value


    @readonly
    @property
    def learners_group_id(self) -> int:
        """
        :class:`Group`'s id. Equals ``None`` if user isn't lesson's owner or admin.
        """
        return self._data['learners_group']


    @readonly
    @property
    def testers_group_id(self) -> int:
        """
        :class:`Group`'s id. Equals ``None`` if user isn't lesson's owner or admin.
        """
        return self._data['testers_group']


    @readonly
    @property
    def moderators_group_id(self) -> int:
        """
        :class:`Group`'s id. Equals ``None`` if user isn't lesson's owner or admin.
        """
        return self._data['moderators_group']


    @readonly
    @property
    def teachers_group_id(self) -> int:
        """
        :class:`Group`'s id. Equals ``None`` if user isn't lesson's owner or admin.
        """
        return self._data['teachers_group']


    @readonly
    @property
    def admins_group_id(self) -> int:
        """
        :class:`Group`'s id. Equals ``None`` if user isn't lesson's owner or admin.
        """
        return self._data['admins_group']


    @property
    def authors_ids(self) -> List[int]:
        """
        List of authors, usually with the only person: course owner

        Type: List[int]
        """
        return self._data['authors']


    @authors_ids.setter
    def authors_ids(self, value: List[int]):
        """
        List of authors, usually with the only person: course owner

        Type: List[int]
        """
        self._data['authors'] = value


    @property
    def tags_ids(self) -> List[int]:
        """
        Type: List[int]
        """
        return self._data['tags']


    @tags_ids.setter
    def tags_ids(self, value: List[int]):
        """
        Type: List[int]
        """
        self._data['tags'] = value




class ListOfCourses:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> Course:
        obj = self._stepik._fetch_object(Course, id)
        return Course(self._stepik, obj)


    def get_all(self, ids: Iterable[int], keep_order=False) -> Iterable[Course]:
        """
        Grab a bunch of ids, usually 20 objects per request.
        """
        if keep_order:
            ids = list(ids)

        objects = self._stepik._fetch_objects(Course, ids)
        iterable = (Course(self._stepik, o) for o in objects)

        return iterable if not keep_order \
            else sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))


    def iterate(self,
                is_featured: bool = None,
                tag: Any = None,
                language: str = None,
                owner: Any = None,
                is_idea_compatible: bool = None,
                is_public: bool = None,
                is_promoted: bool = None,
                schedule_type: str = None,
                exclude_ended: Any = None,
                is_popular: bool = None,
                is_unsuitable: bool = None,
                is_paid: bool = None,
                enrolled: bool = None,
                by_create_date: bool = None,
                by_id: bool = None,
                by_popularity: bool = None,
                by_update_date: bool = None,
                by_activity: bool = None,
                skip: int = 0, limit: Optional[int] = 20) -> Iterable[Course]:
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
            page = self._stepik._get(f'courses?{params}&page={page_idx}&order={ordering}')

            for obj in page['courses']:
                if limit and count >= limit:
                    break

                yield Course(self._stepik, obj)
                count += 1

            if not page['meta']['has_next']:
                break

            page_idx += 1


    def __iter__(self):
        yield from self.iterate(limit=None)


    def create(self,
               title: str,
               summary: str = None,
               workload: str = None,
               intro: str = None,
               course_format: str = None,
               target_audience: str = None,
               is_certificate_auto_issued: bool = None,
               certificate_regular_threshold: int = None,
               certificate_distinction_threshold: int = None,
               instructors: List[int] = None,
               certificate: str = None,
               requirements: str = None,
               description: str = None,
               sections: List[int] = None,
               is_adaptive: bool = None,
               is_idea_compatible: bool = None,
               intro_video: dict = None,
               authors: List[int] = None,
               tags: List[int] = None,
               is_enabled: bool = None,
               language: str = None,
               is_public: bool = None,
               begin_date_source: str = None,
               end_date_source: str = None,
               soft_deadline_source: str = None,
               hard_deadline_source: str = None,
               grading_policy_source: str = None,
               lti_consumer_key: str = None,
               lti_secret_key: str = None,
               lti_private_profile: bool = None,
               **kwargs) -> Course:
        vars = locals().copy()
        data = {'course':
                    {k: v for k, v in {**vars, **kwargs}.items()
                     if k != 'self' and v is not None}}

        response = self._stepik._post('courses', data)
        if 'courses' not in response:
            raise StepikError(response)

        return Course(self._stepik, response['courses'][0])


    def update(self, obj: Course) -> Course:
        required = ['title', 'summary', 'workload', 'intro', 'course_format', 'target_audience', 'is_certificate_auto_issued', 'certificate_regular_threshold', 'certificate_distinction_threshold', 'instructors', 'certificate', 'requirements', 'description', 'sections', 'is_adaptive', 'is_idea_compatible', 'intro_video', 'authors', 'tags', 'is_enabled', 'language', 'is_public', 'begin_date_source', 'end_date_source', 'soft_deadline_source', 'hard_deadline_source', 'grading_policy_source', 'lti_consumer_key', 'lti_secret_key', 'lti_private_profile']
        vars = obj._data
        data = {'course':
                    {k: v for k, v in vars.items()
                     if k != 'self' and v is not None and k in required }}

        response = self._stepik._put(f'courses/{ obj.id }', data)
        if 'courses' not in response:
            raise StepikError(response)

        return Course(self._stepik, response['courses'][0])

