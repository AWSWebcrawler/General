"""Returns the date part of the given datetime"""
from datetime import datetime

from crawler.logging.decorator import decorator_for_logging


@decorator_for_logging
def _get_date(datetime_now: datetime) -> str:

    date = datetime_now.strftime("%Y-%m-%d")
    return date
