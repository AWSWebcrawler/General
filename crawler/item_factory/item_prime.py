"""select, validate and transform the item prime from the given html-tree"""
from lxml import etree

from crawler.logging.decorator import decorator_for_logging


@decorator_for_logging
def _get_prime(tree: etree) -> bool:

    div_tag = tree.find('.//div[@id = "bbop-sbbop-container"]')

    if div_tag is not None:
        return True
    return False
