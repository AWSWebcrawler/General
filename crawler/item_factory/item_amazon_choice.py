"""select, validate and transform the item amazon_choice from the given html-tree"""
import logging

from lxml import etree

from crawler.logging.decorator import decorator_for_logging


@decorator_for_logging
def _get_amazon_choice(tree: etree) -> bool:

    div_tag = tree.find('.//div[@id = "acBadge_feature_div"]')

    if div_tag is None:
        logging.info("tag for item amazon_choice not found in html tree")
        return False

    span_tags = div_tag.findall("div/span/span/span")

    if span_tags is not None and len(span_tags) > 1:
        return True
    return False
