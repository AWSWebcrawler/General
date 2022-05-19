"""Control of the program logic:
    - Reading the config files by calling the config_reader
    - Iterate over the defined scraping URLs in a loop
    - Call spider module to get HTML-text from the response
    - Call item_factory to extract individual tags
    - Calling the store module to save item"""

from datetime import date
import logging.config
from proxy.proxy import get_html
from config_reader.config_reader import read_config
from header_creater.create_header import generate_header
from item_factory.item_factory import create_item
from store import store

def main():
    crawl('.\\input\\url.yaml', '.\\input\\settings.yaml')


def crawl(url_file, settings_file):
    # reading the url and settings file
    settings_dict = read_config(url_file, settings_file)

    #loggin not set up for testing
    if __name__ == "__main__":
        set_up_logging(settings_dict)

    # calling the spider
    header = generate_header(settings_dict)
    proxy = None
    for url in settings_dict['urls']:
        response = get_html(url, header, proxy)
        proxy = response['proxy']
        if float(response['time']) > 3.0:
            proxy = None
        # if the crawler is called from outside as module it returns the html string. This is used to test this script
        if __name__ != "__main__":
            return response
        product_dict = create_item(response['html'], url)
        store.store_item(product_dict, settings_dict)



def set_up_logging(settings_dict):
    log_config = settings_dict["logconfig"]
    log_config['handlers']['file_handler']['filename'] = 'log/' + str(date.today()) + '.log'
    logging.config.dictConfig(log_config)


if __name__ == "__main__":
    main()
