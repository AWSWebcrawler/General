"""This Modul stores the data in csv format.
It automatically detects whether it is running in an AWS enivornment or local and chooses the right store method."""
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
    with open(filepath, mode="a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        if file_exists:
            pass
        else:
            writer.writerow(
                [
                    "timestamp",
                    "date",
                    "time",
                    "name",
                    "current_price",
                    "price_regular",
                    "prime",
                    "discount_in_euros",
                    "percent discount",
                    "sold by amazon",
                    "seller",
                    "amazon_choice",
                    "asin",
                    "url",
                ]
            )
        writer.writerow(
            [
                product["timestamp"],
                product["date"],
                product["time"],
                product["name"].replace('"', "").replace("'", ""),
                product["current_price"],
                product["price_regular"],
                product["prime"],
                product["discount_in_euros"],
                product["percent_discount"],
                product["sold_by_amazon"],
                product["seller"],
                product["amazon_choice"],
                product["asin"],
                product["url"],
            ]
        )
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
