# Run with Python 3
# Saves all step sources into foldered structure
import datetime
import json
import os
from typing import List

from api.courses import Course
from api.lessons import Lesson
from api.sections import Section
from api.units import Unit

integer = int
boolean = bool
decimal = float
string, url, choice = str, str, str

import requests

from config import id, secret


class Stepik:
    def __init__(self, client_id, client_secret):
        token = requests \
            .post('https://stepik.org/oauth2/token/',
                  data={'grant_type': 'client_credentials'},
                  auth=requests.auth.HTTPBasicAuth(client_id, client_secret)) \
            .json() \
            .get('access_token', None)

        if not token:
            raise ConnectionRefusedError('Unable to authorize with provided credentials')

        self.headers = {'Authorization': 'Bearer ' + token}
        self.lel = 3
        self.courses = Courses(self)
        self.sections = Sections(self)
        self.units = Units(self)
        self.lessons = Lessons(self)


    def _fetch_object(self, resource_name: str, id: int):
        """
        :param resource_name: the name of resource
        :param id int: id of the resource to grub
        :return: kek
        """
        api_url = 'http://stepik.org/api/{}/{}'.format(resource_name, id)
        response = requests.get(api_url, headers=self.headers).json()
        return response['{}'.format(resource_name)][0]


    def _fetch_objects(self, resource_name: str, obj_ids: List[int]):
        objs = []
        # Fetch objects by 30 items,
        # so we won't bump into HTTP request length limits
        step_size = 30
        for i in range(0, len(obj_ids), step_size):
            obj_ids_slice = obj_ids[i:i + step_size]
            api_url = 'https://stepik.org/api/{}s?{}' \
                .format(resource_name,
                        '&'.join(f'ids[]={obj_id}' for obj_id in obj_ids_slice))
            response = requests.get(api_url, headers=self.headers).json()
            objs += response[f'{resource_name}s']
        return objs


class Courses(object):
    def __init__(self, stepik: Stepik):
        self.stepik = stepik


    def get(self, course_id: int) -> Course:
        return Course(self.stepik._fetch_object('courses', course_id))


    def update(self, course: Course):
        pass


class Sections(object):
    def __init__(self, stepik: Stepik):
        self.stepik = stepik


    def get(self, id: int) -> Section:
        return Section(self.stepik._fetch_object('sections', id))


class Units(object):
    def __init__(self, stepik: Stepik):
        self.stepik = stepik


    def get(self, id: int) -> Unit:
        return Unit(self.stepik._fetch_object('units', id))


class Lessons(object):
    def __init__(self, stepik: Stepik):
        self.stepik = stepik


    def get(self, id: int) -> Lesson:
        return Lesson(self.stepik._fetch_object('lessons', id))


# 1. Get your keys at https://stepik.org/oauth2/applications/
# (client type = confidential, authorization grant type = client credentials)
stepik = Stepik(client_id=id, client_secret=secret)
course = stepik.courses.get(course_id=14906)

for section in course.sections():
    print(section.title + ':')

    for unit in section.units():
        print('   - ' + unit.lesson().title)

    print()


for sec_id in course.sections:
    section = stepik.sections.get(sec_id)
    print(section.title + ':')

    for unit_id in section.units:
        unit = stepik.units.get(unit_id)
        lesson = stepik.lessons.get(unit.lesson)
        print('   - ' + lesson.title)

    print()

exit(0)




# course = fetch_object('course', course_id)
# sections = fetch_objects('section', course['sections'])
#
# for section in sections:
#
#     unit_ids = section['units']
#     units = fetch_objects('unit', unit_ids)
#
#     for unit in units:
#
#         lesson_id = unit['lesson']
#         lesson = fetch_object('lesson', lesson_id)
#
#         step_ids = lesson['steps']
#         steps = fetch_objects('step', step_ids)
#
#         for step in steps:
#             step_source = fetch_object('step-source', step['id'])
#             path = [
#                 '{} {}'.format(str(course['id']).zfill(2), course['title']),
#                 '{} {}'.format(str(section['position']).zfill(2), section['title']),
#                 '{} {}'.format(str(unit['position']).zfill(2), lesson['title']),
#                 '{}_{}_{}.step'.format(lesson['id'], str(step['position']).zfill(2), step['block']['name'])
#             ]
#             try:
#                 os.makedirs(os.path.join(os.curdir, *path[:-1]))
#             except:
#                 pass
#             filename = os.path.join(os.curdir, *path)
#             f = open(filename, 'w')
#             data = {
#                 'block': step_source['block'],
#                 'id':    str(step['id']),
#                 'time':  datetime.datetime.now().isoformat()
#             }
#             f.write(json.dumps(data))
#             f.close()
#             print(filename)
