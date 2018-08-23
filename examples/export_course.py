#!/usr/bin/env python3

# Save course (all step sources) as in a foldered structure.
# Requires instructor access.

import datetime
import json
import os

from config import id, secret
from stepik import Stepik

stepik = Stepik(client_id=id, client_secret=secret)
course = stepik.courses.get(course_id=1612)  # Docker

for section in course.sections:
    for unit in section.units:
        lesson = unit.lesson()

        for step in unit.lesson().steps:
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
            f.write(json.dumps(data, indent=2, ensure_ascii=False))
            f.close()
            print(filename)
