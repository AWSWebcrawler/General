"""Stores the error occuring during html data extraction
 and stores the error code and the HTML in a HTML file"""

import logging
from datetime import datetime as dt, timedelta, timezone
import boto3
from crawler.logging.decorator import decorator_for_logging


@decorator_for_logging
def store_error_url(error_dict: dict, settings_dict: dict) -> None:
    logging.debug("store_error_methode gestartet")
    url = list(error_dict.keys())[0]
    error = error_dict[url]
    if settings_dict["aws_env"]:
        store_to_csv_error_url(url, error)
    else:
        store_to_s3(url, error, settings_dict)


@decorator_for_logging
def store_to_csv_error_url(key: str, html: str):
    with open(key + ".csv", "w", encoding='utf-8') as file:
        file.write(html)
        file.close()


@decorator_for_logging
def store_to_s3(url, problem, settings_dict: dict) -> None:
    """
    Method gets an product dictionary and the name of the used client.
    Items from the product_dict are then
    stored in S3 in CSV format."""
    bucket_name = settings_dict["s3_bucket"]
    now = dt.now(timezone(timedelta(hours=2)))
    s3_filename = f"ErrorURL/" \
                  f"{str(now.year)}/" \
                  f"{str(now.month)}/" \
                  f"{str(now.day)}/" \
                  f"{str(now.hour)}/" \
                  f"{str(now.minute)}/" \
                  f"{url}.csv"
    simple_storage_service = boto3.resource("s3")
    logging.debug("writing to bucket %s with filename %s", bucket_name, s3_filename)

    # simple_storage_service.put_object(bucket_name, s3_filename, Body=html)
    simple_storage_service.Bucket(bucket_name).put_object(key=s3_filename, Body=problem)
