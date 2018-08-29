# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class CourseProgressChange:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'CourseProgressChange(id={self.id!r})'


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @required
    @property
    def user(self) -> str:
        return self.__data['user']


    @user.setter
    def user(self, value: str):
        self.__data['user'] = value


    @required
    @property
    def course(self) -> str:
        return self.__data['course']


    @course.setter
    def course(self, value: str):
        self.__data['course'] = value


    @required
    @property
    def time(self) -> str:
        """
        Default value: ``"2018-08-26T00:35:10.871Z"``

        Type: str
        """
        return self.__data.setdefault('time', "2018-08-26T00:35:10.871Z")


    @time.setter
    def time(self, value: str):
        """
        Default value: ``"2018-08-26T00:35:10.871Z"``

        Type: str
        """
        self.__data['time'] = value


    @required
    @property
    def score(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('score', "None")


    @score.setter
    def score(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self.__data['score'] = value


    @required
    @property
    def cost(self) -> int:
        return self.__data['cost']


    @cost.setter
    def cost(self, value: int):
        self.__data['cost'] = value


    @required
    @property
    def n_steps(self) -> int:
        return self.__data['n_steps']


    @n_steps.setter
    def n_steps(self, value: int):
        self.__data['n_steps'] = value


    @required
    @property
    def n_steps_passed(self) -> int:
        return self.__data['n_steps_passed']


    @n_steps_passed.setter
    def n_steps_passed(self, value: int):
        self.__data['n_steps_passed'] = value


    @required
    @property
    def best_score(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('best_score', "None")


    @best_score.setter
    def best_score(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self.__data['best_score'] = value


    @property
    def rank(self) -> int:
        return self.__data['rank']


    @rank.setter
    def rank(self, value: int):
        self.__data['rank'] = value


    @property
    def rank_max(self) -> int:
        return self.__data['rank_max']


    @rank_max.setter
    def rank_max(self, value: int):
        self.__data['rank_max'] = value


    @property
    def rank_position(self) -> int:
        return self.__data['rank_position']


    @rank_position.setter
    def rank_position(self, value: int):
        self.__data['rank_position'] = value


    @property
    def users_count(self) -> int:
        return self.__data['users_count']


    @users_count.setter
    def users_count(self, value: int):
        self.__data['users_count'] = value


    @property
    def is_teacher(self) -> bool:
        """
        Default value: ``False``
        """
        return self.__data['is_teacher']


    @is_teacher.setter
    def is_teacher(self, value: bool):
        """
        Default value: ``False``
        """
        self.__data['is_teacher'] = value


    @property
    def date_joined(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('date_joined', "None")


    @date_joined.setter
    def date_joined(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self.__data['date_joined'] = value


    @property
    def last_viewed(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('last_viewed', "None")


    @last_viewed.setter
    def last_viewed(self, value: str):
        """
        Default value: ``"None"``

        Type: str
        """
        self.__data['last_viewed'] = value


