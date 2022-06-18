"""select, validate and transform the item current_price from the given html-tree"""
import logging
import re

from lxml import etree

from crawler.logging.decorator import decorator_for_logging


@decorator_for_logging
def _get_current_price(tree: etree) -> float:

    price_tag = tree.find(
        './/div[@class = "a-section aok-hidden twister-plus-buying-options-price-data"]'
    )

    if price_tag is None:
        logging.warning("tag for item current_price not found in html tree")
        return None

    try:
        price: str = price_tag.text.split('"priceAmount":')[1].split(",")[0]

        if price.strip() and price is not None:
            logging.debug("item current_price found")

            if re.match(r"[0-9]+\.[0-9][0-9]", price):
                return float(price)

            logging.warning("Item current_price has a wrong format")
            return float(price)

        logging.warning("item current_price is empty")

    except (AttributeError, IndexError):
        logging.warning("Error during parsing current_price tag")

    return None
