from typing import List

from api.courses import Course
from api.groups import Group
from api.lessons import Lesson
from api.sections import Section
from api.step_sources import StepSource
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

    def _update(self, resource_name: str, id: int, data: dict):
        """
        :param resource_name: the name of resource
        :param id: resource's id to grub
        :param data: dict object
        """
        api_url = f'https://{self.__server}/api/{resource_name}/{id}'
        response = requests.put(api_url, headers=self.headers, json={resource_name: data}).json()
        return response[f'{resource_name}'][0]


    def _fetch_object(self, resource_name: str, id: int):
        """
        :param resource_name: the name of resource
        :param id: resource's id to grub
        """
        api_url = f'https://{self.__server}/api/{resource_name}/{id}'
        response = requests.get(api_url, headers=self.headers).json()
        if resource_name not in response:
            raise StepikError(response['detail'])
        return response[f'{resource_name}'][0]


    def fetch_objects(self, resource_name: str, obj_ids: List[int]):
        # Fetch objects by 30 items,
        # so we won't bump into HTTP request length limits
        step_size = 30
        for i in range(0, len(obj_ids), step_size):
            obj_ids_slice = obj_ids[i:i + step_size]
            api_url = 'https://{}/api/{}s?{}' \
                .format(self.__server, resource_name,
                        '&'.join(f'ids[]={obj_id}' for obj_id in obj_ids_slice))
            response = requests.get(api_url, headers=self.headers).json()
            yield from response[f'{resource_name}s']


class Courses(object):
    def __init__(self, stepik: Stepik):
        self.stepik = stepik


    def get(self, course_id: int) -> Course:
        return Course(self.stepik, self.stepik._fetch_object('courses', course_id))


    def update(self, course: Course):
        pass


class Sections(object):
    def __init__(self, stepik: Stepik):
        self.stepik = stepik


    def get(self, id: int) -> Section:
        return Section(self.stepik, self.stepik._fetch_object('sections', id))


class Units(object):
    def __init__(self, stepik: Stepik):
        self.stepik = stepik


    def get(self, id: int) -> Unit:
        return Unit(self.stepik, self.stepik._fetch_object('units', id))


    def update(self, unit: Unit):
        self.stepik._update('units', unit.id, unit._Unit__data)


class Lessons(object):
    def __init__(self, stepik: Stepik):
        self.stepik = stepik


    def get(self, id: int) -> Lesson:
        return Lesson(self.stepik, self.stepik._fetch_object('lessons', id))


class StepSources(object):
    def __init__(self, stepik: Stepik):
        self.stepik = stepik


    def get(self, id: int) -> StepSource:
        return StepSource(self.stepik, self.stepik._fetch_object('step-sources', id))



if __name__ == '__main__':
    print('ok')
