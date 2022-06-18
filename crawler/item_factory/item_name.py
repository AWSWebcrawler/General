"""select, validate and transform the item name from the given html-tree"""
import logging

from lxml import etree

from crawler.logging.decorator import decorator_for_logging


@decorator_for_logging
def _get_name(tree: etree) -> str:

    # Searching for name_tag on mobile devices
    name_tag = tree.find('.//span[@id = "title"]')

    if name_tag is not None:

        if name_tag.text.strip():
            logging.debug("item name found")
            return name_tag.text.strip()

    # Searching for name_tag on desktop devices
    name_tag = tree.find('.//span[@id = "productTitle"]')

    if name_tag is None:
        logging.warning("tag for item name not found in html tree")
        return None

    if name_tag.text.strip():
        logging.debug("item name found")
        return name_tag.text.strip()

    logging.warning("item name is empty")

    return None
