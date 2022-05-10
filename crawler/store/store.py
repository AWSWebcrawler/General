import os
import csv
from os.path import exists


def store_item(product_dict, settings_dict):
    """Method receives an item to be stored. It uses environment variables to determine
    whether storage in AWS S3 bucket or local in csv file is required"""

    filename = settings_dict["client"]
    store_to_csv(product_dict, filename)


def store_to_csv(item, filename):
    """Gets called by store_item and stores the item as a csv file"""
    file_exists = exists('..\\output\\' + filename + '.csv')
    with open('..\\output\\' + filename + '.csv', 'a', encoding='utf-8', newline='') as f:
        # also need to configure the headers
        writer = csv.writer(f)
        if file_exists:
            pass
        else:
            writer.writerow(['timestamp', 'date', 'time', 'name', 'current_price', 'price_regular', 'prime',
                             'discount_in_euros', 'percent discount', 'sold by amazon', 'seller', 'amazon_choice',
                             'asin', 'url'])
        writer.writerow(
            [item['timestamp'], item['date'], item['time'], item['name'].replace('"', '').replace("'", ''),
             item['current_price'], item['price_regular'],
             item['prime'], item['discount_in_euros'], item['percent_discount'], item['sold_by_amazon'], item['seller']
                , item['amazon_choice'], item['asin'], item['url']])
        f.close()


def store_to_S3(item, path_to_bucket):
    """Method gets an item and the path to an AWS S3 bucket. attributes of the item
     stored in the bucket in CSV format. There is no return value."""
    pass
