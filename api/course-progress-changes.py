# This file is generated
from common import required, readonly
from typing import List



class WriteCourseProgressChange:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'WriteCourseProgressChange(id={self.id!r})'


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
        Default value: "2018-08-10T09:47:31.030Z"
        """
        return self.__data.setdefault('time', "2018-08-10T09:47:31.030Z")


    @time.setter
    def time(self, value: str):
        """
        Default value: "2018-08-10T09:47:31.030Z"
        """
        self.__data['time'] = value


    @required
    @property
    def score(self) -> str:
        """
        Type: float
        """
        return self.__data['score']


    @score.setter
    def score(self, value: str):
        """
        Type: float
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
        Type: float
        """
        return self.__data['best_score']


    @best_score.setter
    def best_score(self, value: str):
        """
        Type: float
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
        Default value: False
        """
        return self.__data['is_teacher']


    @is_teacher.setter
    def is_teacher(self, value: bool):
        """
        Default value: False
        """
        self.__data['is_teacher'] = value


    @property
    def date_joined(self) -> str:
        """
        Type: datetime
        """
        return self.__data['date_joined']


    @date_joined.setter
    def date_joined(self, value: str):
        """
        Type: datetime
        """
        self.__data['date_joined'] = value


    @property
    def last_viewed(self) -> str:
        """
        Type: datetime
        """
        return self.__data['last_viewed']


    @last_viewed.setter
    def last_viewed(self, value: str):
        """
        Type: datetime
        """
        self.__data['last_viewed'] = value




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
        Default value: "2018-08-10T09:47:31.030Z"
        """
        return self.__data.setdefault('time', "2018-08-10T09:47:31.030Z")


    @time.setter
    def time(self, value: str):
        """
        Default value: "2018-08-10T09:47:31.030Z"
        """
        self.__data['time'] = value


    @required
    @property
    def score(self) -> str:
        """
        Type: float
        """
        return self.__data['score']


    @score.setter
    def score(self, value: str):
        """
        Type: float
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
        Type: float
        """
        return self.__data['best_score']


    @best_score.setter
    def best_score(self, value: str):
        """
        Type: float
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
        Default value: False
        """
        return self.__data['is_teacher']


    @is_teacher.setter
    def is_teacher(self, value: bool):
        """
        Default value: False
        """
        self.__data['is_teacher'] = value


    @property
    def date_joined(self) -> str:
        """
        Type: datetime
        """
        return self.__data['date_joined']


    @date_joined.setter
    def date_joined(self, value: str):
        """
        Type: datetime
        """
        self.__data['date_joined'] = value


    @property
    def last_viewed(self) -> str:
        """
        Type: datetime
        """
        return self.__data['last_viewed']


    @last_viewed.setter
    def last_viewed(self, value: str):
        """
        Type: datetime
        """
        self.__data['last_viewed'] = value


