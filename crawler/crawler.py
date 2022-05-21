from spider.spider import executeRequest
from config.config_reader import read_config_files
from header.header_creater import generate_header
from item_factory.item_factory import create_item
from persistence import store
from datetime import date
import logging.config

"""Control of the program logic:
    - Reading the config files by calling the config
    - Iterate over the defined scraping URLs in a loop
    - Call spider module to get HTML-text from the response
    - Call item_factory to extract individual tags
    - Calling the persistence module to save item"""


def main():
    crawl('../config/url.yaml', '../config/settings.yaml')


def crawl(url_file, settings_file):
    # reading the url and settings file
    settings_dict = read_config_files(url_file, settings_file)

    #loggin not set up for testing
    if __name__ == "__main__":
        set_up_logging(settings_dict)

    # calling the spider
    header = generate_header(settings_dict)
    for url in settings_dict['urls']:
        response = executeRequest(url, header)
        # if the crawler is called from outside as module it returns the html string. This is used to test this script
        if __name__ != "__main__":
            return response
        product_dict = create_item(response, url)
        store.store_item(product_dict, settings_dict)



def set_up_logging(settings_dict):
    log_config = settings_dict["logconfig"]
    log_config['handlers']['file_handler']['filename'] = 'logging/' + str(date.today()) + '.logging'
    logging.config.dictConfig(log_config)


if __name__ == "__main__":
    main()
