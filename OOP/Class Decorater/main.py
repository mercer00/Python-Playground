# decorated class

class decorated_class:
    def __init__(self, wrapped_func):
        self.wrapped_func = wrapped_func

    def __call__(self, *args, **kwargs):
        print(
            f"{self.wrapped_func.__name__} ran with the args {args} and kwargs {kwargs}")
        self.wrapped_func(args)


def add(*args):
    sum = 0
    for t in args:
        for a in t:
            sum += a
    print(sum)


decorated_add = decorated_class(add)
decorated_add(1, 3, 5, 2, 1)


@decorated_class
def mul(*args):
    total = 1
    for t in args:
        for a in t:
            total *= a
    print(total)


mul(3, 3, 2)
