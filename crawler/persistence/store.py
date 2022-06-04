"""Stores the product as csv or in S3

    receives a product_dict with all values and the settings_dict
    with the wanted settings e.g. where to store"""

import csv
from os.path import exists
import logging
import boto3


def store_items(product_output_list: list, settings_dict: dict) -> None:
    """Method receives an item to be stored. It uses environment variables to determine
    whether storage in AWS S3 bucket or local in csv file is required"""
    logging.debug("store_item_methode gestartet")
    if settings_dict["aws_env"]:
        logging.debug("store_to_s3 gestartet")
        store_to_s3(product_output_list, settings_dict)
    else:
        filepath = "../output/" + settings_dict["client"] + ".csv"
        store_to_csv(product_output_list, filepath)


def store_to_csv(product_output_list: list, filepath: str):
    """Gets called by store_item with a list of dictionaries containing
     product information
    and stores the product as a line in a csv file"""
    file_exists = exists(filepath)
    with open(filepath, "a", encoding="utf-8", newline="") as file:
        # also need to configure the headers
        writer = csv.writer(file)
        header_list = [
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
            "brand",
            "shipping",
            "amazon_choice",
            "amazon_choice_for",
            "asin",
            "product_id",
            "manufacturer",
            "country_of_origin",
            "product_dimensions",
            "number_of_reviews",
            "review_score",
            "on_sale_since",
            "url",
        ]
        if file_exists:
            pass
        else:
            writer.writerow(header_list)

        for product_dict in product_output_list:
            write_values = []
            for header in header_list:
                value = product_dict[header]
                if isinstance(value, str):
                    value = value.replace(",", "")
                    value = value.replace('"', "").replace("'", "")
                    value.strip()
                write_values.append(value)
            writer.writerow(write_values)
        file.close()


def store_to_s3(product_output_list: dict, settings_dict: dict) -> None:
    """Method gets a list of product dictionaries and the name of the used client.
    Items from the product_dict are then
    stored in S3 in CSV format."""
    bucket_name = settings_dict["s3_bucket"]
    s3_filename = "%s_bambi.csv", settings_dict["client"]
    simple_storage_service = boto3.resource("s3")
    logging.debug("writing to bucket %s with filename %s", bucket_name, s3_filename)
    header_list = [
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
        "brand",
        "shipping",
        "amazon_choice",
        "amazon_choice_for",
        "asin",
        "product_id",
        "manufacturer",
        "country_of_origin",
        "product_dimensions",
        "number_of_reviews",
        "review_score",
        "on_sale_since",
        "url",
    ]
    body = ""

    for item in header_list:
        body += item
        if item != header_list[-1]:
            body += ","
    body += "\n"

    for product_dict in product_output_list:
        for item in header_list:
            body += (
                str(product_dict[item])
                .replace(",", "")
                .replace('"', "")
                .replace("'", "")
            )
            if item != header_list[-1]:
                body += ","
        body += "\n"
    body = body.decode("utf-8", "ignore")
    simple_storage_service.put_object(bucket_name, s3_filename, Body=body)
