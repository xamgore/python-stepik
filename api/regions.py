# This file is generated
from common import required, readonly
from typing import List
from resources_list import ResourcesList



class WriteRegion:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'WriteRegion(id={self.id!r})'


    @required
    @property
    def name_std(self) -> str:
        return self.__data['name_std']


    @name_std.setter
    def name_std(self, value: str):
        self.__data['name_std'] = value


    @required
    @property
    def alt_names(self) -> str:
        """
        Type: array
        """
        return self.__data['alt_names']


    @alt_names.setter
    def alt_names(self, value: str):
        """
        Type: array
        """
        self.__data['alt_names'] = value




class Region:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'Region(id={self.id!r})'


    @readonly
    @property
    def id(self) -> int:
        return self.__data['id']


    @required
    @property
    def name_std(self) -> str:
        return self.__data['name_std']


    @name_std.setter
    def name_std(self, value: str):
        self.__data['name_std'] = value


    @required
    @property
    def alt_names(self) -> str:
        """
        Type: array
        """
        return self.__data['alt_names']


    @alt_names.setter
    def alt_names(self, value: str):
        """
        Type: array
        """
        self.__data['alt_names'] = value




class WriteAlternativeName:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'WriteAlternativeName(id={self.id!r})'


    @required
    @property
    def name(self) -> str:
        return self.__data['name']


    @name.setter
    def name(self, value: str):
        self.__data['name'] = value


    @required
    @property
    def language(self) -> str:
        return self.__data['language']


    @language.setter
    def language(self, value: str):
        self.__data['language'] = value


    @property
    def is_preferred(self) -> bool:
        """
        Default value: ``False``
        """
        return self.__data['is_preferred']


    @is_preferred.setter
    def is_preferred(self, value: bool):
        """
        Default value: ``False``
        """
        self.__data['is_preferred'] = value




class AlternativeName:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'AlternativeName(id={self.id!r})'


    @required
    @property
    def name(self) -> str:
        return self.__data['name']


    @name.setter
    def name(self, value: str):
        self.__data['name'] = value


    @required
    @property
    def language(self) -> str:
        return self.__data['language']


    @language.setter
    def language(self, value: str):
        self.__data['language'] = value


    @property
    def is_preferred(self) -> bool:
        """
        Default value: ``False``
        """
        return self.__data['is_preferred']


    @is_preferred.setter
    def is_preferred(self, value: bool):
        """
        Default value: ``False``
        """
        self.__data['is_preferred'] = value


