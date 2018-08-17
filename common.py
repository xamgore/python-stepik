def readonly(f):
    return f


def required(f):
    return f


from functools import wraps


def run_once(f):
    """Runs a function (successfully) only once.
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
