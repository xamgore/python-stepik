from json import JSONDecodeError
from typing import List, Iterable, Optional, TypeVar
from urllib.parse import urlencode

from api.courses import Course
from api.lessons import Lesson
from api.sections import Section
from api.step_sources import StepSource
from api.stepics import Stepics
from api.steps import Step
from api.units import Unit
from api.users import User
from api.videos import Video
from errors import StepikError

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
        api_url = f'https://{self._server}/api/{resource_name}/{id}'
        response = requests.put(api_url, headers=self.headers, json={resource_name: data}).json()
        if resource_name not in response:
            raise StepikError(response['detail'])
        return response[f'{resource_name}'][0]


    def _get(self, url):
        api_url = f'https://{self._server}/api/{url}'
        res = requests.get(api_url, headers=self.headers)

        try:
            return res.json()
        except JSONDecodeError as e:
            return {'error': f'{res.status_code} {res.reason}'}


    def _post(self, url, data=None):
        api_url = f'https://{self._server}/api/{url}'
        res = requests.post(api_url, headers=self.headers, json=data or {})

        try:
            return res.json()
        except JSONDecodeError as e:
            return {'error': f'{res.status_code} {res.reason}'}


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


    def _fetch_objects(self, model: TypeVar, obj_ids: List[int]):
        resource_name = model._resources_name

        # Fetch objects by 30 items,
        # so we won't bump into HTTP request length limits
        step_size = 30
        for i in range(0, len(obj_ids), step_size):
            ids_slice = obj_ids[i:i + step_size]
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


class Courses(object):
    def __init__(self, stepik: Stepik):
        self.stepik = stepik


    def get(self, course_id: int) -> Course:
        return Course(self.stepik, self.stepik._fetch_object(Course, course_id))


    def update(self, course: Course):
        pass


class Sections(object):
    def __init__(self, stepik: Stepik):
        self.stepik = stepik


    def get(self, id: int) -> Section:
        return Section(self.stepik, self.stepik._fetch_object(Section, id))


class Units(object):
    def __init__(self, stepik: Stepik):
        self.stepik = stepik


    def get(self, id: int) -> Unit:
        return Unit(self.stepik, self.stepik._fetch_object(Unit, id))


    def get_all(self, ids: List[int], keep_order=True) -> Iterable[Unit]:
        iterable = self.stepik._fetch_objects(Unit, ids)
        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(o['id']))
        yield from (Unit(self.stepik, o) for o in iterable)


    def update(self, unit: Unit):
        self.stepik._update('units', unit.id, unit._data)


class Lessons(object):
    def __init__(self, stepik):
        self._stepik = stepik


    def get(self, id: int) -> Lesson:
        return Lesson(self._stepik, self._stepik._fetch_object(Lesson, id))


    def get_all(self, ids: List[int], keep_order=True) -> Iterable[Lesson]:
        objects = self._stepik._fetch_objects(Lesson, ids)
        iterable = (Lesson(self._stepik, o) for o in objects)

        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(getattr(o, 'id')))

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


    def get_all(self, ids: List[int], keep_order=True) -> Iterable[Step]:
        iterable = self.stepik._fetch_objects(Step, ids)
        if keep_order:
            iterable = sorted(iterable, key=lambda o: ids.index(o['id']))
        yield from (Step(self.stepik, o) for o in iterable)


    def get(self, id: int) -> Step:
        return Step(self.stepik, self.stepik._fetch_object(Step, id))


class StepSources(object):
    def __init__(self, stepik: Stepik):
        self.stepik = stepik


    def get(self, id: int) -> StepSource:
        return StepSource(self.stepik, self.stepik._fetch_object(StepSource, id))


class Users(object):
    def __init__(self, stepik: Stepik):
        self.stepik = stepik


    def get(self, id: int) -> User:
        return User(self.stepik, self.stepik._fetch_object(User, id))


if __name__ == '__main__':
    pass

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
