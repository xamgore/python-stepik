# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class AchievementProgress:
    _resources_name = 'achievement-progresses'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'AchievementProgress(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model AchievementProgress are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @required
    @property
    def user(self) -> str:
        return self._data['user']


    @user.setter
    def user(self, value: str):
        self._data['user'] = value


    @required
    @property
    def achievement(self) -> str:
        return self._data['achievement']


    @achievement.setter
    def achievement(self, value: str):
        self._data['achievement'] = value


    @required
    @property
    def score(self) -> int:
        return self._data['score']


    @score.setter
    def score(self, value: int):
        self._data['score'] = value


    @readonly
    @property
    def kind(self) -> str:
        return self._data['kind']


    @readonly
    @property
    def create_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('create_date', "None")


    @readonly
    @property
    def update_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('update_date', "None")


    @property
    def obtain_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('obtain_date', "None")


    @obtain_date.setter
    def obtain_date(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self._data['obtain_date'] = value




class ListOfAchievementProgresses:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: int) -> AchievementProgress:
        return AchievementProgress(self._stepik, self._stepik._fetch_object(AchievementProgress, id))


    def get_all(self, ids: List[int], keep_order=False) -> Iterable[AchievementProgress]:
        objects = self._stepik._fetch_objects(AchievementProgress, ids)
        iterable = (AchievementProgress(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))  # or []?

        return iterable


    def __iter__(self):
        yield from self.iterate(limit=None)
