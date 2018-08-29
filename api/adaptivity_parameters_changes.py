# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class AdaptivityParametersChange:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'AdaptivityParametersChange(id={self.id!r})'


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @property
    def user(self) -> str:
        return self.__data['user']


    @user.setter
    def user(self, value: str):
        self.__data['user'] = value


    @property
    def lesson(self) -> str:
        return self.__data['lesson']


    @lesson.setter
    def lesson(self, value: str):
        self.__data['lesson'] = value


    @property
    def tag(self) -> str:
        return self.__data['tag']


    @tag.setter
    def tag(self, value: str):
        self.__data['tag'] = value


    @required
    @property
    def time(self) -> str:
        """
        Default value: ``"2018-08-26T00:35:00.566Z"``

        Type: str
        """
        return self.__data.setdefault('time', "2018-08-26T00:35:00.566Z")


    @time.setter
    def time(self, value: str):
        """
        Default value: ``"2018-08-26T00:35:00.566Z"``

        Type: str
        """
        self.__data['time'] = value


    @readonly
    @property
    def reason(self) -> str:
        return self.__data['reason']


    @readonly
    @property
    def predicted_score(self) -> str:
        return self.__data['predicted_score']


    @readonly
    @property
    def real_score(self) -> str:
        return self.__data['real_score']


    @readonly
    @property
    def solving_time(self) -> str:
        return self.__data['solving_time']


    @readonly
    @property
    def attempt_num(self) -> str:
        return self.__data['attempt_num']


    @property
    def old_user_skill(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('old_user_skill', "None")


    @old_user_skill.setter
    def old_user_skill(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self.__data['old_user_skill'] = value


    @property
    def old_user_confidence(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('old_user_confidence', "None")


    @old_user_confidence.setter
    def old_user_confidence(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self.__data['old_user_confidence'] = value


    @property
    def old_lesson_difficulty(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('old_lesson_difficulty', "None")


    @old_lesson_difficulty.setter
    def old_lesson_difficulty(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self.__data['old_lesson_difficulty'] = value


    @property
    def old_lesson_confidence(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('old_lesson_confidence', "None")


    @old_lesson_confidence.setter
    def old_lesson_confidence(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self.__data['old_lesson_confidence'] = value


    @property
    def new_user_skill(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('new_user_skill', "None")


    @new_user_skill.setter
    def new_user_skill(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self.__data['new_user_skill'] = value


    @property
    def new_user_confidence(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('new_user_confidence', "None")


    @new_user_confidence.setter
    def new_user_confidence(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self.__data['new_user_confidence'] = value


    @property
    def new_lesson_difficulty(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('new_lesson_difficulty', "None")


    @new_lesson_difficulty.setter
    def new_lesson_difficulty(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self.__data['new_lesson_difficulty'] = value


    @property
    def new_lesson_confidence(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('new_lesson_confidence', "None")


    @new_lesson_confidence.setter
    def new_lesson_confidence(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self.__data['new_lesson_confidence'] = value


