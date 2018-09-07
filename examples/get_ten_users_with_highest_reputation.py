from typing import Iterable


def take(n: int, iterable: Iterable):
    # take(2, [1,4,6,4,1]) --> 1 4
    assert n > 0

    i = 0
    for x in iterable:
        yield x
        i += 1
        if i >= n:
            break


if __name__ == '__main__':
    from config import id, secret
    from stepik import Stepik

    stepik = Stepik(id, secret)
    top_users = stepik.users.iterate(by_reputation=True)

    for user in take(10, top_users):
        print(user.full_name, user.reputation)
