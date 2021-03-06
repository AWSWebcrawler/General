"""Control of the program logic:
    - Reading the config files by calling the config
    - Iterate over the defined scraping URLs in a loop
    - Call spider module to get HTML-text from the response
    - Call item_factory to extract individual tags
    - Calling the persistence module to save item"""
import json
import sys
import time
from datetime import date
import logging.config
from crawler.proxy.proxy_service import ProxyService
from crawler.config.config_reader import read_config_files
from crawler.header.header_creater import generate_header
from crawler.item_factory.item_factory import create_item
from crawler.persistence.store import store_item
from crawler.exceptions.proxy_exception import ProxyListIsEmptyError


def main(event, context) -> None:
    """Lambda handler function for AWS"""
    crawl("/var/task/config/url.yaml", "/var/task/config/settings.yaml")
    return {
        "headers": {"Content-Type": "application/json"},
        "statusCode": 200,
        "body": json.dumps(
            {"message": "Lambda Container image invoked!", "event": event}
        ),
    }


def crawl(url_filepath: str, settings_filepath: str) -> None:
    """Central Method that controls the WebScraper logic."""

    start_time = time.time()

    settings_dict = read_config_files(url_filepath, settings_filepath)
    set_up_logging(settings_dict)

    proxy_service = ProxyService()
    for url in settings_dict["urls"]:
        try:
            header = generate_header(settings_dict)
            response = proxy_service.get_html(url, header)
            logging.info("Time for request with proxy " + response['proxy'] + ": " + str(response['time']))
        except ProxyListIsEmptyError:
            sys.exit(
                "No more proxies left in the proxy list. The program has been stopped!"
            )
        product_dict = create_item(response["html"], url)
        store_item(product_dict, settings_dict)

    logging.info("Total run time: " + str(time.time() - start_time))


def set_up_logging(settings_dict: dict) -> None:
    """Setting up the logging."""
    log_config = settings_dict["logconfig"]
    if __name__ == "__main__":
        log_config["handlers"]["file_handler"]["filename"] = (
            "log/" + str(date.today()) + ".log"
        )
    logging.config.dictConfig(log_config)


if __name__ == "__main__":
    crawl("../config/url.yaml", "../config/settings.yaml")
