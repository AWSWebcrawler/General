"""select, validate and transform the item sold_by_amazon from the given html-tree"""
import logging

from lxml import etree

from crawler.logging.decorator import decorator_for_logging


@decorator_for_logging
def _get_sold_by_amazon(tree: etree) -> bool:

    div_tag = tree.find('.//div[@id = "merchant-info"]')

    if div_tag is None:
        logging.info("tag for item sold_by_amazon not found in html tree")
        return False

    try:
        seller_tag = div_tag.find("span")
        seller: str = seller_tag.text
        seller = seller.split(" ")[-1].replace(".", "")

        if "Amazon" in seller:
            return True
        return False

    except (AttributeError, IndexError):
        logging.warning("Error during parsing sold_by_amazon tag")

    return None
