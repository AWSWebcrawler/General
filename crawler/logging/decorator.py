import logging


def decorator_for_logging(func):
    def wrapper_logging(*args, **kwargs):
        logging.debug("Calling function " + func.__name__)
        return func(*args, **kwargs)
    return wrapper_logging
