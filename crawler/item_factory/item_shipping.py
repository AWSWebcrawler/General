"""select, validate and transform the item shipping from the given html-tree"""
import logging
import re

from lxml import etree

from crawler.logging.decorator import decorator_for_logging


@decorator_for_logging
def _get_shipping(tree: etree) -> float:

    span_tag = tree.find(".//span[@data-csa-c-delivery-price]")

    if span_tag is None:
        logging.info("tag for item shipping not found in html tree")
        return None
    try:
        shipping: str = span_tag.attrib["data-csa-c-delivery-price"]
        shipping = re.sub(r"\D", " ", shipping)
        shipping = re.sub(" ", ".", shipping.strip())

        if (
            (re.match(r"[0-9]+\.[0-9][0-9]", shipping))
            or (re.match(r"[0-9]+\.[0-9]", shipping))
            or (shipping.isalnum())
            and (shipping is not None)
        ):
            return float(shipping)
        return None
    except (TypeError, AttributeError, ValueError):
        logging.warning("Can not parse item shipping")

    return None
