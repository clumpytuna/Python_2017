import functools
import time
import sys


def profiler(func):
    calls = 0
    depth = 0

    @functools.wraps(func)
    def decorated(*args, **kwargs):
        nonlocal depth, calls

        calls += 1
        depth += 1

        start = time.time()
        value = func(*args, **kwargs)
        depth -= 1

        if depth == 0:
            decorated.last_time_taken = time.time() - start
            decorated.calls = calls
            calls = 0
        return value

    decorated.last_time_taken = 0
    decorated.calls = 0
    return decorated

exec(sys.stdin.read())


