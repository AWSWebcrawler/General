"""select, validate and transform the item percent_discount from the given html-tree"""
import logging
import re

from lxml import etree

from crawler.item_factory.item_current_price import _get_current_price
from crawler.item_factory.item_price_regular import _get_regular_price
from crawler.logging.decorator import decorator_for_logging


@decorator_for_logging
def _get_percent_discount(tree: etree) -> float:

    percent_discount: float = _get_percent_discount_from_table(tree)

    if percent_discount is None:
        percent_discount = _get_percent_discount_from_span_tag(tree)

    if percent_discount is None:
        percent_discount = _calculate_percent_discount(tree)

    return percent_discount


@decorator_for_logging
def _get_percent_discount_from_table(tree: etree) -> float:

    table_data_tag = tree.find('.//td[@class = "a-span12 a-color-price a-size-base"]')

    if table_data_tag is None:
        return None

    discount_tag = table_data_tag.find('.//span[@data-a-color = "price"]')

    if discount_tag is None:
        return None

    try:
        # Replacing non-numeric characters with blanks
        # -> Stripping all leading and following whitespaces
        # -> replacing the blank in the middle of the number with a dot
        discount: str = re.sub(r"\D", " ", discount_tag.tail)
        discount = re.sub(" ", ".", discount.strip())

        if (
            (re.match(r"[0-9]+\.[0-9][0-9]", discount))
            or (re.match(r"[0-9]+\.[0-9]", discount))
            or (discount.isalnum())
            and (discount is not None)
        ):
            logging.debug("item percent_discount found")
            return float(discount)

    except (TypeError, AttributeError, ValueError):
        pass

    return None


@decorator_for_logging
def _get_percent_discount_from_span_tag(tree: etree) -> float:

    span_tag = tree.find(
        './/span[@class = "a-size-large a-color-price savingPriceOverride '
        'aok-align-center reinventPriceSavings'
        'PercentageMargin savingsPercentage"]'
    )
    if span_tag is None:
        return None

    try:
        discount: str = re.sub(r"\D", " ", span_tag.text)
        discount = re.sub(" ", ".", discount.strip())

        if (
            (re.match(r"[0-9]+\.[0-9][0-9]", discount))
            or (re.match(r"[0-9]+\.[0-9]", discount))
            or (discount.isalnum())
            and (discount is not None)
        ):
            logging.debug("item percent_discount found")
            return float(discount)

    except (TypeError, AttributeError, ValueError):
        pass

    return None


@decorator_for_logging
def _calculate_percent_discount(tree: etree) -> float:

    price: float = _get_current_price(tree)
    regular_price: float = _get_regular_price(tree)

    if (price is None) or (regular_price is None) or (regular_price == 0.0):
        logging.warning("Can`t calculate item percent_discount")
        return None

    if price == regular_price:
        return None

    try:
        discount_in_euros = regular_price - price
        percent_discount = discount_in_euros * 100 / regular_price
        return round(percent_discount, 2)

    except (TypeError, ZeroDivisionError):
        logging.warning("Error during calculating item percent_discount")

    return None
