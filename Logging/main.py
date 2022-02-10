import logging

logging.basicConfig(level=logging.INFO, filename="./Logging/decorater.log",
                    format="%(asctime)s:%(levelname)s --> %(message)s")


def decorated_func(func):
    def wrapped(*args, **kwargs):
        logging.info(
            f"{func.__name__} was run with the args {args} and the kwargs {kwargs}")
        print(func(*args, **kwargs))
    return wrapped


@decorated_func
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


add(1, 3, 5, 2)
