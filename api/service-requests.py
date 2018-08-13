# This file is generated
from common import required, readonly
from typing import List


class WriteServiceRequest:
    def __init__(self, data):
        self.__data = data


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
        default value: []
        """
        return self.__data['args']


    @args.setter
    def args(self, value: str):
        """
        default value: []
        """
        self.__data['args'] = value


    @property
    def kwargs(self) -> str:
        """
        default value: {}
        """
        return self.__data['kwargs']


    @kwargs.setter
    def kwargs(self, value: str):
        """
        default value: {}
        """
        self.__data['kwargs'] = value


class ServiceRequest:
    def __init__(self, data):
        self.__data = data


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
        default value: []
        """
        return self.__data['args']


    @args.setter
    def args(self, value: str):
        """
        default value: []
        """
        self.__data['args'] = value


    @property
    def kwargs(self) -> str:
        """
        default value: {}
        """
        return self.__data['kwargs']


    @kwargs.setter
    def kwargs(self, value: str):
        """
        default value: {}
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


