from spider.spider import executeRequest
from config_reader.config_reader import read_config
from header_creater.header_creater import generate_header
from datetime import date
import logging.config

"""Control of the program logic:
    - Reading the config files by calling the config_reader
    - Iterate over the defined scraping URLs in a loop
    - Call spider module to get HTML-text from the response
    - Call item_factory to extract individual tags
    - Calling the store module to save item"""


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
    for url in settings_dict['urls']:
        response = executeRequest(url, header)
        # if the crawler is called from outside as module it returns the html string. This is used to test this script
        if __name__ != "__main__":
            return response
        print(response)



def set_up_logging(settings_dict):
    log_config = settings_dict["logconfig"]
    log_config['handlers']['file_handler']['filename'] = 'log/' + str(date.today()) + '.log'
    logging.config.dictConfig(log_config)


if __name__ == "__main__":
    main()
