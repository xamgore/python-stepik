# This file is generated
from common import required, readonly
from typing import List


class WriteCourse:
    def __init__(self, data):
        self.__data = data


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
        default value: False
        """
        return self.__data['is_certificate_auto_issued']


    @is_certificate_auto_issued.setter
    def is_certificate_auto_issued(self, value: bool):
        """
        default value: False
        """
        self.__data['is_certificate_auto_issued'] = value


    @property
    def certificate_regular_threshold(self) -> int:
        """
        default value: 0
        """
        return self.__data['certificate_regular_threshold']


    @certificate_regular_threshold.setter
    def certificate_regular_threshold(self, value: int):
        """
        default value: 0
        """
        self.__data['certificate_regular_threshold'] = value


    @property
    def certificate_distinction_threshold(self) -> int:
        """
        default value: 0
        """
        return self.__data['certificate_distinction_threshold']


    @certificate_distinction_threshold.setter
    def certificate_distinction_threshold(self, value: int):
        """
        default value: 0
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
        default value: False
        """
        return self.__data['is_adaptive']


    @is_adaptive.setter
    def is_adaptive(self, value: bool):
        """
        default value: False
        """
        self.__data['is_adaptive'] = value


    @property
    def is_idea_compatible(self) -> bool:
        """
        default value: False
        """
        return self.__data['is_idea_compatible']


    @is_idea_compatible.setter
    def is_idea_compatible(self, value: bool):
        """
        default value: False
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
        default value: True
        """
        return self.__data.setdefault('is_enabled', True)


    @is_enabled.setter
    def is_enabled(self, value: bool):
        """
        default value: True
        """
        self.__data['is_enabled'] = value


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


class Course:
    def __init__(self, data):
        self.__data = data


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


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


    @readonly
    @property
    def cover(self) -> str:
        """
        Type: file upload
        """
        return self.__data['cover']


    @property
    def intro(self) -> str:
        """
        text, shown on the about page of the course

        Type: url
        """
        return self.__data['intro']


    @intro.setter
    def intro(self, value: str):
        """
        text, shown on the about page of the course

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


    @readonly
    @property
    def certificate_footer(self) -> str:
        """
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
        default value: False
        """
        return self.__data['is_certificate_auto_issued']


    @is_certificate_auto_issued.setter
    def is_certificate_auto_issued(self, value: bool):
        """
        default value: False
        """
        self.__data['is_certificate_auto_issued'] = value


    @property
    def certificate_regular_threshold(self) -> int:
        """
        default value: 0
        """
        return self.__data['certificate_regular_threshold']


    @certificate_regular_threshold.setter
    def certificate_regular_threshold(self, value: int):
        """
        default value: 0
        """
        self.__data['certificate_regular_threshold'] = value


    @property
    def certificate_distinction_threshold(self) -> int:
        """
        default value: 0
        """
        return self.__data['certificate_distinction_threshold']


    @certificate_distinction_threshold.setter
    def certificate_distinction_threshold(self, value: int):
        """
        default value: 0
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
    def sections(self) -> List[int]:
        """
        List of sections' ids
        """
        return self.__data['sections']


    @sections.setter
    def sections(self, value: List[int]):
        """
        List of sections' ids
        """
        self.__data['sections'] = value


    @readonly
    @property
    def total_units(self) -> str:
        return self.__data['total_units']


    @readonly
    @property
    def enrollment(self) -> str:
        return self.__data['enrollment']


    @readonly
    @property
    def is_favorite(self) -> str:
        return self.__data['is_favorite']


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
    def first_lesson(self) -> str:
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
        return self.__data['schedule_link']


    @readonly
    @property
    def schedule_long_link(self) -> str:
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
    def subscriptions(self) -> str:
        return self.__data['subscriptions']


    @readonly
    @property
    def announcements(self) -> str:
        return self.__data['announcements']


    @readonly
    @property
    def is_contest(self) -> str:
        return self.__data['is_contest']


    @readonly
    @property
    def is_self_paced(self) -> str:
        return self.__data['is_self_paced']


    @property
    def is_adaptive(self) -> bool:
        """
        default value: False
        """
        return self.__data['is_adaptive']


    @is_adaptive.setter
    def is_adaptive(self, value: bool):
        """
        default value: False
        """
        self.__data['is_adaptive'] = value


    @property
    def is_idea_compatible(self) -> bool:
        """
        default value: False
        """
        return self.__data['is_idea_compatible']


    @is_idea_compatible.setter
    def is_idea_compatible(self, value: bool):
        """
        default value: False
        """
        self.__data['is_idea_compatible'] = value


    @readonly
    @property
    def last_step(self) -> str:
        return self.__data['last_step']


    @property
    def intro_video(self) -> str:
        return self.__data['intro_video']


    @intro_video.setter
    def intro_video(self, value: str):
        self.__data['intro_video'] = value


    @readonly
    @property
    def social_providers(self) -> str:
        return self.__data['social_providers']


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


    @readonly
    @property
    def has_tutors(self) -> bool:
        """
        default value: False
        """
        return self.__data['has_tutors']


    @readonly
    @property
    def is_promoted(self) -> bool:
        """
        default value: False
        """
        return self.__data['is_promoted']


    @property
    def is_enabled(self) -> bool:
        """
        default value: True
        """
        return self.__data.setdefault('is_enabled', True)


    @is_enabled.setter
    def is_enabled(self, value: bool):
        """
        default value: True
        """
        self.__data['is_enabled'] = value


    @readonly
    @property
    def is_proctored(self) -> bool:
        """
        default value: False
        """
        return self.__data['is_proctored']


    @readonly
    @property
    def proctor_url(self) -> str:
        """
        Type: url
        """
        return self.__data['proctor_url']


    @required
    @readonly
    @property
    def review_summary(self) -> str:
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
        default value: 0
        """
        return self.__data['certificates_count']


    @required
    @readonly
    @property
    def learners_count(self) -> int:
        """
        default value: 0
        """
        return self.__data['learners_count']


    @readonly
    @property
    def time_to_complete(self) -> int:
        return self.__data['time_to_complete']


    @readonly
    @property
    def is_popular(self) -> bool:
        """
        default value: False
        """
        return self.__data['is_popular']


    @readonly
    @property
    def similar_courses(self) -> str:
        return self.__data['similar_courses']


    @readonly
    @property
    def is_unsuitable(self) -> bool:
        """
        default value: False
        """
        return self.__data['is_unsuitable']


    @readonly
    @property
    def is_paid(self) -> bool:
        """
        default value: False
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
        default value: "0"
        """
        return self.__data.setdefault('readiness', "0")


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
    def begin_date(self) -> str:
        """
        Type: datetime
        """
        return self.__data['begin_date']


    @readonly
    @property
    def end_date(self) -> str:
        """
        Type: datetime
        """
        return self.__data['end_date']


    @readonly
    @property
    def soft_deadline(self) -> str:
        """
        Type: datetime
        """
        return self.__data['soft_deadline']


    @readonly
    @property
    def hard_deadline(self) -> str:
        """
        Type: datetime
        """
        return self.__data['hard_deadline']


    @readonly
    @property
    def grading_policy(self) -> str:
        """
        Type: choice
        """
        return self.__data['grading_policy']


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


    @readonly
    @property
    def is_active(self) -> bool:
        return self.__data['is_active']


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


