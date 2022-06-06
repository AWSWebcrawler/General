"""Stores the error occuring during html data extraction
 and stores the error code and the HTML in a HTML file"""

import logging
from datetime import datetime as dt, timedelta, timezone
import boto3
from crawler.logging.decorator import decorator_for_logging


@decorator_for_logging
def store_error_url(error_dict: dict, settings_dict: dict) -> None:

    if settings_dict["aws_env"]:
        store_to_csv_error_url(error_dict)
    else:
        store_to_s3(error_dict, settings_dict)


@decorator_for_logging
def store_to_csv_error_url(error_dict: dict):
    for key in error_dict:
        with open("../output/"+key + ".csv", "w", encoding='utf-8') as file:
            file.write(error_dict[key])
        file.close()


@decorator_for_logging
def store_to_s3(error_dict: dict, settings_dict: dict) -> None:
    """
    Method gets an product dictionary and the name of the used client.
    Items from the product_dict are then
    stored in S3 in CSV format."""
    bucket_name = settings_dict["s3_bucket"]
    simple_storage_service = boto3.resource("s3")
    now = dt.now(timezone(timedelta(hours=2)))
    for key in error_dict:
        s3_filename = f"ErrorURL/" \
                  f"{str(now.year)}/" \
                  f"{str(now.month)}/" \
                  f"{str(now.day)}/" \
                  f"{str(now.hour)}/" \
                  f"{str(now.minute)}/" \
                  f"{key}.csv"

        logging.debug("writing to bucket %s with filename %s", bucket_name, s3_filename)
    # simple_storage_service.put_object(bucket_name, s3_filename, Body=html)
        simple_storage_service\
            .Bucket(bucket_name)\
            .put_object(key=s3_filename, Body=error_dict[key])
