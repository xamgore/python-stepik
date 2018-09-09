# This file is generated
from typing import List, Iterable, Any, Optional

from stepik.errors import StepikError
from stepik.common import required, readonly
from stepik.resources_list import ResourcesList
from .users import User


class Stepics:
    _resources_name = 'stepics'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'Stepics(id={self.user!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model Stepics are missing')


    def user(self) -> User:
        return User(self._stepik, self._stepik._fetch_object(User, self.user_id))


    def profile(self) -> User:
        return User(self._stepik, self._stepik._fetch_object(User, self.user_id))


    @property
    def total_quizzes(self) -> int:
        return self._data['total_quizzes']


    @total_quizzes.setter
    def total_quizzes(self, value: int):
        self._data['total_quizzes'] = value


    @property
    def total_active(self) -> int:
        return self._data['total_active']


    @total_active.setter
    def total_active(self, value: int):
        self._data['total_active'] = value


    @property
    def total_submissions(self) -> int:
        return self._data['total_submissions']


    @total_submissions.setter
    def total_submissions(self, value: int):
        self._data['total_submissions'] = value


    @property
    def config(self) -> dict:
        """
        Some trash actively used on the frontend.

        See `server's response <https://stepik.org/api/docs/#!/stepics>`_ to get more information.

        Type: dict
        """
        return self._data['config']


    @config.setter
    def config(self, value: dict):
        """
        Some trash actively used on the frontend.

        See `server's response <https://stepik.org/api/docs/#!/stepics>`_ to get more information.

        Type: dict
        """
        self._data['config'] = value


    @property
    def server_time(self) -> float:
        return self._data['server_time']


    @server_time.setter
    def server_time(self, value: float):
        self._data['server_time'] = value


    @property
    def user_id(self) -> int:
        """
        :class:`Profile`'s id
        """
        return self._data['profile']


    @user_id.setter
    def user_id(self, value: int):
        """
        :class:`Profile`'s id
        """
        self._data['profile'] = value


