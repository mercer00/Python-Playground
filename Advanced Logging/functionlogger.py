import logging
import classlogger

funcLogger = logging.getLogger(__name__)
funcLogger.setLevel(logging.DEBUG)

funcFormat = logging.Formatter("%(asctime)s:%(levelname)s --> %(message)s")

funcHandler = logging.FileHandler("./Advanced Logging/function.log")
funcHandler.setFormatter(funcFormat)
funcLogger.addHandler(funcHandler)

streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.INFO)
streamFormat = logging.Formatter("%(asctime)s --> %(message)s")
streamHandler.setFormatter(streamFormat)

funcLogger.addHandler(streamHandler)


def logging_func(func):
    def wrapper(*args, **kwargs):
        funcLogger.debug(
            f"{func.__name__} ran with the args {args} and the kwargs {kwargs}")
        funcLogger.info(f"Logged")
        print(func(*args, **kwargs))
    return wrapper


@logging_func
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


add(1, 2, 5)
