import csv
from os.path import exists

def store_item(product_dict, settings_dict):
    """Method receives an item to be stored. It uses environment variables to determine
    whether storage in AWS S3 bucket or local in csv file is required"""


    new_list = list(product_dict.values())
    print(new_list)
    filename = settings_dict["client"]
    store_to_csv(new_list, filename)

"""Method receives an item and a file name. It adds the attributes of the item in CSV format
     on a new line in the specified file. There is no return value."""
# def is_aws_env():
#     return os.environ.get('AWS_LAMBDA_FUNCTION_NAME') or os.environ.get('AWS_EXECUTION_ENV')
#
# def lambda_handler(event, context):
#     if is_aws_env():
#         store_to_S3('abc', 'abc')
#     else:
#         store_to_csv(item, filename)
#
#     if not is_aws_env():
#         lambda_handler({}, {})
def store_to_csv(item, filename):
    """Method receives an item and a file name. It adds the attributes of the item in CSV format
     on a new line in the specified file. There is no return value."""
    #somehow the filepath is directed from the crawler
    with open('.\\output\\' + filename + '.csv', 'a', newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        if file_exists:
            pass
        else:
            writer.writerow(["header1", "header2"])
        writer.writerow(item)
        f.close()


def store_to_S3(item, path_to_bucket):
    """Method gets an item and the path to an AWS S3 bucket. attributes of the item
     stored in the bucket in CSV format. There is no return value."""
    pass
