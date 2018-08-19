# Run with Python 3
# Saves all step sources into foldered structure
import datetime
import json
import os

from config import id, secret
from stepik import Stepik

# 1. Get your keys at https://stepik.org/oauth2/applications/
# (client type = confidential, authorization grant type = client credentials)
if __name__ == '__main__':
    stepik = Stepik(client_id=id, client_secret=secret)
    course = stepik.courses.get(course_id=1612)  # Docker

    for section in course.sections:
        for unit in section.units.list():
            lesson = stepik.lessons.get(unit.lesson)
            for step in lesson.steps:
                source = stepik.step_sources.get(step.id)

                path = [
                    f'{str(course.id).zfill(2)} {course.title}',
                    f'{str(section.position).zfill(2)} {section.title}',
                    f'{str(unit.position).zfill(2)} {lesson.title}',
                    f'{lesson.id}_{str(step.position).zfill(2)}_{step.block["name"]}.step'
                ]

                try:
                    os.makedirs(os.path.join(os.curdir, *path[:-1]))
                except:
                    pass

                filename = os.path.join(os.curdir, *path)
                f = open(filename, 'w')
                data = {
                    'block': source.block,
                    'id':    str(step.id),
                    'time':  datetime.datetime.now().isoformat()
                }
                f.write(json.dumps(data))
                f.close()
                print(filename)
