"""select, validate and transform the item on_sale_since from the given html-tree"""
import locale
import logging
import time

from lxml import etree

from crawler.logging.decorator import decorator_for_logging


@decorator_for_logging
def _get_on_sale_since(tree: etree):

    on_sale_since = _get_on_sale_since_from_list(tree)

    if on_sale_since is None:
        on_sale_since = _get_on_sale_since_from_table(tree)

    return on_sale_since


@decorator_for_logging
def _get_on_sale_since_from_list(tree: etree):

    div_tag = tree.find('.//div[@id = "detailBulletsWrapper_feature_div"]')

    if div_tag is None:
        return None

    span_tags = div_tag.findall('.//span[@class = "a-list-item"]')

    if div_tag is None:
        return None

    for list_item in span_tags:
        try:
            if (
                list_item.find('.//span[@class = "a-text-bold"]')
                .text.strip()
                .startswith("Im Angebot von Amazon.de seit")
            ):

                locale.setlocale(locale.LC_TIME, "de_DE")
                date_format = "%d. %B %Y"

                date = (list_item.findall(".//span")[1]).text

                new_date = time.strptime(date, date_format)

                return (
                    str(new_date.tm_mday)
                    + "."
                    + str(new_date.tm_mon)
                    + "."
                    + str(new_date.tm_year)
                )
        except (TypeError, AttributeError, IndexError):
            logging.warning("Can not parse item on_sale_since")

    return None


@decorator_for_logging
def _get_on_sale_since_from_table(tree: etree):

    table_tag = tree.find('.//table[@id = "productDetails_detailBullets_sections1"]')

    if table_tag is None:
        logging.info("tag for item on_sale_since not found in html tree")
        return None

    table_row_tags = table_tag.findall(".//tr")

    if table_row_tags is None:
        logging.info("tag for item on_sale_since not found in html tree")
        return None

    for table_item in table_row_tags:
        try:
            if (
                table_item.find(".//th")
                .text.strip()
                .startswith("Im Angebot von Amazon.de seit")
            ):

                date = (table_item.find(".//td")).text
                date = date.replace("\u200e", "").strip()

                locale.setlocale(locale.LC_TIME, "de_DE")
                date_format = "%d. %B %Y"

                new_date = time.strptime(date, date_format)

                return (
                    str(new_date.tm_mday)
                    + "."
                    + str(new_date.tm_mon)
                    + "."
                    + str(new_date.tm_year)
                )
        except (TypeError, AttributeError):
            logging.warning("Can not parse item on_sale_since")

    return None
