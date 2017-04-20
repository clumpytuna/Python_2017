import functools
import sys


def takes(*types):

    def outside_wrapper(func):
        @functools.wraps(func)
        def inside_wrapper(*args, **kwargs):

            for arg, type_ in zip(args, types):
                if type(arg) != type_:
                    raise TypeError('Wrong type')
            index = 0

            for key in kwargs:
                if type(kwargs[key]) != types[index]:
                    raise TypeError('Wrong type')
                index += 1

            return func(*args, **kwargs)
        return inside_wrapper
    return outside_wrapper
exec(sys.stdin.read())


