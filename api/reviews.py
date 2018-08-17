# This file is generated
from common import required, readonly
from typing import List



class WriteReview:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'WriteReview(id={self.id!r})'


    @required
    @property
    def session(self) -> str:
        return self.__data['session']


    @session.setter
    def session(self, value: str):
        self.__data['session'] = value


    @property
    def target_session(self) -> str:
        return self.__data['target_session']


    @target_session.setter
    def target_session(self, value: str):
        self.__data['target_session'] = value


    @property
    def text(self) -> str:
        return self.__data['text']


    @text.setter
    def text(self, value: str):
        self.__data['text'] = value


    @required
    @property
    def rubric_scores(self) -> str:
        return self.__data['rubric_scores']


    @rubric_scores.setter
    def rubric_scores(self, value: str):
        self.__data['rubric_scores'] = value




class Review:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'Review(id={self.id!r})'


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @required
    @property
    def session(self) -> str:
        return self.__data['session']


    @session.setter
    def session(self, value: str):
        self.__data['session'] = value


    @property
    def target_session(self) -> str:
        return self.__data['target_session']


    @target_session.setter
    def target_session(self, value: str):
        self.__data['target_session'] = value


    @property
    def text(self) -> str:
        return self.__data['text']


    @text.setter
    def text(self, value: str):
        self.__data['text'] = value


    @required
    @property
    def rubric_scores(self) -> str:
        return self.__data['rubric_scores']


    @rubric_scores.setter
    def rubric_scores(self, value: str):
        self.__data['rubric_scores'] = value


    @readonly
    @property
    def submission(self) -> int:
        return self.__data['submission']


    @readonly
    @property
    def when_finished(self) -> str:
        """
        Type: datetime
        """
        return self.__data['when_finished']


    @readonly
    @property
    def is_verified(self) -> bool:
        """
        Default value: False
        """
        return self.__data['is_verified']


