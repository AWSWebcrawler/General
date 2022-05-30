"""Stores the product as csv or in S3

    receives a product_dict with all values and the settings_dict
    with the wanted settings e.g. where to store"""

import csv
from os.path import exists
import logging
import boto3
from botocore.exceptions import ClientError


def store_item(product_dict: dict, settings_dict: dict) -> None:
    """Method receives an item to be stored. It uses environment variables to determine
    whether storage in AWS S3 bucket or local in csv file is required"""
    logging.debug("store_item_methode gestartet")
    if settings_dict["aws_env"]:
        logging.debug("store_to_s3 gestartet")
        store_to_s3(product_dict, settings_dict)
    else:
        filepath = "../output/" + settings_dict["client"] + ".csv"
        store_to_csv(product_dict, filepath)


def store_to_csv(product: dict, filepath: str):
    """Gets called by store_item with a dictionary containing product information
    and stores the product as a line in a csv file"""
    file_exists = exists(filepath)
    with open(filepath, 'a', encoding='utf-8', newline='') as file:
        # also need to configure the headers
        writer = csv.writer(file)
        header_list = ['timestamp',
                       'date',
                       'time',
                       'name',
                       'current_price',
                       'price_regular',
                       'prime',
                       'discount_in_euros',
                       'percent_discount',
                       'sold_by_amazon',
                       'seller',
                       'amazon_choice',
                       'asin',
                       'url']
        if file_exists:
            pass
        else:
            writer.writerow(header_list)

        write_values = []
        for header in header_list:
            value = product[header]
            if isinstance(value) == str:
                value = value.replace('"', '').replace("'", '')
                value.strip()
            write_values.append(value)
        writer.writerow(write_values)
        file.close()


def store_to_s3(product_dict: dict, settings_dict: dict) -> None:
    """Method gets an product dictionary and the name of the used client. Items from the product_dict are then
    stored in S3 in CSV format."""
    bucket_name = settings_dict["s3_bucket"]
    s3_filename = "%s_lambda.csv", settings_dict["client"]
    local_file = "/tmp/download.csv"
    s3 = boto3.resource("s3")
    logging.debug("writing to bucket %s with filename %s", bucket_name, s3_filename)
    headers = [
        "timestamp",
        "date",
        "time",
        "name",
        "current_price",
        "price_regular",
        "prime",
        "discount_in_euros",
        "percent_discount",
        "sold_by_amazon",
        "seller",
        "amazon_choice",
        "asin",
        "url",
    ]
    body = ""

    for item in headers:
        # body += str(product_dict[item]).replace(',', ' ')
        body += " ".join(str(product_dict[item]).split(","))
        if item != "url":
            body += ","
    body += "\n"

    try:
        s3.Bucket(bucket_name).download_file(s3_filename, local_file)
    except ClientError as ex:
        if ex.response["Error"]["Code"] == "404":
            print("The object does not exist.")
        else:
            raise
    with open(local_file, mode="a+", encoding="utf-8") as file:
        empty_test_char = file.read(1)
        if empty_test_char:
            column_names = ""
            for item in headers:
                column_names += item
                if item != "url":
                    column_names += ","
            column_names += "\n"
            file.write(column_names)
        file.write(body)

    s3.meta.client.upload_file(local_file, bucket_name, s3_filename)
