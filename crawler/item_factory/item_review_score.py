"""select, validate and transform the item review_score from the given html-tree"""
import logging
import re

from lxml import etree

from crawler.logging.decorator import decorator_for_logging


@decorator_for_logging
def _get_review_score(tree: etree):

    span_tag = tree.find('.//span[@id = "acrPopover"]')

    if span_tag is None:
        logging.info("tag for item review_score not found in html tree")
        return None
    try:
        review_score: str = span_tag.attrib["title"].split(" ")[0]

        if (re.match(r"[0-9],[0-9]", review_score)) and (review_score is not None):
            return review_score
        return None
    except (TypeError, AttributeError, IndexError):
        logging.warning("Can not parse item review_score")

    return None
