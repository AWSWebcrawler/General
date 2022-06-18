"""select, validate and transform the item product_id from the given html-tree"""
import logging

from lxml import etree

from crawler.item_factory.item_brand import _get_brand
from crawler.logging.decorator import decorator_for_logging


@decorator_for_logging
def _get_product_id(tree: etree):

    if _get_brand(tree) == "Amazon":
        return None

    product_id = _get_product_id_from_list(tree)

    if product_id is None:
        product_id = _get_product_id_from_table(tree)

    return product_id


@decorator_for_logging
def _get_product_id_from_list(tree: etree):

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
                .startswith("Modellnummer")
                or list_item.find('.//span[@class = "a-text-bold"]')
                .text.strip()
                .startswith("Teilenummer")
                or list_item.find(".//th")
                .text.strip()
                .startswith("Artikelnummer")
            ):
                return (list_item.findall(".//span")[1]).text
        except (TypeError, AttributeError, IndexError):
            logging.warning("Can not parse item product_id")

    return None


@decorator_for_logging
def _get_product_id_from_table(tree: etree):

    table_tag = tree.find('.//table[@id = "productDetails_techSpec_section_1"]')

    if table_tag is None:
        logging.info("tag for item product_id not found in html tree")
        return None

    table_row_tags = table_tag.findall(".//tr")

    if table_row_tags is None:
        logging.info("tag for item product_id not found in html tree")
        return None

    for table_item in table_row_tags:
        try:
            if (
                table_item.find(".//th").text.strip().startswith("Modellnummer")
                or table_item.find(".//th").text.strip().startswith("Teilenummer")
                or table_item.find(".//th").text.strip().startswith("Artikelnummer")
            ):
                product_dimension = (table_item.find(".//td")).text
                return product_dimension.replace("\u200e", "").strip()
        except (TypeError, AttributeError):
            logging.warning("Can not parse item product_id")

    return None
