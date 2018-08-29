# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class BlockEdit:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'BlockEdit(id={self.id!r})'


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
    def options(self) -> str:
        """
        Enter a valid JSON object

        Default value: ``{}``
        """
        return self.__data['options']


    @readonly
    @property
    def subtitle_files(self) -> str:
        return self.__data['subtitle_files']


    @property
    def source(self) -> str:
        """
        Enter a valid JSON object

        Default value: ``{}``
        """
        return self.__data['source']


    @source.setter
    def source(self, value: str):
        """
        Enter a valid JSON object

        Default value: ``{}``
        """
        self.__data['source'] = value


    @property
    def subtitles(self) -> str:
        """
        Enter a valid JSON object

        Default value: ``{}``
        """
        return self.__data['subtitles']


    @subtitles.setter
    def subtitles(self, value: str):
        """
        Enter a valid JSON object

        Default value: ``{}``
        """
        self.__data['subtitles'] = value


    @readonly
    @property
    def tests_archive(self) -> str:
        return self.__data['tests_archive']


    @property
    def feedback_correct(self) -> str:
        return self.__data['feedback_correct']


    @feedback_correct.setter
    def feedback_correct(self, value: str):
        self.__data['feedback_correct'] = value


    @property
    def feedback_wrong(self) -> str:
        return self.__data['feedback_wrong']


    @feedback_wrong.setter
    def feedback_wrong(self, value: str):
        self.__data['feedback_wrong'] = value




class StepSource:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'StepSource(id={self.id!r})'


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
        Default value: ``1``
        """
        return self.__data.setdefault('position', 1)


    @position.setter
    def position(self, value: int):
        """
        Default value: ``1``
        """
        self.__data['position'] = value


    @readonly
    @property
    def status(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('status', "None")


    @required
    @property
    def block(self) -> str:
        """
        Type: str
        """
        return self.__data['block']


    @block.setter
    def block(self, value: str):
        """
        Type: str
        """
        self.__data['block'] = value


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
        Default value: ``False``
        """
        return self.__data['is_solutions_unlocked']


    @is_solutions_unlocked.setter
    def is_solutions_unlocked(self, value: bool):
        """
        Default value: ``False``
        """
        self.__data['is_solutions_unlocked'] = value


    @required
    @property
    def solutions_unlocked_attempts(self) -> int:
        """
        Default value: ``3``
        """
        return self.__data.setdefault('solutions_unlocked_attempts', 3)


    @solutions_unlocked_attempts.setter
    def solutions_unlocked_attempts(self, value: int):
        """
        Default value: ``3``
        """
        self.__data['solutions_unlocked_attempts'] = value


    @property
    def has_submissions_restrictions(self) -> bool:
        """
        Default value: ``False``
        """
        return self.__data['has_submissions_restrictions']


    @has_submissions_restrictions.setter
    def has_submissions_restrictions(self, value: bool):
        """
        Default value: ``False``
        """
        self.__data['has_submissions_restrictions'] = value


    @required
    @property
    def max_submissions_count(self) -> int:
        """
        Default value: ``3``
        """
        return self.__data.setdefault('max_submissions_count', 3)


    @max_submissions_count.setter
    def max_submissions_count(self, value: int):
        """
        Default value: ``3``
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
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('create_date', "None")


    @readonly
    @property
    def update_date(self) -> str:
        """
        Default value: ``"None"``

        Type: str
        """
        return self.__data.setdefault('update_date', "None")


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


    @readonly
    @property
    def reason_of_failure(self) -> str:
        return self.__data['reason_of_failure']


    @readonly
    @property
    def error(self) -> str:
        """
        Enter a valid JSON object

        Default value: ``{'text': '', 'code': '', 'params': {}}``
        """
        return self.__data.setdefault('error', {'text': '', 'code': '', 'params': {}})


    @required
    @readonly
    @property
    def warnings(self) -> str:
        """
        Enter a valid JSON object

        Default value: ``[]``
        """
        return self.__data['warnings']


    @required
    @property
    def cost(self) -> int:
        """
        Default value: ``0``
        """
        return self.__data['cost']


    @cost.setter
    def cost(self, value: int):
        """
        Default value: ``0``
        """
        self.__data['cost'] = value

