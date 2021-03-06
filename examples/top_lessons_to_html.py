import os

from stepik import Stepik


def generate_html(top_lessons):
    rows = ""

    for lesson in top_lessons:
        rows += """<tr>
            <td><a href="https://stepik.org/lesson/{0.id}">{0.title}</a></td>
            <td>{0.viewed_by}</td>
            <td>{0.passed_by}</td>
            <td>{0.vote_delta}</td>
        </tr>""".format(lesson)

    template = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset=utf-8 />
            <title>Top lessons sorted by number of views</title>
        </head>
        <body>
        <table border="1" align="center">
            <tr>
                <th>Course title</th>
                <th>Viewed by</th>
                <th>Passed by</th>
                <th>Vote delta</th>
            </tr>
            {rows}
        </table>
        </body>
        </html>
    """

    return template


if __name__ == "__main__":
    from config import id, secret
    stepik = Stepik(id, secret, server='stepik.org')

    # We want to sort by votes, to take the most popular lessons
    top_lessons = stepik.lessons.iterate(by_vote_delta=True, limit=20)

    # Sort by number of views
    lessons = sorted(top_lessons, key=lambda l: l.viewed_by, reverse=True)

    # Generate html and write it to file
    with open(f'{os.path.dirname(__file__)}/out/top_lessons.html', 'w+') as f:
        f.write(generate_html(lessons))
