"""select, validate and transform the item brand from the given html-tree"""
import logging

from lxml import etree

from crawler.logging.decorator import decorator_for_logging


@decorator_for_logging
def _get_brand(tree: etree):

    div_tag = tree.find('.//div[@id = "bylineInfo_feature_div"]')

    if div_tag is None:
        logging.info("tag for item brand not found in html tree")
        return None

    anchor_tag = div_tag.find(".//a")

    if anchor_tag is None:
        logging.info("tag for item brand not found in html tree")
        return None

    try:
        if "Amazon" in anchor_tag.text:
            return "Amazon"
        try:
            return anchor_tag.text.split("den ")[1].replace("-Store", "")
        except (TypeError, AttributeError, IndexError):
            return anchor_tag.text.split("Marke: ")[1]
    except (TypeError, AttributeError, IndexError):
        logging.warning("Can not parse item brand")

    return None
