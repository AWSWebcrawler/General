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
from threading import Thread

from crawler.proxy.proxy_service import ProxyService
from crawler.config.config_reader import read_config_files
from crawler.header.header_creater import generate_header
from crawler.item_factory.item_factory import create_item
from crawler.persistence.store_scraper_data import store_item
from crawler.exceptions.proxy_exception import ProxyListIsEmptyError
from crawler.persistence.store_error_url import store_error_url
from crawler.persistence.store_error_html import store_error_html


def main(event, context) -> None:
    """Lambda handler function for AWS"""
    aws_client_info = str(event["client"])
    crawl("/var/task/config/url.yaml", "/var/task/config/settings.yaml", aws_client_info=aws_client_info)
    return {
        "headers": {"Content-Type": "application/json"},
        "statusCode": 200,
        "body": json.dumps(
            {"message": "Lambda Container image invoked!", "event": event}
        ),
    }


def crawl(url_filepath: str, settings_filepath: str, aws_client_info=None) -> None:
    """Central Method that controls the WebScraper logic."""

    start_time = time.time()

    settings_dict = read_config_files(url_filepath, settings_filepath, aws_client_info)
    set_up_logging(settings_dict)

    proxy_service = ProxyService()
    urls = settings_dict["urls"]
    product_output_list = []
    urls_with_problem = {}
    function_name_with_html = {}

    threads = []
    for n in range(1, 5):
        crawler_thread = Thread(
            target=proxy_threading,
            args=(urls, proxy_service, settings_dict, product_output_list, urls_with_problem, function_name_with_html),
        )
        threads.append(crawler_thread)
        crawler_thread.start()
    for crawler_thread in threads:
        crawler_thread.join()

    store_item(product_output_list, settings_dict)
    logging.info("Total run time: " + str(time.time() - start_time))


def set_up_logging(settings_dict: dict) -> None:
    """Setting up the logging."""
    log_config = settings_dict["logconfig"]
    if __name__ == "__main__":
        log_config["handlers"]["file_handler"]["filename"] = (
            "log/" + str(date.today()) + ".log"
        )
    logging.config.dictConfig(log_config)


def proxy_threading(
    urls: list,
    proxy_service: ProxyService,
    settings_dict: dict,
    product_output_list: list,
    urls_with_problem: dict,
    html_with_error: dict
):

    """Threading method"""
    while urls:
        url = urls.pop()
        try:
            header = generate_header(settings_dict)
            response = proxy_service.get_html(url, header, urls_with_problem)
            if response is None:
                continue
            logging.info(
                "Time for request with proxy "
                + response["proxy"]
                + ": "
                + str(response["time"])
            )
        except ProxyListIsEmptyError:
            sys.exit(
                "No more proxies left in the proxy list. The program has been stopped!"
            )
        product_dict = create_item(response["html"], url, html_with_error)
        product_output_list.append(product_dict)

    store_error_url(urls_with_problem, settings_dict)
    store_error_html(html_with_error, settings_dict)


if __name__ == "__main__":
    crawl("../config/url.yaml", "../config/settings.yaml")
