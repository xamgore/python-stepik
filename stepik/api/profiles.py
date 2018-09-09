# This file is generated
from typing import List, Iterable, Any, Optional

from stepik.errors import StepikError
from stepik.common import required, readonly
from stepik.resources_list import ResourcesList


class Profile:
    """
    User profile resource.
    """

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




class ListOfProfiles:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> Profile:
        obj = self._stepik._fetch_object(Profile, id)
        return Profile(self._stepik, obj)


    def get_all(self, ids: Iterable[int], keep_order=False) -> Iterable[Profile]:
        """
        Grab a bunch of ids, usually 20 objects per request.
        """
        if keep_order:
            ids = list(ids)

        objects = self._stepik._fetch_objects(Profile, ids)
        iterable = (Profile(self._stepik, o) for o in objects)

        return iterable if not keep_order \
            else sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))


    def iterate(self,
                skip: int = 0, limit: Optional[int] = 20) -> Iterable[Profile]:
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
            page = self._stepik._get(f'profiles?{params}&page={page_idx}&order={ordering}')

            for obj in page['profiles']:
                if limit and count >= limit:
                    break

                yield Profile(self._stepik, obj)
                count += 1

            if not page['meta']['has_next']:
                break

            page_idx += 1


    def __iter__(self):
        yield from self.iterate(limit=None)

