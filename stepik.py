from json import JSONDecodeError
from typing import List, Iterable, TypeVar, Optional
from urllib.parse import urlencode

from api.courses import Course, ListOfCourses
from api.lessons import Lesson, ListOfLessons
from api.sections import Section, ListOfSections
from api.step_sources import StepSource, ListOfStepSources
from api.stepics import Stepics
from api.steps import Step, ListOfSteps
from api.units import Unit, ListOfUnits
from api.users import User, ListOfUsers
from api.videos import Video
from errors import StepikError
from profiles import ListOfProfiles

integer = int
boolean = bool
decimal = float
string, url, choice = str, str, str

import requests


class Stepik:
    def __init__(self, client_id: str, client_secret: str, server: str = 'stepik.org'):
        data = {'grant_type': 'client_credentials'}
        auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
        resp = requests.post(f'https://{server}/oauth2/token/', data, auth=auth)
        token = resp.json().get('access_token', None)

        if not token:
            raise ConnectionRefusedError('Unable to authorize with provided credentials')

        self._server = server
        self.headers = {'Authorization': 'Bearer ' + token}

        self.courses = ListOfCourses(self)
        self.sections = ListOfSections(self)
        self.units = ListOfUnits(self)
        self.lessons = ListOfLessons(self)
        self.step_sources = ListOfStepSources(self)
        self.users = ListOfUsers(self)
        self.steps = ListOfSteps(self)
        self.profiles = ListOfProfiles(self)


    def _update(self, resource_name: str, id: int, data: dict):
        """
        :param resource_name: the name of resource
        :param id: resource's id to grub
        :param data: dict object
        """
        api_url = f'https://{self._server}/api/{resource_name}/{id}'
        response = requests.put(api_url, headers=self.headers, json=data).json()
        if resource_name not in response:
            raise StepikError(response['detail'])
        return response[f'{resource_name}'][0]


    def _get(self, url):
        api_url = f'https://{self._server}/api/{url}'
        res = requests.get(api_url, headers=self.headers)

        try:
            return res.json()
        except JSONDecodeError as e:
            return {'detail': f'{res.status_code} {res.reason}'}


    def _post(self, url, data=None):
        api_url = f'https://{self._server}/api/{url}'
        res = requests.post(api_url, headers=self.headers, json=data or {})

        try:
            return res.json()
        except JSONDecodeError as e:
            return {'detail': f'{res.status_code} {res.reason}'}


    def _put(self, url, data=None):
        api_url = f'https://{self._server}/api/{url}'
        res = requests.put(api_url, headers=self.headers, json=data or {})

        try:
            return res.json()
        except JSONDecodeError as e:
            return {'detail': f'{res.status_code} {res.reason}'}


    def _delete(self, url, id):
        api_url = f'https://{self._server}/api/{url}/{id}'
        res = requests.delete(api_url, headers=self.headers)

        try:
            return res.json()
        except JSONDecodeError as e:
            return {'detail': f'{res.status_code} {res.reason}'}


    def _fetch_object(self, model: TypeVar, id: int):
        """
        :param model: the name of resource
        :param id: resource's id to grub
        """
        resource_name = model._resources_name
        response = self._get(f'{resource_name}/{id}')

        if resource_name not in response:
            raise StepikError(response['detail'])

        return response[resource_name][0]


    @staticmethod
    def __take(n: int, iterable: Iterable):
        # take(2, [1,4,6,4,1]) --> 1 4
        assert n > 0

        i = 0
        for x in iterable:
            yield x
            i += 1
            if i >= n:
                break


    def _fetch_objects(self, model: TypeVar, obj_ids: Iterable[int]):
        resource_name = model._resources_name
        iterator = iter(obj_ids)

        # Fetch objects by 20 items,
        # so we won't bump into HTTP request length limits
        step_size = 20
        while True:
            ids_slice = list(self.__take(step_size, iterator))
            if not ids_slice:
                break

            ids = '&'.join(f'ids[]={id}' for id in ids_slice)
            response = self._get(f'{resource_name}/?{ids}')

            if resource_name not in response:
                raise StepikError(response['detail'])

            yield from response[resource_name]


    def _upload(self, resource_name, files, data):
        return requests.post(f'https://{self._server}/api/{resource_name}',
                             headers=self.headers, files=files, data=data)


    def upload_video(self, file_path: str = None, file_url: str = None,
                     lesson_id: int = None, course_id: int = None):
        if lesson_id is None and course_id is None:
            raise AttributeError('lesson_id or course_id must be filled')

        data = {'lesson': lesson_id} if course_id is None else {'course': course_id}

        if file_path is not None:
            with open(file_path, 'rb') as f:
                res = self._upload('videos', {'source': f}, data).json()
        elif file_url is not None:
            data['source_url'] = file_url
            res = self._post('videos', {'video': data}).json()
        else:
            raise AttributeError('file_path or file_url must be filled')

        return Video(self, res)


    def stepics(self) -> Stepics:
        """
        The current context: user's id, system's state.
        """
        return Stepics(self, self._fetch_object(Stepics, 1))


if __name__ == '__main__':
    pass

    from config import id, secret
    stepik = Stepik(id, secret)

    lesson = stepik.lessons.create(title='This is my test lesson', is_public=False)
    print(lesson.title, lesson.id)

    lesson.title = 'Ok, second test'
    lesson = stepik.lessons.update(lesson)
    print(lesson.title, lesson.id)

    stepik.lessons.delete(lesson.id)



    # sections = course.sections.list()
    #
    # unit_ids = [id for sec in sections for id in sec.units_ids]
    # units = stepik.units.get_all(unit_ids)
    #
    # lesson_ids = [u.lesson_id for u in units]
    # lessons = stepik.lessons.get_all(lesson_ids)
    #
    # step_ids = [id for les in lessons for id in les.steps_ids]
    # steps = stepik.steps.get_all(step_ids)
