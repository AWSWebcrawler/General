"""Returns the time part of the given datetime"""
from datetime import datetime

from crawler.logging.decorator import decorator_for_logging


@decorator_for_logging
def _get_time(datetime_now: datetime) -> str:

    current_time = datetime_now.strftime("%H:%M:%S")
    return current_time
