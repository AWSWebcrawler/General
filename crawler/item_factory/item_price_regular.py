"""select, validate and transform the item regular_price from the given html-tree"""
import logging
import re

from lxml import etree

from crawler.item_factory.item_current_price import _get_current_price
from crawler.logging.decorator import decorator_for_logging


@decorator_for_logging
def _get_regular_price(tree: etree) -> float:

    span_tag = tree.find(
        './/span[@class = "a-size-small a-color-secondary aok-align-center basisPrice"]'
    )

    if (span_tag is None) or ("Unverb. Preisempf.:" not in span_tag.text):
        logging.info(
            "item regular price not found -> calling function for item current price"
        )
        return _get_current_price(tree)

    current_price_tag = span_tag.find('.//span[@class = "a-offscreen"]')

    if current_price_tag is None:
        logging.info(
            "item regular price not found -> calling function for item current price"
        )
        return _get_current_price(tree)

    try:
        # Replacing non-numeric characters with blanks
        # -> Stripping all leading and following whitespaces
        # -> replacing the blank in the middle of the number with a dot
        current_price: str = current_price_tag.text
        current_price = re.sub(r"\D", " ", current_price)
        current_price = re.sub(" ", ".", current_price.strip())

        if (
            (re.match(r"[0-9]+\.[0-9][0-9]", current_price))
            or (re.match(r"[0-9]+\.[0-9]", current_price))
            or (current_price.isalnum())
            and (current_price is not None)
        ):
            logging.debug("item regular_price found")
            return float(current_price)

        logging.warning("item regular_price is empty")

    except (TypeError, AttributeError, ValueError):
        logging.warning("Can not parse item regular_price")

    logging.info(
        "item regular price not found -> calling function for item current price"
    )
    return _get_current_price(tree)
