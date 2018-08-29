# This file is generated
from typing import List

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class RecommendationReaction:
    _resources_name = 'recommendation-reactions'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'RecommendationReaction(id={self.user!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model RecommendationReaction are missing')


    @required
    @property
    def user(self) -> str:
        return self._data['user']


    @user.setter
    def user(self, value: str):
        self._data['user'] = value


    @required
    @property
    def lesson(self) -> str:
        return self._data['lesson']


    @lesson.setter
    def lesson(self, value: str):
        self._data['lesson'] = value


    @required
    @property
    def reaction(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('reaction', "None")


    @reaction.setter
    def reaction(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self._data['reaction'] = value


    @required
    @property
    def time(self) -> str:
        """
        Default value: ``"2018-08-26T00:35:32.023Z"``

        Type: str
        """
        return self._data.setdefault('time', "2018-08-26T00:35:32.023Z")


    @time.setter
    def time(self, value: str):
        """
        Default value: ``"2018-08-26T00:35:32.023Z"``

        Type: str
        """
        self._data['time'] = value


