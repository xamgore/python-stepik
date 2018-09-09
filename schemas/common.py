import re


from functools import wraps


def run_once(f):
    """
    Runs a function (successfully) only once.
    The running can be reset by setting the `has_run` attribute to False
    """


    @wraps(f)
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.result = f(*args, **kwargs)
            wrapper.has_run = True
        return wrapper.result


    wrapper.has_run = False
    return wrapper


first_cap_re = re.compile('(.)([A-Z][a-z]+)')
all_cap_re = re.compile('([a-z0-9])([A-Z])')


def to_snake_case(string):
    s1 = first_cap_re.sub(r'\1_\2', string)
    return all_cap_re.sub(r'\1_\2', s1).lower()


def to_dash_case(string):
    s1 = first_cap_re.sub(r'\1-\2', string)
    return all_cap_re.sub(r'\1-\2', s1).lower()


def to_camel_case(dash_str: str) -> str:
    return ''.join(map(str.title, dash_str.split('-')))
