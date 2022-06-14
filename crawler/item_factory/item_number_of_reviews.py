"""select, validate and transform the item number_of_reviews from the given html-tree"""
import logging
import re

from lxml import etree

from crawler.logging.decorator import decorator_for_logging


@decorator_for_logging
def _get_number_of_reviews(tree: etree):

    span_tag = tree.find('.//span[@id = "acrCustomerReviewText"]')

    if span_tag is None:
        logging.info("tag for item number_of_reviews not found in html tree")
        return None
    try:
        number_of_reviews: str = re.sub(r"\D", " ", span_tag.text)
        number_of_reviews = number_of_reviews.replace(" ", "")

        if (re.match(r"[0-9]+", number_of_reviews)) and (number_of_reviews is not None):
            return int(number_of_reviews)
        return None
    except (TypeError, AttributeError, ValueError):
        logging.warning("Can not parse item number_of_reviews")

    return None
