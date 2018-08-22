# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class WriteCourse:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'WriteCourse(id={self.id!r})'


    @property
    def summary(self) -> str:
        return self.__data['summary']


    @summary.setter
    def summary(self, value: str):
        self.__data['summary'] = value


    @property
    def workload(self) -> str:
        return self.__data['workload']


    @workload.setter
    def workload(self, value: str):
        self.__data['workload'] = value


    @property
    def intro(self) -> str:
        """
        Type: url
        """
        return self.__data['intro']


    @intro.setter
    def intro(self, value: str):
        """
        Type: url
        """
        self.__data['intro'] = value


    @property
    def course_format(self) -> str:
        return self.__data['course_format']


    @course_format.setter
    def course_format(self, value: str):
        self.__data['course_format'] = value


    @property
    def target_audience(self) -> str:
        return self.__data['target_audience']


    @target_audience.setter
    def target_audience(self, value: str):
        self.__data['target_audience'] = value


    @property
    def is_certificate_auto_issued(self) -> bool:
        """
        Default value: ``False``
        """
        return self.__data['is_certificate_auto_issued']


    @is_certificate_auto_issued.setter
    def is_certificate_auto_issued(self, value: bool):
        """
        Default value: ``False``
        """
        self.__data['is_certificate_auto_issued'] = value


    @property
    def certificate_regular_threshold(self) -> int:
        """
        Default value: ``0``
        """
        return self.__data['certificate_regular_threshold']


    @certificate_regular_threshold.setter
    def certificate_regular_threshold(self, value: int):
        """
        Default value: ``0``
        """
        self.__data['certificate_regular_threshold'] = value


    @property
    def certificate_distinction_threshold(self) -> int:
        """
        Default value: ``0``
        """
        return self.__data['certificate_distinction_threshold']


    @certificate_distinction_threshold.setter
    def certificate_distinction_threshold(self, value: int):
        """
        Default value: ``0``
        """
        self.__data['certificate_distinction_threshold'] = value


    @property
    def instructors(self) -> str:
        return self.__data['instructors']


    @instructors.setter
    def instructors(self, value: str):
        self.__data['instructors'] = value


    @property
    def certificate(self) -> str:
        return self.__data['certificate']


    @certificate.setter
    def certificate(self, value: str):
        self.__data['certificate'] = value


    @property
    def requirements(self) -> str:
        return self.__data['requirements']


    @requirements.setter
    def requirements(self, value: str):
        self.__data['requirements'] = value


    @property
    def description(self) -> str:
        return self.__data['description']


    @description.setter
    def description(self, value: str):
        self.__data['description'] = value


    @required
    @property
    def sections(self) -> str:
        return self.__data['sections']


    @sections.setter
    def sections(self, value: str):
        self.__data['sections'] = value


    @property
    def is_adaptive(self) -> bool:
        """
        Default value: ``False``
        """
        return self.__data['is_adaptive']


    @is_adaptive.setter
    def is_adaptive(self, value: bool):
        """
        Default value: ``False``
        """
        self.__data['is_adaptive'] = value


    @property
    def is_idea_compatible(self) -> bool:
        """
        Default value: ``False``
        """
        return self.__data['is_idea_compatible']


    @is_idea_compatible.setter
    def is_idea_compatible(self, value: bool):
        """
        Default value: ``False``
        """
        self.__data['is_idea_compatible'] = value


    @property
    def intro_video(self) -> str:
        return self.__data['intro_video']


    @intro_video.setter
    def intro_video(self, value: str):
        self.__data['intro_video'] = value


    @property
    def authors(self) -> str:
        return self.__data['authors']


    @authors.setter
    def authors(self, value: str):
        self.__data['authors'] = value


    @property
    def tags(self) -> str:
        return self.__data['tags']


    @tags.setter
    def tags(self, value: str):
        self.__data['tags'] = value


    @property
    def is_enabled(self) -> bool:
        """
        Default value: ``True``
        """
        return self.__data.setdefault('is_enabled', True)


    @is_enabled.setter
    def is_enabled(self, value: bool):
        """
        Default value: ``True``
        """
        self.__data['is_enabled'] = value


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
    def begin_date_source(self) -> str:
        """
        Type: datetime
        """
        return self.__data['begin_date_source']


    @begin_date_source.setter
    def begin_date_source(self, value: str):
        """
        Type: datetime
        """
        self.__data['begin_date_source'] = value


    @property
    def end_date_source(self) -> str:
        """
        Type: datetime
        """
        return self.__data['end_date_source']


    @end_date_source.setter
    def end_date_source(self, value: str):
        """
        Type: datetime
        """
        self.__data['end_date_source'] = value


    @property
    def soft_deadline_source(self) -> str:
        """
        Type: datetime
        """
        return self.__data['soft_deadline_source']


    @soft_deadline_source.setter
    def soft_deadline_source(self, value: str):
        """
        Type: datetime
        """
        self.__data['soft_deadline_source'] = value


    @property
    def hard_deadline_source(self) -> str:
        """
        Type: datetime
        """
        return self.__data['hard_deadline_source']


    @hard_deadline_source.setter
    def hard_deadline_source(self, value: str):
        """
        Type: datetime
        """
        self.__data['hard_deadline_source'] = value


    @property
    def grading_policy_source(self) -> str:
        """
        Type: choice
        """
        return self.__data['grading_policy_source']


    @grading_policy_source.setter
    def grading_policy_source(self, value: str):
        """
        Type: choice
        """
        self.__data['grading_policy_source'] = value


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


from api.sections import Section
from api.users import User
from api.groups import Group
from api.tags import Tag


class Course:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'Course(id={self.id!r})'


    @property
    def sections(self) -> ResourcesList[Section]:
        return ResourcesList[Section](Section, self.__stepik, self, 'sections_ids')


    @property
    def authors(self) -> ResourcesList[User]:
        return ResourcesList[User](User, self.__stepik, self, 'authors_ids')


    @property
    def tags(self) -> ResourcesList[Tag]:
        return ResourcesList[Tag](Tag, self.__stepik, self, 'tags_ids')


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
        """
        Course's unique identifier
        """
        return self.__data['id']


    @property
    def summary(self) -> str:
        """
        Short description about the course, may contain HTML tags
        """
        return self.__data['summary']


    @summary.setter
    def summary(self, value: str):
        """
        Short description about the course, may contain HTML tags
        """
        self.__data['summary'] = value


    @property
    def workload(self) -> str:
        return self.__data['workload']


    @workload.setter
    def workload(self, value: str):
        self.__data['workload'] = value


    @readonly
    @property
    def cover(self) -> str:
        """
        Path to the cover image, without the hostname, i.e. ``/media/...1c67c.png``.

        May take ``None`` value.

        Type: file upload
        """
        return self.__data['cover']


    @property
    def intro(self) -> str:
        """
        Link to the introduction video (with html5 player), that may explain what is the course about.

        Default value: ``""``
        """
        return self.__data.setdefault('intro', "")


    @intro.setter
    def intro(self, value: str):
        """
        Link to the introduction video (with html5 player), that may explain what is the course about.

        Default value: ``""``
        """
        self.__data['intro'] = value


    @property
    def course_format(self) -> str:
        """
        Default value: ````
        """
        return self.__data['course_format']


    @course_format.setter
    def course_format(self, value: str):
        """
        Default value: ````
        """
        self.__data['course_format'] = value


    @property
    def target_audience(self) -> str:
        """
        Default value: ````
        """
        return self.__data['target_audience']


    @target_audience.setter
    def target_audience(self, value: str):
        """
        Default value: ````
        """
        self.__data['target_audience'] = value


    @readonly
    @property
    def certificate_footer(self) -> str:
        """
        May take ``None`` value.

        Type: file upload
        """
        return self.__data['certificate_footer']


    @readonly
    @property
    def certificate_cover_org(self) -> str:
        """
        Type: file upload
        """
        return self.__data['certificate_cover_org']


    @property
    def is_certificate_auto_issued(self) -> bool:
        """
        Default value: ``False``
        """
        return self.__data['is_certificate_auto_issued']


    @is_certificate_auto_issued.setter
    def is_certificate_auto_issued(self, value: bool):
        """
        Default value: ``False``
        """
        self.__data['is_certificate_auto_issued'] = value


    @property
    def certificate_regular_threshold(self) -> int:
        """
        Default value: ``0``
        """
        return self.__data['certificate_regular_threshold']


    @certificate_regular_threshold.setter
    def certificate_regular_threshold(self, value: int):
        """
        Default value: ``0``
        """
        self.__data['certificate_regular_threshold'] = value


    @property
    def certificate_distinction_threshold(self) -> int:
        """
        Default value: ``0``
        """
        return self.__data['certificate_distinction_threshold']


    @certificate_distinction_threshold.setter
    def certificate_distinction_threshold(self, value: int):
        """
        Default value: ``0``
        """
        self.__data['certificate_distinction_threshold'] = value


    @property
    def instructors(self) -> List[int]:
        return self.__data['instructors']


    @instructors.setter
    def instructors(self, value: List[int]):
        self.__data['instructors'] = value


    @property
    def certificate(self) -> str:
        return self.__data['certificate']


    @certificate.setter
    def certificate(self, value: str):
        self.__data['certificate'] = value


    @property
    def requirements(self) -> str:
        return self.__data['requirements']


    @requirements.setter
    def requirements(self, value: str):
        self.__data['requirements'] = value


    @property
    def description(self) -> str:
        """
        Full description about the course, may contain HTML tags
        """
        return self.__data['description']


    @description.setter
    def description(self, value: str):
        """
        Full description about the course, may contain HTML tags
        """
        self.__data['description'] = value


    @readonly
    @property
    def total_units(self) -> int:
        """
        Total number of units
        """
        return self.__data['total_units']


    @readonly
    @property
    def enrollment(self) -> int:
        """
        Enrollment id (which usually is equals to course id), if user enrolled. If not, ``None``.
        """
        return self.__data['enrollment']


    @readonly
    @property
    def is_favorite(self) -> bool:
        """
        Is the course is favourite. See ``favorite_courses`` list.
        """
        return self.__data['is_favorite']


    @readonly
    @property
    def actions(self) -> dict:
        """
        Contains a dict of ``<action : link to the page>``. If user is not an admin or the course owner, dict is empty.
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
    def first_lesson(self) -> int:
        return self.__data['first_lesson']


    @readonly
    @property
    def first_unit(self) -> str:
        return self.__data['first_unit']


    @readonly
    @property
    def certificate_link(self) -> str:
        return self.__data['certificate_link']


    @readonly
    @property
    def certificate_regular_link(self) -> str:
        return self.__data['certificate_regular_link']


    @readonly
    @property
    def certificate_distinction_link(self) -> str:
        return self.__data['certificate_distinction_link']


    @readonly
    @property
    def schedule_link(self) -> str:
        """
        Path to the ``ics``, without the host name
        """
        return self.__data['schedule_link']


    @readonly
    @property
    def schedule_long_link(self) -> str:
        """
        Path to the ``ics``, without the host name
        """
        return self.__data['schedule_long_link']


    @readonly
    @property
    def first_deadline(self) -> str:
        return self.__data['first_deadline']


    @readonly
    @property
    def last_deadline(self) -> str:
        return self.__data['last_deadline']


    @readonly
    @property
    def subscriptions(self) -> List[str]:
        return self.__data['subscriptions']


    @readonly
    @property
    def announcements(self) -> List[str]:
        return self.__data['announcements']


    @readonly
    @property
    def is_contest(self) -> bool:
        return self.__data['is_contest']


    @readonly
    @property
    def is_self_paced(self) -> bool:
        """
        Completely open course, without deadlines and other things
        """
        return self.__data['is_self_paced']


    @property
    def is_adaptive(self) -> bool:
        """
        Adaptive means that course is based on tasks, which can be marked as easy or hard. Stepik will give better tasks next time.

        Default value: ``False``
        """
        return self.__data['is_adaptive']


    @is_adaptive.setter
    def is_adaptive(self, value: bool):
        """
        Adaptive means that course is based on tasks, which can be marked as easy or hard. Stepik will give better tasks next time.

        Default value: ``False``
        """
        self.__data['is_adaptive'] = value


    @property
    def is_idea_compatible(self) -> bool:
        """
        Default value: ``False``
        """
        import warnings; warnings.warn('This function is deprecated', DeprecationWarning)
        return self.__data['is_idea_compatible']


    @is_idea_compatible.setter
    def is_idea_compatible(self, value: bool):
        """
        Default value: ``False``
        """
        import warnings; warnings.warn('This function is deprecated', DeprecationWarning)
        self.__data['is_idea_compatible'] = value


    @readonly
    @property
    def last_step(self) -> int:
        return self.__data['last_step']


    @property
    def intro_video(self) -> dict:
        """
        Dict with following fields:

        * thumbnail — full url to image
        * urls — list of ``{quality, url}``
        * duration — in seconds
        * upload_date — isoformat
        * filename
        """
        return self.__data['intro_video']


    @intro_video.setter
    def intro_video(self, value: dict):
        """
        Dict with following fields:

        * thumbnail — full url to image
        * urls — list of ``{quality, url}``
        * duration — in seconds
        * upload_date — isoformat
        * filename
        """
        self.__data['intro_video'] = value


    @readonly
    @property
    def social_providers(self) -> str:
        return self.__data['social_providers']


    @readonly
    @property
    def has_tutors(self) -> bool:
        """
        Default value: ``False``
        """
        return self.__data['has_tutors']


    @readonly
    @property
    def is_promoted(self) -> bool:
        """
        Default value: ``False``
        """
        return self.__data['is_promoted']


    @property
    def is_enabled(self) -> bool:
        """
        Default value: ``True``
        """
        return self.__data.setdefault('is_enabled', True)


    @is_enabled.setter
    def is_enabled(self, value: bool):
        """
        Default value: ``True``
        """
        self.__data['is_enabled'] = value


    @readonly
    @property
    def is_proctored(self) -> bool:
        """
        Default value: ``False``
        """
        return self.__data['is_proctored']


    @readonly
    @property
    def proctor_url(self) -> str:
        """
        May take ``None`` value.

        Type: url
        """
        return self.__data['proctor_url']


    @required
    @readonly
    @property
    def review_summary(self) -> int:
        return self.__data['review_summary']


    @readonly
    @property
    def schedule_type(self) -> str:
        """
        Type: choice
        """
        return self.__data['schedule_type']


    @required
    @readonly
    @property
    def certificates_count(self) -> int:
        """
        Default value: ``0``
        """
        return self.__data['certificates_count']


    @required
    @readonly
    @property
    def learners_count(self) -> int:
        """
        Number of learners enrolled

        Default value: ``0``
        """
        return self.__data['learners_count']


    @readonly
    @property
    def time_to_complete(self) -> int:
        """
        Average time to complete the course
        """
        return self.__data['time_to_complete']


    @readonly
    @property
    def is_popular(self) -> bool:
        """
        Default value: ``False``
        """
        return self.__data['is_popular']


    @readonly
    @property
    def similar_courses(self) -> List[int]:
        return self.__data['similar_courses']


    @readonly
    @property
    def is_unsuitable(self) -> bool:
        """
        Does course contain information unsuitable for a wide audience? (how to drink alcohol at work)

        Default value: ``False``
        """
        return self.__data['is_unsuitable']


    @readonly
    @property
    def is_paid(self) -> bool:
        """
        Default value: ``False``
        """
        return self.__data['is_paid']


    @readonly
    @property
    def price(self) -> float:
        return self.__data['price']


    @readonly
    @property
    def currency_code(self) -> str:
        """
        Type: choice
        """
        return self.__data['currency_code']


    @readonly
    @property
    def display_price(self) -> str:
        return self.__data['display_price']


    @readonly
    @property
    def continue_url(self) -> str:
        return self.__data['continue_url']


    @required
    @readonly
    @property
    def readiness(self) -> str:
        """
        Default value: ``"0"``
        """
        return self.__data.setdefault('readiness', "0")


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
        Title of the course
        """
        return self.__data['title']


    @title.setter
    def title(self, value: str):
        """
        Title of the course
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
    def begin_date(self) -> str:
        """
        Open date: when the course starts for enrolled users.

        Use `begin_date_source` to update the value.

        Type: datetime
        """
        return self.__data['begin_date']


    @readonly
    @property
    def end_date(self) -> str:
        """
        Close date: when the module will be disabled (close date is usually left empty).

        Use `end_date_source` to update the value.

        Type: datetime
        """
        return self.__data['end_date']


    @readonly
    @property
    def soft_deadline(self) -> str:
        """
        Soft deadline: when the cost of every step will be reduced.

        Use `soft_deadline_source` to update the value.

        Type: datetime
        """
        return self.__data['soft_deadline']


    @readonly
    @property
    def hard_deadline(self) -> str:
        """
        Hard deadline: when the cost of every step will be zero.

        Use `hard_deadline_source` to update the value.

        Type: datetime
        """
        return self.__data['hard_deadline']


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

        Type: choice
        """
        return self.__data['grading_policy']


    @property
    def begin_date_source(self) -> str:
        """
        Open date: when the module starts for enrolled users

        Use `begin_date_source` to update the value.

        Type: datetime
        """
        return self.__data['begin_date_source']


    @begin_date_source.setter
    def begin_date_source(self, value: str):
        """
        Open date: when the module starts for enrolled users

        Use `begin_date_source` to update the value.

        Type: datetime
        """
        self.__data['begin_date_source'] = value


    @property
    def end_date_source(self) -> str:
        """
        Close date: when the module will be disabled (close date is usually left empty).

        Use `end_date_source` to update the value.

        Type: datetime
        """
        return self.__data['end_date_source']


    @end_date_source.setter
    def end_date_source(self, value: str):
        """
        Close date: when the module will be disabled (close date is usually left empty).

        Use `end_date_source` to update the value.

        Type: datetime
        """
        self.__data['end_date_source'] = value


    @property
    def soft_deadline_source(self) -> str:
        """
        Soft deadline: when the cost of every step will be reduced.

        Use `soft_deadline_source` to update the value.

        Type: datetime
        """
        return self.__data['soft_deadline_source']


    @soft_deadline_source.setter
    def soft_deadline_source(self, value: str):
        """
        Soft deadline: when the cost of every step will be reduced.

        Use `soft_deadline_source` to update the value.

        Type: datetime
        """
        self.__data['soft_deadline_source'] = value


    @property
    def hard_deadline_source(self) -> str:
        """
        Hard deadline: when the cost of every step will be zero.

        Use `hard_deadline_source` to update the value.

        Type: datetime
        """
        return self.__data['hard_deadline_source']


    @hard_deadline_source.setter
    def hard_deadline_source(self, value: str):
        """
        Hard deadline: when the cost of every step will be zero.

        Use `hard_deadline_source` to update the value.

        Type: datetime
        """
        self.__data['hard_deadline_source'] = value


    @property
    def grading_policy_source(self) -> str:
        """
        Policy can be one of these:

        * ``None`` — default for the course
        * ``"no_deadlines"`` — no deadlines
        * ``"halved"`` — half points
        * ``"linear"`` — linear descending

        Use `grading_policy_source` to update the value.

        Type: choice
        """
        return self.__data['grading_policy_source']


    @grading_policy_source.setter
    def grading_policy_source(self, value: str):
        """
        Policy can be one of these:

        * ``None`` — default for the course
        * ``"no_deadlines"`` — no deadlines
        * ``"halved"`` — half points
        * ``"linear"`` — linear descending

        Use `grading_policy_source` to update the value.

        Type: choice
        """
        self.__data['grading_policy_source'] = value


    @readonly
    @property
    def is_active(self) -> bool:
        return self.__data['is_active']


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
    def sections_ids(self) -> List[int]:
        """
        List of sections
        """
        return self.__data['sections']


    @sections_ids.setter
    def sections_ids(self, value: List[int]):
        """
        List of sections
        """
        self.__data['sections'] = value


    @property
    def authors_ids(self) -> List[int]:
        """
        List of authors, usually with the only person: course owner
        """
        return self.__data['authors']


    @authors_ids.setter
    def authors_ids(self, value: List[int]):
        """
        List of authors, usually with the only person: course owner
        """
        self.__data['authors'] = value


    @property
    def tags_ids(self) -> List[int]:
        return self.__data['tags']


    @tags_ids.setter
    def tags_ids(self, value: List[int]):
        self.__data['tags'] = value


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


