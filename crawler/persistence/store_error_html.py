"""Stores the error occuring during html data extraction
 and stores the error code and the HTML in a HTML file"""

import logging
from datetime import datetime as dt, timedelta, timezone
import boto3
from crawler.logging.decorator import decorator_for_logging


@decorator_for_logging
def store_error_html(error_dict: dict, settings_dict: dict) -> None:
    if settings_dict["aws_env"]:
        for item in error_dict:
            store_to_s3(item, error_dict[item], settings_dict)
    else:
        for item in error_dict:
            store_to_csv_html(item, error_dict[item])


@decorator_for_logging
def store_to_csv_html(error_string: str, html_list: list):
    body = ''
    with open("../output/" + error_string + ".csv", "w", encoding='utf-8') as file:
        for item in html_list:
            body += item.replace(",", '')
            body += ','
        file.write(body)
        file.close()


@decorator_for_logging
def store_to_s3(error_string: str, html_list: list, settings_dict: dict) -> None:
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
                  f"{error_string}.csv"
    body = ""

    for item in html_list:
        item = str(item).replace(',', '')
        body += item
        body += ','

    simple_storage_service = boto3.resource("s3")
    logging.debug("writing to bucket %s with filename %s", bucket_name, s3_filename)
    simple_storage_service.Bucket(bucket_name).put_object(key=s3_filename, Body=body)
