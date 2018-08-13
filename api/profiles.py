# This file is generated
from common import required, readonly
from typing import List


class WriteProfile:
    def __init__(self, data):
        self.__data = data


    @required
    @property
    def first_name(self) -> str:
        return self.__data['first_name']


    @first_name.setter
    def first_name(self, value: str):
        self.__data['first_name'] = value


    @required
    @property
    def last_name(self) -> str:
        return self.__data['last_name']


    @last_name.setter
    def last_name(self, value: str):
        self.__data['last_name'] = value


    @property
    def is_private(self) -> bool:
        """
        default value: False
        """
        return self.__data['is_private']


    @is_private.setter
    def is_private(self, value: bool):
        """
        default value: False
        """
        self.__data['is_private'] = value


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
    def city(self) -> str:
        return self.__data['city']


    @city.setter
    def city(self, value: str):
        self.__data['city'] = value


    @property
    def short_bio(self) -> str:
        return self.__data['short_bio']


    @short_bio.setter
    def short_bio(self, value: str):
        self.__data['short_bio'] = value


    @property
    def details(self) -> str:
        return self.__data['details']


    @details.setter
    def details(self, value: str):
        self.__data['details'] = value


    @property
    def subscribed_for_mail(self) -> bool:
        """
        default value: True
        """
        return self.__data.setdefault('subscribed_for_mail', True)


    @subscribed_for_mail.setter
    def subscribed_for_mail(self, value: bool):
        """
        default value: True
        """
        self.__data['subscribed_for_mail'] = value


    @property
    def notification_email_delay(self) -> str:
        """
        Type: choice
        """
        return self.__data['notification_email_delay']


    @notification_email_delay.setter
    def notification_email_delay(self, value: str):
        """
        Type: choice
        """
        self.__data['notification_email_delay'] = value


    @property
    def subscribed_for_marketing(self) -> bool:
        """
        default value: False
        """
        return self.__data['subscribed_for_marketing']


    @subscribed_for_marketing.setter
    def subscribed_for_marketing(self, value: bool):
        """
        default value: False
        """
        self.__data['subscribed_for_marketing'] = value


    @property
    def subscribed_for_partners(self) -> bool:
        """
        default value: False
        """
        return self.__data['subscribed_for_partners']


    @subscribed_for_partners.setter
    def subscribed_for_partners(self, value: bool):
        """
        default value: False
        """
        self.__data['subscribed_for_partners'] = value


    @property
    def subscribed_for_news_en(self) -> bool:
        """
        default value: True
        """
        return self.__data.setdefault('subscribed_for_news_en', True)


    @subscribed_for_news_en.setter
    def subscribed_for_news_en(self, value: bool):
        """
        default value: True
        """
        self.__data['subscribed_for_news_en'] = value


    @property
    def subscribed_for_news_ru(self) -> bool:
        """
        default value: False
        """
        return self.__data['subscribed_for_news_ru']


    @subscribed_for_news_ru.setter
    def subscribed_for_news_ru(self, value: bool):
        """
        default value: False
        """
        self.__data['subscribed_for_news_ru'] = value


    @required
    @property
    def bit_field(self) -> int:
        """
        default value: 0
        """
        return self.__data['bit_field']


    @bit_field.setter
    def bit_field(self, value: int):
        """
        default value: 0
        """
        self.__data['bit_field'] = value


    @property
    def is_web_push_enabled(self) -> bool:
        """
        default value: True
        """
        return self.__data.setdefault('is_web_push_enabled', True)


    @is_web_push_enabled.setter
    def is_web_push_enabled(self, value: bool):
        """
        default value: True
        """
        self.__data['is_web_push_enabled'] = value


class Profile:
    def __init__(self, data):
        self.__data = data


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @required
    @property
    def first_name(self) -> str:
        return self.__data['first_name']


    @first_name.setter
    def first_name(self, value: str):
        self.__data['first_name'] = value


    @required
    @property
    def last_name(self) -> str:
        return self.__data['last_name']


    @last_name.setter
    def last_name(self, value: str):
        self.__data['last_name'] = value


    @readonly
    @property
    def full_name(self) -> str:
        return self.__data['full_name']


    @property
    def is_private(self) -> bool:
        """
        default value: False
        """
        return self.__data['is_private']


    @is_private.setter
    def is_private(self, value: bool):
        """
        default value: False
        """
        self.__data['is_private'] = value


    @readonly
    @property
    def avatar(self) -> str:
        return self.__data['avatar']


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
    def city(self) -> str:
        return self.__data['city']


    @city.setter
    def city(self, value: str):
        self.__data['city'] = value


    @property
    def short_bio(self) -> str:
        return self.__data['short_bio']


    @short_bio.setter
    def short_bio(self, value: str):
        self.__data['short_bio'] = value


    @property
    def details(self) -> str:
        return self.__data['details']


    @details.setter
    def details(self, value: str):
        self.__data['details'] = value


    @property
    def subscribed_for_mail(self) -> bool:
        """
        default value: True
        """
        return self.__data.setdefault('subscribed_for_mail', True)


    @subscribed_for_mail.setter
    def subscribed_for_mail(self, value: bool):
        """
        default value: True
        """
        self.__data['subscribed_for_mail'] = value


    @property
    def notification_email_delay(self) -> str:
        """
        Type: choice
        """
        return self.__data['notification_email_delay']


    @notification_email_delay.setter
    def notification_email_delay(self, value: str):
        """
        Type: choice
        """
        self.__data['notification_email_delay'] = value


    @readonly
    @property
    def notification_status(self) -> str:
        return self.__data['notification_status']


    @readonly
    @property
    def is_staff(self) -> bool:
        """
        Designates whether the user can log into this admin site.

        default value: False
        """
        return self.__data['is_staff']


    @readonly
    @property
    def is_guest(self) -> bool:
        """
        default value: False
        """
        return self.__data['is_guest']


    @readonly
    @property
    def can_add_lesson(self) -> str:
        return self.__data['can_add_lesson']


    @readonly
    @property
    def can_add_course(self) -> str:
        return self.__data['can_add_course']


    @readonly
    @property
    def can_add_group(self) -> str:
        return self.__data['can_add_group']


    @property
    def subscribed_for_marketing(self) -> bool:
        """
        default value: False
        """
        return self.__data['subscribed_for_marketing']


    @subscribed_for_marketing.setter
    def subscribed_for_marketing(self, value: bool):
        """
        default value: False
        """
        self.__data['subscribed_for_marketing'] = value


    @property
    def subscribed_for_partners(self) -> bool:
        """
        default value: False
        """
        return self.__data['subscribed_for_partners']


    @subscribed_for_partners.setter
    def subscribed_for_partners(self, value: bool):
        """
        default value: False
        """
        self.__data['subscribed_for_partners'] = value


    @property
    def subscribed_for_news_en(self) -> bool:
        """
        default value: True
        """
        return self.__data.setdefault('subscribed_for_news_en', True)


    @subscribed_for_news_en.setter
    def subscribed_for_news_en(self, value: bool):
        """
        default value: True
        """
        self.__data['subscribed_for_news_en'] = value


    @property
    def subscribed_for_news_ru(self) -> bool:
        """
        default value: False
        """
        return self.__data['subscribed_for_news_ru']


    @subscribed_for_news_ru.setter
    def subscribed_for_news_ru(self, value: bool):
        """
        default value: False
        """
        self.__data['subscribed_for_news_ru'] = value


    @required
    @property
    def bit_field(self) -> int:
        """
        default value: 0
        """
        return self.__data['bit_field']


    @bit_field.setter
    def bit_field(self, value: int):
        """
        default value: 0
        """
        self.__data['bit_field'] = value


    @required
    @readonly
    @property
    def level(self) -> int:
        """
        default value: 0
        """
        return self.__data['level']


    @readonly
    @property
    def level_title(self) -> str:
        return self.__data['level_title']


    @readonly
    @property
    def level_abilities(self) -> str:
        return self.__data['level_abilities']


    @readonly
    @property
    def has_password(self) -> str:
        return self.__data['has_password']


    @readonly
    @property
    def social_accounts(self) -> str:
        return self.__data['social_accounts']


    @readonly
    @property
    def email_addresses(self) -> str:
        return self.__data['email_addresses']


    @readonly
    @property
    def is_email_verified(self) -> str:
        return self.__data['is_email_verified']


    @readonly
    @property
    def invite_url(self) -> str:
        return self.__data['invite_url']


    @readonly
    @property
    def telegram_bot_url(self) -> str:
        return self.__data['telegram_bot_url']


    @required
    @readonly
    @property
    def subscription_plan(self) -> str:
        return self.__data['subscription_plan']


    @readonly
    @property
    def experiment_choices(self) -> str:
        return self.__data['experiment_choices']


    @readonly
    @property
    def allowed_private_courses_count(self) -> str:
        return self.__data['allowed_private_courses_count']


    @property
    def is_web_push_enabled(self) -> bool:
        """
        default value: True
        """
        return self.__data.setdefault('is_web_push_enabled', True)


    @is_web_push_enabled.setter
    def is_web_push_enabled(self, value: bool):
        """
        default value: True
        """
        self.__data['is_web_push_enabled'] = value


