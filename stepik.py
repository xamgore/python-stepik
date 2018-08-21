from typing import List, Iterable

from api.courses import Course
from api.lessons import Lesson
from api.sections import Section
from api.step_sources import StepSource
from api.stepics import Environment
from api.steps import Step
from api.units import Unit
from api.users import User

integer = int
boolean = bool
decimal = float
string, url, choice = str, str, str

import requests


class StepikError(RuntimeError):
    pass


class Stepik:
    def __init__(self, client_id, client_secret, server='stepik.org'):
        data = {'grant_type': 'client_credentials'}
        auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
        resp = requests.post(f'https://{server}/oauth2/token/', data, auth=auth)
        token = resp.json().get('access_token', None)

        if not token:
            raise ConnectionRefusedError('Unable to authorize with provided credentials')

        self.__server = server
        self.headers = {'Authorization': 'Bearer ' + token}

        self.courses = Courses(self)
        self.sections = Sections(self)
        self.units = Units(self)
        self.lessons = Lessons(self)
        self.step_sources = StepSources(self)
        self.users = Users(self)
        self.steps = Steps(self)


    def _update(self, resource_name: str, id: int, data: dict):
        """
        :param resource_name: the name of resource
        :param id: resource's id to grub
        :param data: dict object
        """
        api_url = f'https://{self.__server}/api/{resource_name}/{id}'
        response = requests.put(api_url, headers=self.headers, json={resource_name: data}).json()
        if resource_name not in response:
            raise StepikError(response['detail'])
        return response[f'{resource_name}'][0]


    def fetch_object(self, resource_name: str, id: int):
        """
        :param resource_name: the name of resource
        :param id: resource's id to grub
        """
        from common import to_dash_case
        resource_name = to_dash_case(resource_name)

        api_url = f'https://{self.__server}/api/{resource_name}s/{id}'
        response = requests.get(api_url, headers=self.headers).json()
        if f'{resource_name}s' not in response:
            raise StepikError(response['detail'])
        return response[f'{resource_name}s'][0]


    def fetch_objects(self, resource_name: str, obj_ids: List[int]):
        # Fetch objects by 30 items,
        # so we won't bump into HTTP request length limits
        step_size = 30
        for i in range(0, len(obj_ids), step_size):
            ids_slice = obj_ids[i:i + step_size]
            api_url = 'https://{}/api/{}s?{}' \
                .format(self.__server, resource_name,
                        '&'.join(f'ids[]={id}' for id in ids_slice))
            response = requests.get(api_url, headers=self.headers).json()
            yield from response[f'{resource_name}s']


    def stepics(self) -> Environment:
        """
        Return the current context: user's id, system's state.
        """
        return Environment(self, self.fetch_object('stepic', 1))


class Courses(object):
    def __init__(self, stepik: Stepik):
        self.stepik = stepik


    def get(self, course_id: int) -> Course:
        return Course(self.stepik, self.stepik.fetch_object('course', course_id))


    def update(self, course: Course):
        pass


class Sections(object):
    def __init__(self, stepik: Stepik):
        self.stepik = stepik


    def get(self, id: int) -> Section:
        return Section(self.stepik, self.stepik.fetch_object('section', id))


class Units(object):
    def __init__(self, stepik: Stepik):
        self.stepik = stepik


    def get(self, id: int) -> Unit:
        return Unit(self.stepik, self.stepik.fetch_object('unit', id))


    def fetch_all(self, ids: List[int], keep_order=True) -> Iterable[Unit]:
        iterable = self.stepik.fetch_objects('unit', ids)
        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(o['id']))
        yield from (Unit(self.stepik, o) for o in iterable)


    def update(self, unit: Unit):
        self.stepik._update('units', unit.id, unit._Unit__data)


class Lessons(object):
    def __init__(self, stepik: Stepik):
        self.stepik = stepik


    def fetch_all(self, ids: List[int], keep_order=True) -> Iterable[Lesson]:
        iterable = self.stepik.fetch_objects('lesson', ids)
        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(o['id']))
        yield from (Lesson(self.stepik, o) for o in iterable)


    def get(self, id: int) -> Lesson:
        return Lesson(self.stepik, self.stepik.fetch_object('lesson', id))



class Steps(object):
    def __init__(self, stepik: Stepik):
        self.stepik = stepik


    def fetch_all(self, ids: List[int], keep_order=True) -> Iterable[Step]:
        iterable = self.stepik.fetch_objects('step', ids)
        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(o['id']))
        yield from (Step(self.stepik, o) for o in iterable)


    def get(self, id: int) -> Step:
        return Step(self.stepik, self.stepik.fetch_object('step', id))


class StepSources(object):
    def __init__(self, stepik: Stepik):
        self.stepik = stepik


    def get(self, id: int) -> StepSource:
        return StepSource(self.stepik, self.stepik.fetch_object('step-source', id))


class Users(object):
    def __init__(self, stepik: Stepik):
        self.stepik = stepik


    def get(self, id: int) -> User:
        return User(self.stepik, self.stepik.fetch_object('user', id))


if __name__ == '__main__':
    print('ok')
