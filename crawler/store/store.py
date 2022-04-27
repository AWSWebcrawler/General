def store_item(item):
    """Method receives an item to be stored. It uses environment variables to determine
    whether storage in AWS S3 bucket or local in csv file is required"""
    pass


def store_to_csv(item, filename):
    """Method receives an item and a file name. It adds the attributes of the item in CSV format
     on a new line in the specified file. There is no return value."""
    pass

def store_to_S3(item, path_to_bucket):
    """Method gets an item and the path to an AWS S3 bucket. attributes of the item
     stored in the bucket in CSV format. There is no return value."""
    pass