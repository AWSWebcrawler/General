"""select, validate and transform the item regular_price from the given html-tree"""
import logging
import re

from lxml import etree

from crawler.item_factory.item_current_price import _get_current_price
from crawler.logging.decorator import decorator_for_logging


@decorator_for_logging
def _get_regular_price(tree: etree) -> float:

    regular_price = _get_regular_price_from_table(tree)

    if regular_price is None:
        regular_price = _get_regular_price_from_span(tree)

    if regular_price is None:
        return _get_current_price(tree)
    return regular_price


@decorator_for_logging
def _get_regular_price_from_table(tree: etree) -> float:

    table_tags = tree.findall('.//table[@class = "a-lineitem a-align-top"]')

    if table_tags is None:
        return None

    try:
        table_tag = table_tags[0]
    except (IndexError, TypeError):
        return None

    tr_tags = table_tag.findall(".//tr")

    try:
        regular_price = None

        for tr_tag in tr_tags:
            if (
                "Unverb. Preisempf.:" in tr_tag.find(".//td").text
                or "Zuletzt niedrigster Preis:" in tr_tag.find(".//td").text
                or "Bündel-Listenpreis:" in tr_tag.find(".//td").text
            ):
                td_tag = tr_tag.findall(".//td")[1]
                regular_price = td_tag.find('.//span[@class = "a-offscreen"]').text
                break

        # Replacing non-numeric characters with blanks
        # -> Stripping all leading and following whitespaces
        # -> replacing the blank in the middle of the number with a dot
        regular_price = re.sub(r"\D", " ", regular_price)
        regular_price = re.sub(" ", ".", regular_price.strip())

        if (
            (re.match(r"[0-9]+\.[0-9][0-9]", regular_price))
            or (re.match(r"[0-9]+\.[0-9]", regular_price))
            or (regular_price.isalnum())
            and (regular_price is not None)
        ):
            logging.debug("item regular_price found")
            return float(regular_price)

        logging.warning("item regular_price is empty")

    except (TypeError, AttributeError, ValueError):
        logging.warning("Can not parse item regular_price")

    return None


@decorator_for_logging
def _get_regular_price_from_span(tree: etree) -> float:

    span_tag = tree.find(
        './/span[@class = "a-size-small a-color-secondary aok-align-center basisPrice"]'
    )

    if (
        (span_tag is None)
        or ("Unverb. Preisempf.:" not in span_tag.text)
        and ("Statt:" not in span_tag.text)
    ):
        logging.info("item regular price not found in html tree")
        return None

    regular_price_tag = span_tag.find('.//span[@class = "a-offscreen"]')

    if regular_price_tag is None:
        logging.info("item regular price not found in html tree")
        return None

    try:
        # Replacing non-numeric characters with blanks
        # -> Stripping all leading and following whitespaces
        # -> replacing the blank in the middle of the number with a dot
        regular_price: str = regular_price_tag.text
        regular_price = re.sub(r"\D", " ", regular_price)
        regular_price = re.sub(" ", ".", regular_price.strip())

        if (
            (re.match(r"[0-9]+\.[0-9][0-9]", regular_price))
            or (re.match(r"[0-9]+\.[0-9]", regular_price))
            or (regular_price.isalnum())
            and (regular_price is not None)
        ):
            logging.debug("item regular_price found")
            return float(regular_price)

        logging.warning("item regular_price is empty")

    except (TypeError, AttributeError, ValueError):
        logging.warning("Can not parse item regular_price")

    logging.info("item regular price not found in html tree")
    return None
