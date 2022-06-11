"""Stores the error occuring during html data extraction
 and stores the error code and the HTML in a HTML file"""

import logging
from datetime import datetime as dt, timedelta, timezone
import boto3
from crawler.logging.decorator import decorator_for_logging


@decorator_for_logging
def store_error_url(error_dict: dict, settings_dict: dict) -> None:
    if settings_dict["aws_env"]:
        store_to_s3(error_dict, settings_dict)
    else:
        store_to_csv_error_url(error_dict)


@decorator_for_logging
def store_to_csv_error_url(error_dict: dict) -> None:
    """Store to local machine"""
    refactored_dict = {}
    for key, value in error_dict.items():
        if value in refactored_dict:
            refactored_dict[value].append(key)
        else:
            refactored_dict[value] = [key]
    for key in refactored_dict:
        body = ''
        for val in refactored_dict[key]:
            body += val
            body += ','

        with open("../output/" + key + ".csv", "a", encoding='utf-8') as file:
            key += ','
            file.writelines(body)
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
    refactored_dict = {}
    for key, value in error_dict.items():
        if value in refactored_dict:
            refactored_dict[value].append(key)
        else:
            refactored_dict[value] = [key]
    for key in refactored_dict:
        s3_filename = f"ErrorURL/" \
                      f"{str(now.year)}/" \
                      f"{str(now.month)}/" \
                      f"{str(now.day)}/" \
                      f"{str(now.hour)}/" \
                      f"{str(now.minute)}/" \
                      f"{key}_{settings_dict['client']}.csv"
        body = ''
        for val in refactored_dict[key]:
            body += val
            body += ','

        logging.debug("writing to bucket %s with filename %s", bucket_name, s3_filename)
        # simple_storage_service.put_object(bucket_name, s3_filename, Body=html)
        simple_storage_service \
            .Bucket(bucket_name) \
            .put_object(key=s3_filename, Body=body)
