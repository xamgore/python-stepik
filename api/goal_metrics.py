# This file is generated
from typing import List, Iterable, Any

from errors import StepikError
from common import required, readonly
from resources_list import ResourcesList


class GoalMetric:
    _resources_name = 'goal-metrics'


    def __init__(self, stepik, data):
        from stepik import Stepik
        self._stepik: Stepik = stepik
        self._data = data
        self._check_fields(data)


    def __repr__(self):
        return f'GoalMetric(id={self.goal_name!r})'


    def _check_fields(self, obj):
        # Ensure, all required fields are in the data-object
        if not all(f in obj.keys() for f in self._data):
            raise StepikError('Some fields required by the model GoalMetric are missing')


    @required
    @property
    def goal_name(self) -> str:
        return self._data['goal_name']


    @goal_name.setter
    def goal_name(self, value: str):
        self._data['goal_name'] = value


    @required
    @property
    def value(self) -> str:
        """
        Default value: ``"0"``

        Type: str
        """
        return self._data.setdefault('value', "0")


    @value.setter
    def value(self, value: str):
        """
        Default value: ``"0"``

        Type: str
        """
        self._data['value'] = value




class ListOfGoalMetrics:
    def __init__(self, stepik):
        from stepik import Stepik
        self._stepik: Stepik = stepik


    def create(self, goal_name: str, value: str = None) -> GoalMetric:
        vars = locals().copy()
        data = {'goal-metric': {k: v for k, v in vars.items() if k != 'self' and v is not None}}

        resources_name = 'goal-metrics'
        response = self._stepik._post(resources_name, data)

        if resources_name not in response:
            raise StepikError(response)

        return GoalMetric(self._stepik, response[resources_name][0])
