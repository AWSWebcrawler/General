"""Stores the product as csv or in S3

    receives a product_dict with all values and the settings_dict
    with the wanted settings e.g. where to store"""

import csv
from os.path import exists


def store_item(product_dict, settings_dict):
    """Method receives an item to be stored. It uses environment variables to determine
    whether storage in AWS S3 bucket or local in csv file is required"""
    filepath = '../output/' + settings_dict["client"] + ".csv"
    store_to_csv(product_dict, filepath)


def store_to_csv(product, filepath):
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


def store_to_S3(item, path_to_bucket):
    """Method gets an item and the path to an AWS S3 bucket. attributes of the item
     stored in the bucket in CSV format. There is no return value."""
    pass
