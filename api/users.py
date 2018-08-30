# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class User:
    _resources_name = 'users'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'User(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model User are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @readonly
    @property
    def profile(self) -> str:
        return self._data['profile']


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
    def is_active(self) -> bool:
        """
        Designates whether this user should be treated as active. Unselect this instead of deleting accounts.

        Default value: ``True``
        """
        return self._data.setdefault('is_active', True)


    @readonly
    @property
    def is_guest(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['is_guest']


    @readonly
    @property
    def is_organization(self) -> bool:
        """
        Default value: ``False``
        """
        return self._data['is_organization']


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
    def first_name(self) -> str:
        return self._data['first_name']


    @first_name.setter
    def first_name(self, value: str):
        self._data['first_name'] = value


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


    @readonly
    @property
    def alias(self) -> str:
        return self._data['alias']


    @readonly
    @property
    def avatar(self) -> str:
        return self._data['avatar']


    @readonly
    @property
    def cover(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('cover', "None")


    @readonly
    @property
    def city(self) -> str:
        return self._data['city']


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


    @required
    @readonly
    @property
    def knowledge(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['knowledge']


    @readonly
    @property
    def knowledge_rank(self) -> int:
        return self._data['knowledge_rank']


    @required
    @readonly
    @property
    def reputation(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['reputation']


    @readonly
    @property
    def reputation_rank(self) -> int:
        return self._data['reputation_rank']


    @readonly
    @property
    def join_date(self) -> str:
        return self._data['join_date']


    @readonly
    @property
    def social_profiles(self) -> str:
        return self._data['social_profiles']


    @required
    @readonly
    @property
    def solved_steps_count(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['solved_steps_count']


    @required
    @readonly
    @property
    def created_courses_count(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['created_courses_count']


    @required
    @readonly
    @property
    def created_lessons_count(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['created_lessons_count']


    @required
    @readonly
    @property
    def issued_certificates_count(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['issued_certificates_count']


    @required
    @readonly
    @property
    def followers_count(self) -> int:
        """
        Default value: ``0``
        """
        return self._data['followers_count']




class ListOfUsers:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> User:
        return User(self._stepik, self._stepik._fetch_object(User, id))


    def get_all(self, ids: List[int], keep_order=False) -> Iterable[User]:
        objects = self._stepik._fetch_objects(User, ids)
        iterable = (User(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)


    def create(self, is_private: bool = None, short_bio: str = None, details: str = None, first_name: str = None, last_name: str = None) -> User:
        vars = locals().copy()
        data = {'user': {k: v for k, v in vars.items() if k != 'self' and v is not None}}

        resources_name = 'users'
        response = self._stepik._post(resources_name, data)

        if resources_name not in response:
            raise StepikError(response)

        return User(self._stepik, response[resources_name][0])
