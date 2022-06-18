"""select, validate and transform the item amazon_choice_for from the given html-tree"""
import logging

from lxml import etree

from crawler.item_factory.item_amazon_choice import _get_amazon_choice
from crawler.logging.decorator import decorator_for_logging


@decorator_for_logging
def _get_amazon_choice_for(tree: etree):

    if not _get_amazon_choice(tree):
        logging.info("tag for item amazon_choice_for not found in html tree")
        return None

    div_tag = tree.find('.//div[@id = "acBadge_feature_div"]')
    anchor_tag = div_tag.find(".//a")

    if anchor_tag is None:
        logging.info("tag for item amazon_choice_for not found in html tree")
        return False

    try:
        amazon_choice_for = anchor_tag.text

        if amazon_choice_for:
            return amazon_choice_for
    except (TypeError, AttributeError):
        logging.warning("Can not parse item amazon_choice_for")
    return None
