#!/usr/bin/env python3

# Get list of all courses and create list of authors,
# ever involved in course creation process.
# Then print data aggregated by author name.

from collections import defaultdict

from stepik import Stepik

if __name__ == '__main__':
    from config import id, secret

    stepik = Stepik(client_id=id, client_secret=secret)
    author_courses = defaultdict(set)

    for course in stepik.courses.iterate(language='ru', by_popularity=True, limit=100):
        # ignore "dead" courses
        if not course.discussions_count:
            continue

        # for each author we will have all courses that were created with his participation
        for id in course.authors_ids:
            author_courses[id].add(course.title)

    # grab ~20 users' profiles per request
    authors = stepik.users.get_all(author_courses.keys())

    for author in authors:
        titles = [f'«{t}»' for t in author_courses[author.id]]

        print(author.first_name, author.last_name, 'took part in creating',
              'this course:' if len(titles) == 1 else 'these courses:',
              '\n ', ', '.join(titles), end='\n\n')
