"""Stores the error occuring during html data extraction
 and stores the error code and the HTML in a HTML file"""

import logging
from datetime import datetime as dt, timedelta, timezone
import boto3
from crawler.logging.decorator import decorator_for_logging


@decorator_for_logging
def store_error_html(error_dict: dict, settings_dict: dict) -> None:
    logging.debug("store_error_methode gestartet")
    error_string = list(error_dict.keys())[0]
    html = error_dict[error_string]
    if settings_dict["aws_env"]:
        store_to_html(error_string, html)
    else:
        store_to_s3(error_string, html, settings_dict)


@decorator_for_logging
def store_to_html(key: str, html: str):
    with open(key + ".html", "w", encoding='utf-8') as file:
        file.write(html)
        file.close()


@decorator_for_logging
def store_to_s3(error_string, html, settings_dict: dict) -> None:
    """Method gets the url and html.
     The html value is stored named after the url, then
    stored in S3 in html format."""
    bucket_name = settings_dict["s3_bucket"]
    now = dt.now(timezone(timedelta(hours=2)))
    s3_filename = f"ErrorHTML/" \
                  f"{str(now.year)}/" \
                  f"{str(now.month)}/" \
                  f"{str(now.day)}/" \
                  f"{str(now.hour)}/" \
                  f"{str(now.minute)}/" \
                  f"{error_string}.html"
    simple_storage_service = boto3.resource("s3")
    logging.debug("writing to bucket %s with filename %s", bucket_name, s3_filename)

    simple_storage_service.put_object(bucket_name, s3_filename, Body=html)

# error_dict_test = {"Error 404": "<body><button>Tische sauber</button></body>"}
# settings_dict = {
#     "aws_env": True,
#     "s3_bucket": "firstcrawlerbucket",
# }
# store_error_html(error_dict_test, settings_dict)
