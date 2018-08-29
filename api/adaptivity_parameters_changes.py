# This file is generated
from typing import List

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class AdaptivityParametersChange:
    _resources_name = 'adaptivity-parameters-changes'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'AdaptivityParametersChange(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model AdaptivityParametersChange are missing')


    @readonly
    @property
    def id(self) -> int:
        return self._data['id']


    @property
    def user(self) -> str:
        return self._data['user']


    @user.setter
    def user(self, value: str):
        self._data['user'] = value


    @property
    def lesson(self) -> str:
        return self._data['lesson']


    @lesson.setter
    def lesson(self, value: str):
        self._data['lesson'] = value


    @property
    def tag(self) -> str:
        return self._data['tag']


    @tag.setter
    def tag(self, value: str):
        self._data['tag'] = value


    @required
    @property
    def time(self) -> str:
        """
        Default value: ``"2018-08-26T00:35:00.566Z"``

        Type: str
        """
        return self._data.setdefault('time', "2018-08-26T00:35:00.566Z")


    @time.setter
    def time(self, value: str):
        """
        Default value: ``"2018-08-26T00:35:00.566Z"``

        Type: str
        """
        self._data['time'] = value


    @readonly
    @property
    def reason(self) -> str:
        return self._data['reason']


    @readonly
    @property
    def predicted_score(self) -> str:
        return self._data['predicted_score']


    @readonly
    @property
    def real_score(self) -> str:
        return self._data['real_score']


    @readonly
    @property
    def solving_time(self) -> str:
        return self._data['solving_time']


    @readonly
    @property
    def attempt_num(self) -> str:
        return self._data['attempt_num']


    @property
    def old_user_skill(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('old_user_skill', "None")


    @old_user_skill.setter
    def old_user_skill(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self._data['old_user_skill'] = value


    @property
    def old_user_confidence(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('old_user_confidence', "None")


    @old_user_confidence.setter
    def old_user_confidence(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self._data['old_user_confidence'] = value


    @property
    def old_lesson_difficulty(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('old_lesson_difficulty', "None")


    @old_lesson_difficulty.setter
    def old_lesson_difficulty(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self._data['old_lesson_difficulty'] = value


    @property
    def old_lesson_confidence(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('old_lesson_confidence', "None")


    @old_lesson_confidence.setter
    def old_lesson_confidence(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self._data['old_lesson_confidence'] = value


    @property
    def new_user_skill(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('new_user_skill', "None")


    @new_user_skill.setter
    def new_user_skill(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self._data['new_user_skill'] = value


    @property
    def new_user_confidence(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('new_user_confidence', "None")


    @new_user_confidence.setter
    def new_user_confidence(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self._data['new_user_confidence'] = value


    @property
    def new_lesson_difficulty(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('new_lesson_difficulty', "None")


    @new_lesson_difficulty.setter
    def new_lesson_difficulty(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self._data['new_lesson_difficulty'] = value


    @property
    def new_lesson_confidence(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self._data.setdefault('new_lesson_confidence', "None")


    @new_lesson_confidence.setter
    def new_lesson_confidence(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self._data['new_lesson_confidence'] = value


