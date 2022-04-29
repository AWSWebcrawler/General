from crawler.header_creater.create_header import generate_header
from crawler.log import logging_config

test_map = "android"

test_header = generate_header(test_map)
logging_config.warning(test_header)
