"""select, validate and transform the item asin from the given html-tree"""
import logging
import re

from lxml import etree

from crawler.logging.decorator import decorator_for_logging


@decorator_for_logging
def _get_asin(tree: etree) -> str:

    asin_tag = tree.find('.//input[@id = "ASIN"]')

    if asin_tag is None:
        logging.warning("tag for item asin not found in html tree")
        return None

    try:
        asin: str = asin_tag.attrib["value"]

        if asin.strip() and asin is not None:
            logging.info("item asin found")

            if re.match("^([0-9]|[A-Z])+$", asin):
                return asin

            logging.warning("Item asin has a wrong format")
            return asin

        logging.warning("item asin is empty")

    except AttributeError:
        logging.warning("Error during parsing asin tag")

    return None
