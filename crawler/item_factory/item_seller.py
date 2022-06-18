"""select, validate and transform the item seller from the given html-tree"""
import logging

from lxml import etree

from crawler.item_factory.item_sold_by_amazon import _get_sold_by_amazon
from crawler.logging.decorator import decorator_for_logging


@decorator_for_logging
def _get_seller(tree: etree) -> str:

    if _get_sold_by_amazon(tree):
        return "Amazon"

    div_tag = tree.find('.//div[@id = "merchant-info"]')

    if div_tag is None:
        logging.info("tag for item seller not found in html tree")
        return None

    try:
        anchor_tag = div_tag.find("a")
        seller_tag = anchor_tag.find("span")
        seller: str = seller_tag.text

        if seller.strip() and seller is not None:
            logging.debug("item seller found")
            return seller

        logging.warning("item seller is empty")

    except AttributeError:
        logging.warning("Error during parsing seller tag")

    return None
