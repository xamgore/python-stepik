#!/usr/bin/env python3

# Save course (all step sources) in a foldered structure.
# Requires instructor access.

import datetime
import json
from os.path import dirname, join
from os import makedirs

from config import id, secret
from stepik import Stepik

stepik = Stepik(client_id=id, client_secret=secret)
course = stepik.courses.get(id=14906)  # Docker

for section in course.sections:
    for unit in section.units:
        lesson = unit.lesson()

        for step in unit.lesson().steps:
            source = stepik.step_sources.get(step.id)

            data = {
                'block': source.block,
                'id':    str(step.id),
                'time':  datetime.datetime.now().isoformat()
            }

            path = [
                f'{str(course.id).zfill(2)} {course.title}',
                f'{str(section.position).zfill(2)} {section.title}',
                f'{str(unit.position).zfill(2)} {lesson.title}',
                f'{lesson.id}_{str(step.position).zfill(2)}_{step.block["name"]}.step'
            ]

            makedirs(join(dirname(__file__), 'out', *path[:-1]), exist_ok=True)
            filename = join(dirname(__file__), 'out', *path)

            with open(filename, 'w') as f:
                f.write(json.dumps(data, indent=2, ensure_ascii=False))
                print(filename)
