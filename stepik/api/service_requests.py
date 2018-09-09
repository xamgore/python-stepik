# This file is generated
from typing import List, Iterable, Any, Optional

from stepik.errors import StepikError
from stepik.common import required, readonly
from stepik.resources_list import ResourcesList


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




class ListOfServiceRequests:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def get(self, id: str) -> ServiceRequest:
        obj = self._stepik._fetch_object(ServiceRequest, id)
        return ServiceRequest(self._stepik, obj)


    def create(self,
               target: str,
               method: str,
               args: str = None,
               kwargs: str = None,
               **kwargs) -> ServiceRequest:
        vars = locals().copy()
        data = {'service-request':
                    {k: v for k, v in {**vars, **kwargs}.items()
                     if k != 'self' and v is not None}}

        response = self._stepik._post('service-requests', data)
        if 'service-requests' not in response:
            raise StepikError(response)

        return ServiceRequest(self._stepik, response['service-requests'][0])

