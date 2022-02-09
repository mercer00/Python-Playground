# decorated functions

def decorated_func(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} ran with the args {args} and kwargs {kwargs}")
        func(args)
    return wrapper


def add(*args):
    sum = 0
    for t in args:
        for a in t:
            sum += a
    print(sum)


decorated_add = decorated_func(add)
decorated_add(1, 3, 5, 2, 1)


@decorated_func
def mul(*args):
    total = 1
    for t in args:
        for a in t:
            total *= a
    print(total)


mul(3, 3, 2)
