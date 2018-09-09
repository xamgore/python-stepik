# This file is generated
from typing import List, Iterable, Any, Optional

from stepik.errors import StepikError
from stepik.common import required, readonly
from stepik.resources_list import ResourcesList


class User:
    """
    User resource.
    """

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
        obj = self._stepik._fetch_object(User, id)
        return User(self._stepik, obj)


    def get_all(self, ids: Iterable[int], keep_order=False) -> Iterable[User]:
        """
        Grab a bunch of ids, usually 20 objects per request.
        """
        if keep_order:
            ids = list(ids)

        objects = self._stepik._fetch_objects(User, ids)
        iterable = (User(self._stepik, o) for o in objects)

        return iterable if not keep_order \
            else sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))


    def iterate(self,
                alias: Any = None,
                order: Any = None,
                by_id: bool = None,
                by_reputation: bool = None,
                by_knowledge_rank: bool = None,
                by_knowledge: bool = None,
                by_reputation_rank: bool = None,
                skip: int = 0, limit: Optional[int] = 20) -> Iterable[User]:
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
            page = self._stepik._get(f'users?{params}&page={page_idx}&order={ordering}')

            for obj in page['users']:
                if limit and count >= limit:
                    break

                yield User(self._stepik, obj)
                count += 1

            if not page['meta']['has_next']:
                break

            page_idx += 1


    def __iter__(self):
        yield from self.iterate(limit=None)


    def create(self,
               email: str,
               is_private: bool = None,
               short_bio: str = None,
               details: str = None,
               first_name: str = None,
               last_name: str = None,
               **kwargs) -> User:
        vars = locals().copy()
        data = {'user':
                    {k: v for k, v in {**vars, **kwargs}.items()
                     if k != 'self' and v is not None}}

        response = self._stepik._post('users', data)
        if 'users' not in response:
            raise StepikError(response)

        return User(self._stepik, response['users'][0])

