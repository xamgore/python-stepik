from typing import List, Iterable, Optional
from urllib.parse import urlencode

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
    def __init__(self, client_id: str, client_secret: str, server: str = 'stepik.org'):
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


    def _get(self, url):
        api_url = f'https://{self.__server}/api/{url}'
        return requests.get(api_url, headers=self.headers).json()


    def _fetch_object(self, resource_name: str, id: int):
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


    def _fetch_objects(self, resource_name: str, obj_ids: List[int]):
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
        The current context: user's id, system's state.
        """
        return Environment(self, self._fetch_object('stepic', 1))


class Courses(object):
    def __init__(self, stepik: Stepik):
        self.stepik = stepik


    def get(self, course_id: int) -> Course:
        return Course(self.stepik, self.stepik._fetch_object('course', course_id))


    def update(self, course: Course):
        pass


class Sections(object):
    def __init__(self, stepik: Stepik):
        self.stepik = stepik


    def get(self, id: int) -> Section:
        return Section(self.stepik, self.stepik._fetch_object('section', id))


class Units(object):
    def __init__(self, stepik: Stepik):
        self.stepik = stepik


    def get(self, id: int) -> Unit:
        return Unit(self.stepik, self.stepik._fetch_object('unit', id))


    def fetch_all(self, ids: List[int], keep_order=True) -> Iterable[Unit]:
        iterable = self.stepik._fetch_objects('unit', ids)
        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(o['id']))
        yield from (Unit(self.stepik, o) for o in iterable)


    def update(self, unit: Unit):
        self.stepik._update('units', unit.id, unit._Unit__data)


class Lessons(object):
    def __init__(self, stepik: Stepik):
        self._stepik = stepik


    def get(self, id: int) -> Lesson:
        return Lesson(self._stepik, self._stepik._fetch_object('lesson', id))


    def get_all(self, ids: List[int], keep_order=True) -> Iterable[Lesson]:
        objects = self._stepik._fetch_objects('lesson', ids)
        iterable = (Lesson(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(o['id']))

        yield from iterable


    def iterate(self, course: Optional[int] = None, owner: Optional[int] = None,
                language: Optional[str] = None, is_featured: Optional[bool] = None,
                by_id: Optional[bool] = None, by_create_date: Optional[bool] = None,
                by_update_date: Optional[bool] = None, by_vote_delta: Optional[bool] = None,
                by_vote_epic: Optional[bool] = None, by_vote_abuse: Optional[bool] = None,
                skip: Optional[int] = 0, limit: Optional[int] = 20) -> Iterable[Lesson]:

        assert skip >= 0, 'skip must be positive'
        assert limit is None or limit >= 0, 'limit must be positive'

        vars = locals().copy()
        args, order = [], []

        for k, v in vars.items():
            is_ordering = k.startswith('by_')
            is_special = k in ['self', 'skip']

            if not v is None and not is_ordering and not is_special:
                args.append((k, v))

            if not v is None and is_ordering:
                sign = '-' if v else ''
                order.append(sign + k[3:])


        params = urlencode(args, doseq=True)
        ordering = ','.join(order)

        skip = 0 if skip is None else skip
        page_idx, count = divmod(skip, 20)
        page_idx += 1  # stepik counts from 1

        while True:
            page = self._stepik._get(f'lessons?{params}&page={page_idx}&order={ordering}')

            for lesson in page['lessons']:
                if limit and count >= limit:
                    break

                yield Lesson(self._stepik, lesson)
                count += 1

            if not page['meta']['has_next']:
                break

            page_idx += 1


    def __iter__(self):
        yield from self.iterate(limit=None)


class Steps(object):
    def __init__(self, stepik: Stepik):
        self.stepik = stepik


    def fetch_all(self, ids: List[int], keep_order=True) -> Iterable[Step]:
        iterable = self.stepik._fetch_objects('step', ids)
        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(o['id']))
        yield from (Step(self.stepik, o) for o in iterable)


    def get(self, id: int) -> Step:
        return Step(self.stepik, self.stepik._fetch_object('step', id))


class StepSources(object):
    def __init__(self, stepik: Stepik):
        self.stepik = stepik


    def get(self, id: int) -> StepSource:
        return StepSource(self.stepik, self.stepik._fetch_object('step-source', id))


class Users(object):
    def __init__(self, stepik: Stepik):
        self.stepik = stepik


    def get(self, id: int) -> User:
        return User(self.stepik, self.stepik._fetch_object('user', id))


if __name__ == '__main__':
    pass
