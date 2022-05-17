import csv
from os.path import exists


# TODO add path to file as parameter
def store_item(product_dict, settings_dict, path_to_store):
    """Method receives an item to be stored. It uses environment variables to determine
    whether storage in AWS S3 bucket or local in csv file is required"""
    filepath = ".\\output\\ " + settings_dict["client"] + ".csv"
    # TODO use f-strings
    filepath = f".\\output\\ {settings_dict['client']}.csv"
    _store_to_csv(product_dict, filepath)


def _store_to_csv(product, filepath):
    """Gets called by store_item with a dictionary containing product information
    and stores the product as a line in a csv file"""
    file_exists = exists(filepath)
    with open(filepath, mode="a", encoding="utf-8", newline="") as file:
        # also need to configure the headers
        writer = csv.writer(file)

        keys_in_order = ["timestamp","date","time","name","current_price","price_regular","prime","discount_in_euros","percent discount","sold by amazon","seller","amazon_choice","asin","url",]
        if not file_exists:
            writer.writerow(keys_in_order)
        # writer.writerow([product[key] for key in keys_in_order])
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


def _store_to_S3(item, path_to_bucket):
    """Method gets an item and the path to an AWS S3 bucket. attributes of the item
    stored in the bucket in CSV format. There is no return value."""
    pass
