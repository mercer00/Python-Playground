# using decoraters to print time taken to run

import time


def decorated_func(func):
    def wrapped_func(*args, **kwargs):
        first = time.time()
        func(*args, **kwargs)
        last = time.time()
        time_taken = last - first
        print(f"Time taken to run {func.__name__} ==> {time_taken}s")
    return wrapped_func


@decorated_func
def add(x, y, z):
    print(x + y + z)


add(10, 20, 30)
