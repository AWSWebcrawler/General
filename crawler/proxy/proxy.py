"""The proxy module gets an url, a dictionary (and a proxy). It makes the request and validate the response. The
return value is a dictionary with the html, the used proxy and the required time. """

import logging
from random import choice
import time
import requests

proxy_list = None
proxy_urls = {
    "socks4": "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/94732c66982abfc273cfb41056efe7a062b78d01"
              "/proxies/socks4.txt",
    "socks5": "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/94732c66982abfc273cfb41056efe7a062b78d01"
              "/proxies/socks5.txt",
    "http": "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/94732c66982abfc273cfb41056efe7a062b78d01"
            "/proxies/http.txt "
}


def get_html(url, header, old_proxy) -> dict:
    """Calls the following methods."""

    if old_proxy is None:
        proxy = get_random_proxy()
        return call_url(url, header, proxy)

    return call_url(url, header, old_proxy)


def call_url(url, header, proxy) -> dict:
    """Makes the request to the given url with the given header and proxy. Also checks if the response is valid."""

    try:
        time_for_request = time.time()
        response = requests.get(url, headers=header, proxies=proxy, timeout=3, verify=False)
        time_request_finished = time.time() - time_for_request
        if response.status_code == 200 and "(MEOW)" in response.text:
            html_with_proxy = {
                'html': response.text,
                'proxy': proxy,
                'time': time_request_finished
            }
            return html_with_proxy

        logging.error("Timeout")

    except:
        logging.error("Proxy not working")

    remove_proxy_from_list(proxy)
    return call_url(url, header, get_random_proxy())


def get_proxies():
    """Creates a list with socks4, socks5 and http proxies"""
    logging.debug("Calling function get_proxies")

    response_socks4 = requests.get(proxy_urls["socks4"])
    response_socks5 = requests.get(proxy_urls["socks5"])
    response_http = requests.get(proxy_urls["http"])

    socks4_proxies = [row.decode() for row in response_socks4.iter_lines()]
    socks5_proxies = [row.decode() for row in response_socks5.iter_lines()]
    http_proxies = [row.decode() for row in response_http.iter_lines()]

    socks4_proxies = ["socks4://" + proxy for proxy in socks4_proxies]
    socks5_proxies = ["socks5h://" + proxy for proxy in socks5_proxies]

    global proxy_list
    proxy_list = http_proxies
    proxy_list.extend(socks4_proxies)
    proxy_list.extend(socks5_proxies)


def get_random_proxy() -> dict:
    """Checks if proxy_list is already filled. Then returns a random proxy of proxy_list"""

    logging.debug("Calling function test_proxy")

    if proxy_list is None:
        get_proxies()

    proxy_ip = choice(proxy_list)

    proxy = {
        "http": proxy_ip
    }
    return proxy


def remove_proxy_from_list(proxy):
    """Removes the given proxy from proxy_list"""
    proxy = proxy['http']
    if proxy_list is not None and proxy in proxy_list:
        proxy_list.remove(proxy)
