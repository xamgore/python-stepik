#!/usr/bin/env python3

# Saves all step texts from course into single HTML file.
# Example of using multiple IDs in one API call.

from time import time
from os.path import dirname

from stepik.api.steps import Step
from stepik import Stepik


def step_to_html(step: Step):
    text = step.block['text']
    url = f'<a href="https://stepik.org/lesson/{step.lesson}/step/{step.position}">{step.id}</a>'
    return f'<h1>{url}</h1>{text}<hr>'


if __name__ == '__main__':
    from config import id, secret

    stepik = Stepik(client_id=id, client_secret=secret)
    course = stepik.courses.get(1)

    # Straightforward way, make request on each object separately:
    with open(f'{dirname(__file__)}/out/course-{course.id}.html', 'w', encoding='utf-8') as f:
        start = time()

        for section in course.sections:
            for unit in section.units:
                for step in unit.lesson().steps:
                    f.write(step_to_html(step))

        print(time() - start)  # 30 seconds

    # The fastest way, make request with the whole bunch of ids
    start = time()
    sections = course.sections.list()

    unit_ids = [id for sec in sections for id in sec.units_ids]
    units = stepik.units.get_all(unit_ids, keep_order=True)

    lesson_ids = [u.lesson_id for u in units]
    lessons = stepik.lessons.get_all(lesson_ids, keep_order=True)

    step_ids = [id for les in lessons for id in les.steps_ids]
    steps = stepik.steps.get_all(step_ids, keep_order=True)

    with open(f'{dirname(__file__)}/out/course-{course.id}.2.html', 'w', encoding='utf-8') as f:
        for step in steps:
            f.write(step_to_html(step))

    print(time() - start)  # 6 seconds
