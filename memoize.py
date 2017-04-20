import functools
import sys


def memoize(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = args + tuple(kwargs.items())

        if key in cache:
            return cache[key]

        value = func(*args, **kwargs)
        cache[key] = value

        return value
    return wrapper
exec(sys.stdin.read())


