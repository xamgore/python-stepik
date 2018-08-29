# This file is generated
from typing import List

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class ServiceRequest:
    _resources_name = 'service-requests'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'ServiceRequest(id={self.id!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model ServiceRequest are missing')


    @readonly
    @property
    def id(self) -> str:
        return self._data['id']


    @required
    @property
    def target(self) -> str:
        return self._data['target']


    @target.setter
    def target(self, value: str):
        self._data['target'] = value


    @required
    @property
    def method(self) -> str:
        return self._data['method']


    @method.setter
    def method(self, value: str):
        self._data['method'] = value


    @property
    def args(self) -> str:
        """
        Default value: ``[]``
        """
        return self._data['args']


    @args.setter
    def args(self, value: str):
        """
        Default value: ``[]``
        """
        self._data['args'] = value


    @property
    def kwargs(self) -> str:
        """
        Default value: ``{}``
        """
        return self._data['kwargs']


    @kwargs.setter
    def kwargs(self, value: str):
        """
        Default value: ``{}``
        """
        self._data['kwargs'] = value


    @readonly
    @property
    def status(self) -> str:
        return self._data['status']


    @readonly
    @property
    def result(self) -> str:
        return self._data['result']


