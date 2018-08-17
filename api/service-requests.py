# This file is generated
from common import required, readonly
from typing import List



class WriteServiceRequest:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'WriteServiceRequest(id={self.id!r})'


    @required
    @property
    def target(self) -> str:
        return self.__data['target']


    @target.setter
    def target(self, value: str):
        self.__data['target'] = value


    @required
    @property
    def method(self) -> str:
        return self.__data['method']


    @method.setter
    def method(self, value: str):
        self.__data['method'] = value


    @property
    def args(self) -> str:
        """
        Default value: []
        """
        return self.__data['args']


    @args.setter
    def args(self, value: str):
        """
        Default value: []
        """
        self.__data['args'] = value


    @property
    def kwargs(self) -> str:
        """
        Default value: {}
        """
        return self.__data['kwargs']


    @kwargs.setter
    def kwargs(self, value: str):
        """
        Default value: {}
        """
        self.__data['kwargs'] = value




class ServiceRequest:
    def __init__(self, stepik, data):
        self.__stepik = stepik
        self.__data = data


    def __repr__(self):
        return f'ServiceRequest(id={self.id!r})'


    @readonly
    @property
    def id(self) -> str:
        return self.__data['id']


    @required
    @property
    def target(self) -> str:
        return self.__data['target']


    @target.setter
    def target(self, value: str):
        self.__data['target'] = value


    @required
    @property
    def method(self) -> str:
        return self.__data['method']


    @method.setter
    def method(self, value: str):
        self.__data['method'] = value


    @property
    def args(self) -> str:
        """
        Default value: []
        """
        return self.__data['args']


    @args.setter
    def args(self, value: str):
        """
        Default value: []
        """
        self.__data['args'] = value


    @property
    def kwargs(self) -> str:
        """
        Default value: {}
        """
        return self.__data['kwargs']


    @kwargs.setter
    def kwargs(self, value: str):
        """
        Default value: {}
        """
        self.__data['kwargs'] = value


    @readonly
    @property
    def status(self) -> str:
        return self.__data['status']


    @readonly
    @property
    def result(self) -> str:
        return self.__data['result']


