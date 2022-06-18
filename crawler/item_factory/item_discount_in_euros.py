"""select, validate and transform the item discount_in_euros from the given html-tree"""
import logging
import re

from lxml import etree

from crawler.item_factory.item_current_price import _get_current_price
from crawler.item_factory.item_price_regular import _get_regular_price
from crawler.logging.decorator import decorator_for_logging


@decorator_for_logging
def _get_discount_in_euros(tree: etree) -> float:

    discount: float = _get_discount_in_euros_from_table(tree)

    if discount is None:
        discount = _calculate_discount_in_euros(tree)

    return discount


@decorator_for_logging
def _get_discount_in_euros_from_table(tree: etree) -> float:

    table_data_tag = tree.find('.//td[@class = "a-span12 a-color-price a-size-base"]')

    if table_data_tag is None:
        return None

    discount_tag = table_data_tag.find('.//span[@class = "a-offscreen"]')

    if discount_tag is None:
        return None

    try:
        # Replacing non-numeric characters with blanks
        # -> Stripping all leading and following whitespaces
        # -> replacing the blank in the middle of the number with a dot
        discount: str = re.sub(r"\D", " ", discount_tag.text)
        discount = re.sub(" ", ".", discount.strip())

        if (
            (re.match(r"[0-9]+\.[0-9][0-9]", discount))
            or (re.match(r"[0-9]+\.[0-9]", discount))
            or (discount.isalnum())
            and (discount is not None)
        ):
            logging.debug("item discount_in_euros found")
            return float(discount)
    except (TypeError, AttributeError, ValueError):
        logging.warning("Can not parse item discount_in_euros")

    return None


@decorator_for_logging
def _calculate_discount_in_euros(tree: etree) -> float:
    """Calculating item discount_in_euros using above implemented methods"""

    price: float = _get_current_price(tree)
    regular_price: float = _get_regular_price(tree)

    if price is None or regular_price is None:
        logging.warning("Can`t calculate item discount_in_euros")
        return None

    if price == regular_price:
        return None

    try:
        discount_in_euros = regular_price - price
        return round(discount_in_euros, 2)

    except TypeError:
        logging.warning("Error during calculating item discount_in_euros")

    return None
