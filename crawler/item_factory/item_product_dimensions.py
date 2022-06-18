"""select, validate and transform the
item product_dimensions from the given html-tree"""
import logging

from lxml import etree

from crawler.logging.decorator import decorator_for_logging


@decorator_for_logging
def _get_product_dimensions(tree: etree):

    product_dimension = _get_product_dimensions_from_list(tree)

    if product_dimension is None:
        product_dimension = _get_product_dimensions_from_table(tree)

    if product_dimension is None:
        product_dimension = _get_product_dimensions_from_div(tree)

    return product_dimension


@decorator_for_logging
def _get_product_dimensions_from_list(tree: etree):

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
                .startswith("Produktabmessungen")
            ) or list_item.find(".//th").text.strip().startswith(
                "Verpackungsabmessungen"
            ):
                product_dimensions = (list_item.findall(".//span")[1]).text
                if ";" in product_dimensions:
                    return product_dimensions.split(";")[0]
                return product_dimensions
        except (TypeError, AttributeError, IndexError):
            logging.warning("Can not parse item product_dimensions")

    return None


@decorator_for_logging
def _get_product_dimensions_from_table(tree: etree):

    table_tag = tree.find('.//table[@id = "productDetails_techSpec_section_1"]')

    if table_tag is None:
        return None

    table_row_tags = table_tag.findall(".//tr")

    if table_row_tags is None:
        return None

    for table_item in table_row_tags:
        try:
            if table_item.find(".//th").text.strip().startswith(
                "Produktabmessungen"
            ) or table_item.find(".//th").text.strip().startswith(
                "Verpackungsabmessungen"
            ):
                product_dimensions = (table_item.find(".//td")).text
                product_dimensions = product_dimensions.replace("\u200e", "").strip()
                if ";" in product_dimensions:
                    return product_dimensions.split(";")[0]
                return product_dimensions
        except (TypeError, AttributeError):
            logging.warning("Can not parse item product_dimensions")

    return None


@decorator_for_logging
def _get_product_dimensions_from_div(tree: etree):

    div_tag_id = tree.find('.//div[@id = "tech"]')

    if div_tag_id is None:
        logging.info("tag for item product_dimensions not found in html tree")
        return None

    try:
        div_tag_class = div_tag_id.findall(
            './/div[@class = "content-grid-row-wrapper "]'
        )[3]
    except IndexError:
        div_tag_parent = div_tag_id.getparent()
        try:
            div_tag_class = div_tag_parent.findall(
                './/div[@class = "content-grid-row-wrapper "]'
            )[3]
        except (IndexError, AttributeError):
            logging.info("tag for item product_dimensions not found in html tree")
            return None

    if div_tag_class is None:
        logging.info("tag for item product_dimensions not found in html tree")
        return None

    table_rows = div_tag_class.findall(".//tr")

    for table_item in table_rows:
        try:
            if table_item.find(".//strong").text.strip().startswith("Abmessungen"):
                product_dimensions = (table_item.findall(".//p")[1]).text
                if ";" in product_dimensions:
                    return product_dimensions.split(";")[0]
                return product_dimensions
        except (TypeError, AttributeError, IndexError):
            logging.warning("Can not parse item product_dimensions")

    return None
