# This file is generated
from typing import List, Iterable, Any

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




class ListOfRecommendationReactions:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get_all(self, users: List[str], keep_order=False) -> Iterable[RecommendationReaction]:
        objects = self._stepik._fetch_objects(RecommendationReaction, users)
        iterable = (RecommendationReaction(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'user')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)


    def create(self, user: str, lesson: str, reaction: str, time: str = None) -> RecommendationReaction:
        vars = locals().copy()
        data = {'recommendation-reaction': {k: v for k, v in vars.items() if k != 'self' and v is not None}}

        resources_name = 'recommendation-reactions'
        response = self._stepik._post(resources_name, data)

        if resources_name not in response:
            raise StepikError(response)

        return RecommendationReaction(self._stepik, response[resources_name][0])
