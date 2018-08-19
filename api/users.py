# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class WriteUser:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'WriteUser(id={self.id!r})'


    @property
    def is_private(self) -> bool:
        """
        Default value: ``False``
        """
        return self.__data['is_private']


    @is_private.setter
    def is_private(self, value: bool):
        """
        Default value: ``False``
        """
        self.__data['is_private'] = value


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
    def first_name(self) -> str:
        return self.__data['first_name']


    @first_name.setter
    def first_name(self, value: str):
        self.__data['first_name'] = value


    @property
    def last_name(self) -> str:
        return self.__data['last_name']


    @last_name.setter
    def last_name(self, value: str):
        self.__data['last_name'] = value


    @required
    @property
    def email(self) -> str:
        """
        Type: email
        """
        return self.__data['email']


    @email.setter
    def email(self, value: str):
        """
        Type: email
        """
        self.__data['email'] = value


    @property
    def password(self) -> str:
        return self.__data['password']


    @password.setter
    def password(self, value: str):
        self.__data['password'] = value




class User:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'User(id={self.id!r})'


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @readonly
    @property
    def profile(self) -> str:
        return self.__data['profile']


    @property
    def is_private(self) -> bool:
        """
        Default value: ``False``
        """
        return self.__data['is_private']


    @is_private.setter
    def is_private(self, value: bool):
        """
        Default value: ``False``
        """
        self.__data['is_private'] = value


    @readonly
    @property
    def is_active(self) -> bool:
        """
        Designates whether this user should be treated as active. Unselect this instead of deleting accounts.

        Default value: ``True``
        """
        return self.__data.setdefault('is_active', True)


    @readonly
    @property
    def is_guest(self) -> bool:
        """
        Default value: ``False``
        """
        return self.__data['is_guest']


    @readonly
    @property
    def is_organization(self) -> bool:
        """
        Default value: ``False``
        """
        return self.__data['is_organization']


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
    def first_name(self) -> str:
        return self.__data['first_name']


    @first_name.setter
    def first_name(self, value: str):
        self.__data['first_name'] = value


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


    @readonly
    @property
    def alias(self) -> str:
        return self.__data['alias']


    @readonly
    @property
    def avatar(self) -> str:
        return self.__data['avatar']


    @readonly
    @property
    def cover(self) -> str:
        """
        Type: file upload
        """
        return self.__data['cover']


    @readonly
    @property
    def city(self) -> str:
        return self.__data['city']


    @required
    @readonly
    @property
    def level(self) -> int:
        """
        Default value: ``0``
        """
        return self.__data['level']


    @readonly
    @property
    def level_title(self) -> str:
        return self.__data['level_title']


    @required
    @readonly
    @property
    def knowledge(self) -> int:
        """
        Default value: ``0``
        """
        return self.__data['knowledge']


    @readonly
    @property
    def knowledge_rank(self) -> int:
        return self.__data['knowledge_rank']


    @required
    @readonly
    @property
    def reputation(self) -> int:
        """
        Default value: ``0``
        """
        return self.__data['reputation']


    @readonly
    @property
    def reputation_rank(self) -> int:
        return self.__data['reputation_rank']


    @readonly
    @property
    def join_date(self) -> str:
        return self.__data['join_date']


    @readonly
    @property
    def social_profiles(self) -> str:
        return self.__data['social_profiles']


    @required
    @readonly
    @property
    def solved_steps_count(self) -> int:
        """
        Default value: ``0``
        """
        return self.__data['solved_steps_count']


    @required
    @readonly
    @property
    def created_courses_count(self) -> int:
        """
        Default value: ``0``
        """
        return self.__data['created_courses_count']


    @required
    @readonly
    @property
    def created_lessons_count(self) -> int:
        """
        Default value: ``0``
        """
        return self.__data['created_lessons_count']


    @required
    @readonly
    @property
    def issued_certificates_count(self) -> int:
        """
        Default value: ``0``
        """
        return self.__data['issued_certificates_count']


    @required
    @readonly
    @property
    def followers_count(self) -> int:
        """
        Default value: ``0``
        """
        return self.__data['followers_count']


