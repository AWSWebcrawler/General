"""validate and returns the given url"""
import logging
import re

from crawler.logging.decorator import decorator_for_logging


@decorator_for_logging
def _get_url(url: str) -> str:

    if re.match("^https://www.amazon.de", url):
        return url

    logging.warning("Item url doesn`t start with https://www.amazon.de")
    return url
