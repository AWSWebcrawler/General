"""select, validate and transform the item manufacturer from the given html-tree"""
import logging

from lxml import etree

from crawler.logging.decorator import decorator_for_logging


@decorator_for_logging
def _get_manufacturer(tree: etree):

    manufacturer = _get_manufacturer_from_list(tree)

    if manufacturer is None:
        manufacturer = _get_manufacturer_from_table(tree)

    return manufacturer


@decorator_for_logging
def _get_manufacturer_from_list(tree: etree):

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
                .startswith("Hersteller")
            ):
                return list_item.findall(".//span")[1].text
        except (TypeError, AttributeError, IndexError):
            logging.warning("Can not parse item manufacturer")

    return None


@decorator_for_logging
def _get_manufacturer_from_table(tree: etree):

    table_tag = tree.find('.//table[@id = "productDetails_techSpec_section_1"]')

    if table_tag is None:
        logging.info("tag for item manufacturer not found in html tree")
        return None

    table_row_tags = table_tag.findall(".//tr")

    if table_row_tags is None:
        logging.info("tag for item manufacturer not found in html tree")
        return None

    for table_item in table_row_tags:
        try:
            if table_item.find(".//th").text.strip().startswith("Hersteller"):
                product_dimension = table_item.find(".//td").text
                return product_dimension.replace("\u200e", "").strip()
        except (TypeError, AttributeError):
            logging.warning("Can not parse item manufacturer")

    return None
