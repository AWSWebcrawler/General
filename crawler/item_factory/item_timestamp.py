"""Returns the unix timestamp of the given datetime"""
from datetime import datetime

from crawler.logging.decorator import decorator_for_logging


@decorator_for_logging
def _get_timestamp(datetime_now: datetime) -> float:

    timestamp = datetime.timestamp(datetime_now)
    return timestamp
