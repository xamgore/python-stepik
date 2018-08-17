# This file is generated
from common import required, readonly
from typing import List



class WriteStep:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'WriteStep(id={self.id!r})'


    @required
    @property
    def position(self) -> int:
        """
        Default value: 1
        """
        return self.__data.setdefault('position', 1)


    @position.setter
    def position(self, value: int):
        """
        Default value: 1
        """
        self.__data['position'] = value


    @property
    def is_solutions_unlocked(self) -> bool:
        """
        Default value: False
        """
        return self.__data['is_solutions_unlocked']


    @is_solutions_unlocked.setter
    def is_solutions_unlocked(self, value: bool):
        """
        Default value: False
        """
        self.__data['is_solutions_unlocked'] = value


    @required
    @property
    def solutions_unlocked_attempts(self) -> int:
        """
        Default value: 3
        """
        return self.__data.setdefault('solutions_unlocked_attempts', 3)


    @solutions_unlocked_attempts.setter
    def solutions_unlocked_attempts(self, value: int):
        """
        Default value: 3
        """
        self.__data['solutions_unlocked_attempts'] = value


    @property
    def has_submissions_restrictions(self) -> bool:
        """
        Default value: False
        """
        return self.__data['has_submissions_restrictions']


    @has_submissions_restrictions.setter
    def has_submissions_restrictions(self, value: bool):
        """
        Default value: False
        """
        self.__data['has_submissions_restrictions'] = value


    @required
    @property
    def max_submissions_count(self) -> int:
        """
        Default value: 3
        """
        return self.__data.setdefault('max_submissions_count', 3)


    @max_submissions_count.setter
    def max_submissions_count(self, value: int):
        """
        Default value: 3
        """
        self.__data['max_submissions_count'] = value




class Step:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'Step(id={self.id!r})'


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @required
    @readonly
    @property
    def lesson(self) -> str:
        return self.__data['lesson']


    @required
    @property
    def position(self) -> int:
        """
        Default value: 1
        """
        return self.__data.setdefault('position', 1)


    @position.setter
    def position(self, value: int):
        """
        Default value: 1
        """
        self.__data['position'] = value


    @readonly
    @property
    def status(self) -> str:
        """
        Type: choice
        """
        return self.__data['status']


    @readonly
    @property
    def block(self) -> str:
        """
        Type: BlockViewSerializer
        """
        return self.__data['block']


    @readonly
    @property
    def actions(self) -> str:
        return self.__data['actions']


    @readonly
    @property
    def progress(self) -> str:
        return self.__data['progress']


    @readonly
    @property
    def subscriptions(self) -> str:
        return self.__data['subscriptions']


    @required
    @readonly
    @property
    def instruction(self) -> str:
        return self.__data['instruction']


    @readonly
    @property
    def session(self) -> str:
        return self.__data['session']


    @readonly
    @property
    def instruction_type(self) -> str:
        return self.__data['instruction_type']


    @readonly
    @property
    def viewed_by(self) -> str:
        return self.__data['viewed_by']


    @readonly
    @property
    def passed_by(self) -> str:
        return self.__data['passed_by']


    @readonly
    @property
    def correct_ratio(self) -> str:
        return self.__data['correct_ratio']


    @readonly
    @property
    def worth(self) -> str:
        return self.__data['worth']


    @property
    def is_solutions_unlocked(self) -> bool:
        """
        Default value: False
        """
        return self.__data['is_solutions_unlocked']


    @is_solutions_unlocked.setter
    def is_solutions_unlocked(self, value: bool):
        """
        Default value: False
        """
        self.__data['is_solutions_unlocked'] = value


    @required
    @property
    def solutions_unlocked_attempts(self) -> int:
        """
        Default value: 3
        """
        return self.__data.setdefault('solutions_unlocked_attempts', 3)


    @solutions_unlocked_attempts.setter
    def solutions_unlocked_attempts(self, value: int):
        """
        Default value: 3
        """
        self.__data['solutions_unlocked_attempts'] = value


    @property
    def has_submissions_restrictions(self) -> bool:
        """
        Default value: False
        """
        return self.__data['has_submissions_restrictions']


    @has_submissions_restrictions.setter
    def has_submissions_restrictions(self, value: bool):
        """
        Default value: False
        """
        self.__data['has_submissions_restrictions'] = value


    @required
    @property
    def max_submissions_count(self) -> int:
        """
        Default value: 3
        """
        return self.__data.setdefault('max_submissions_count', 3)


    @max_submissions_count.setter
    def max_submissions_count(self, value: int):
        """
        Default value: 3
        """
        self.__data['max_submissions_count'] = value


    @readonly
    @property
    def variation(self) -> str:
        return self.__data['variation']


    @readonly
    @property
    def variations_count(self) -> str:
        return self.__data['variations_count']


    @readonly
    @property
    def create_date(self) -> str:
        """
        Type: datetime
        """
        return self.__data['create_date']


    @readonly
    @property
    def update_date(self) -> str:
        """
        Type: datetime
        """
        return self.__data['update_date']


    @readonly
    @property
    def discussions_count(self) -> str:
        return self.__data['discussions_count']


    @readonly
    @property
    def discussion_proxy(self) -> str:
        return self.__data['discussion_proxy']


    @readonly
    @property
    def discussion_threads(self) -> str:
        return self.__data['discussion_threads']




class WriteBlockView:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'WriteBlockView(id={self.id!r})'


    @required
    @property
    def name(self) -> str:
        return self.__data['name']


    @name.setter
    def name(self, value: str):
        self.__data['name'] = value


    @property
    def text(self) -> str:
        return self.__data['text']


    @text.setter
    def text(self, value: str):
        self.__data['text'] = value


    @property
    def video(self) -> str:
        return self.__data['video']


    @video.setter
    def video(self, value: str):
        self.__data['video'] = value


    @property
    def animation(self) -> str:
        return self.__data['animation']


    @animation.setter
    def animation(self, value: str):
        self.__data['animation'] = value




class BlockView:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'BlockView(id={self.id!r})'


    @required
    @property
    def name(self) -> str:
        return self.__data['name']


    @name.setter
    def name(self, value: str):
        self.__data['name'] = value


    @property
    def text(self) -> str:
        return self.__data['text']


    @text.setter
    def text(self, value: str):
        self.__data['text'] = value


    @property
    def video(self) -> str:
        return self.__data['video']


    @video.setter
    def video(self, value: str):
        self.__data['video'] = value


    @property
    def animation(self) -> str:
        return self.__data['animation']


    @animation.setter
    def animation(self, value: str):
        self.__data['animation'] = value


    @readonly
    @property
    def options(self) -> List:
        """
        Default value: {}
        """
        return self.__data['options']


    @readonly
    @property
    def subtitle_files(self) -> str:
        return self.__data['subtitle_files']


