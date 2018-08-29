# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class Achievement:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'Achievement(id={self.id!r})'


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @required
    @property
    def kind(self) -> str:
        return self.__data['kind']


    @kind.setter
    def kind(self, value: str):
        self.__data['kind'] = value


    @required
    @property
    def target_score(self) -> int:
        return self.__data['target_score']


    @target_score.setter
    def target_score(self, value: int):
        self.__data['target_score'] = value


    @required
    @property
    def icon_uploadcare_uuid(self) -> str:
        return self.__data['icon_uploadcare_uuid']


    @icon_uploadcare_uuid.setter
    def icon_uploadcare_uuid(self, value: str):
        self.__data['icon_uploadcare_uuid'] = value


    @readonly
    @property
    def icon_urls(self) -> str:
        return self.__data['icon_urls']


