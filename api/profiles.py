# This file is generated
from typing import List

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class Profile:
    _resources_name = 'profiles'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'Profile(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model Profile are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @property
    def first_name(self) -> str:
        return self._data['first_name']


    @first_name.setter
    def first_name(self, value: str):
        self._data['first_name'] = value


    @required
    @property
    def last_name(self) -> str:
        return self._data['last_name']


    @last_name.setter
    def last_name(self, value: str):
        self._data['last_name'] = value


    @readonly
    @property
    def full_name(self) -> str:
        return self._data['full_name']


    @property
    def is_private(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['is_private']


    @is_private.setter
    def is_private(self, value: bool):
        """
        Default value: ``False``
        """
        self._data['is_private'] = value


    @readonly
    @property
    def avatar(self) -> str:
        return self._data['avatar']


    @required
    @property
    def language(self) -> str:
        """
        Default value: ``"en"``

        Type: str
        """
        return self._data.setdefault('language', "en")


    @language.setter
    def language(self, value: str):
        """
        Default value: ``"en"``

        Type: str
        """
        self._data['language'] = value


    @property
    def city(self) -> str:
        return self._data['city']


    @city.setter
    def city(self, value: str):
        self._data['city'] = value


    @property
    def short_bio(self) -> str:
        return self._data['short_bio']


    @short_bio.setter
    def short_bio(self, value: str):
        self._data['short_bio'] = value


    @property
    def details(self) -> str:
        return self._data['details']


    @details.setter
    def details(self, value: str):
        self._data['details'] = value


    @property
    def subscribed_for_mail(self) -> bool:
        """
        Default value: ``True``
        """
        return self._data.setdefault('subscribed_for_mail', True)


    @subscribed_for_mail.setter
    def subscribed_for_mail(self, value: bool):
        """
        Default value: ``True``
        """
        self._data['subscribed_for_mail'] = value


    @property
    def notification_email_delay(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('notification_email_delay', "None")


    @notification_email_delay.setter
    def notification_email_delay(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self._data['notification_email_delay'] = value


    @readonly
    @property
    def notification_status(self) -> str:
        return self._data['notification_status']


    @readonly
    @property
    def is_staff(self) -> bool:
        """
        Designates whether the user can log into this admin site.

        Default value: ``False``
        """
        return self._data['is_staff']


    @readonly
    @property
    def is_guest(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['is_guest']


    @readonly
    @property
    def can_add_lesson(self) -> str:
        return self._data['can_add_lesson']


    @readonly
    @property
    def can_add_course(self) -> str:
        return self._data['can_add_course']


    @readonly
    @property
    def can_add_group(self) -> str:
        return self._data['can_add_group']


    @property
    def subscribed_for_marketing(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['subscribed_for_marketing']


    @subscribed_for_marketing.setter
    def subscribed_for_marketing(self, value: bool):
        """
        Default value: ``False``
        """
        self._data['subscribed_for_marketing'] = value


    @property
    def subscribed_for_partners(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['subscribed_for_partners']


    @subscribed_for_partners.setter
    def subscribed_for_partners(self, value: bool):
        """
        Default value: ``False``
        """
        self._data['subscribed_for_partners'] = value


    @property
    def subscribed_for_news_en(self) -> bool:
        """
        Default value: ``True``
        """
        return self._data.setdefault('subscribed_for_news_en', True)


    @subscribed_for_news_en.setter
    def subscribed_for_news_en(self, value: bool):
        """
        Default value: ``True``
        """
        self._data['subscribed_for_news_en'] = value


    @property
    def subscribed_for_news_ru(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['subscribed_for_news_ru']


    @subscribed_for_news_ru.setter
    def subscribed_for_news_ru(self, value: bool):
        """
        Default value: ``False``
        """
        self._data['subscribed_for_news_ru'] = value


    @required
    @property
    def bit_field(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['bit_field']


    @bit_field.setter
    def bit_field(self, value: int):
        """
        Default value: ``0``
        """
        self._data['bit_field'] = value


    @required
    @readonly
    @property
    def level(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['level']


    @readonly
    @property
    def level_title(self) -> str:
        return self._data['level_title']


    @readonly
    @property
    def level_abilities(self) -> str:
        return self._data['level_abilities']


    @readonly
    @property
    def has_password(self) -> str:
        return self._data['has_password']


    @readonly
    @property
    def social_accounts(self) -> str:
        return self._data['social_accounts']


    @readonly
    @property
    def email_addresses(self) -> str:
        return self._data['email_addresses']


    @readonly
    @property
    def is_email_verified(self) -> str:
        return self._data['is_email_verified']


    @readonly
    @property
    def invite_url(self) -> str:
        return self._data['invite_url']


    @readonly
    @property
    def telegram_bot_url(self) -> str:
        return self._data['telegram_bot_url']


    @required
    @readonly
    @property
    def subscription_plan(self) -> str:
        return self._data['subscription_plan']


    @readonly
    @property
    def experiment_choices(self) -> str:
        return self._data['experiment_choices']


    @readonly
    @property
    def allowed_private_courses_count(self) -> str:
        return self._data['allowed_private_courses_count']


    @property
    def is_web_push_enabled(self) -> bool:
        """
        Default value: ``True``
        """
        return self._data.setdefault('is_web_push_enabled', True)


    @is_web_push_enabled.setter
    def is_web_push_enabled(self, value: bool):
        """
        Default value: ``True``
        """
        self._data['is_web_push_enabled'] = value


