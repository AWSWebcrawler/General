"""The proxy module gets an url, a dictionary (and a proxy). It makes the request and validate the response. The
return value is a dictionary with the html, the used proxy and the required time. """

import logging
import random
import time
from typing import Iterator
import requests
from exceptions.proxy_exception import ProxyGotBlockedError
from exceptions.proxy_exception import ProxyListIsEmptyError
from exceptions.proxy_exception import SlowProxyError
from exceptions.proxy_exception import ProxyNotWorkingError


class ProxyService:
    """The Proxy Service has the proxy as Attributes. It`s initialized with a proxy_list and a current_proxy"""
    proxy_prefix_path = "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/" \
                        "94732c66982abfc273cfb41056efe7a062b78d01/proxies/"
    proxy_urls = {
        "socks4": f"{proxy_prefix_path}socks4.txt",
        "socks5": f"{proxy_prefix_path}socks5.txt",
        "http": f"{proxy_prefix_path}http.txt",
    }

    def __init__(self):
        self.proxy_list = _get_proxies(self.proxy_urls)
        self.current_proxy = self.proxy_list.pop()

    def get_html(self, url: str, header: dict) -> dict:
        """Calls the following methods."""
        while True:
            try:
                return _call_url(url, header, self.current_proxy)
            except (ProxyGotBlockedError, ProxyNotWorkingError, SlowProxyError) as error:
                logging.error(error)
                try:
                    self.current_proxy = self.proxy_list.pop()
                except IndexError:
                    raise ProxyListIsEmptyError


def _call_url(url: str, header: dict, current_proxy: str) -> dict:
    """Makes the request to the given url with the given header and proxy. Also checks if the response is valid."""

    time_for_request = time.time()
    try:
        response = requests.get(url, headers=header, proxies={"http": current_proxy}, timeout=3)
    except Exception:
        raise ProxyNotWorkingError("Proxy is not working: " + current_proxy)

    time_request_finished = time.time() - time_for_request
    if "(MEOW)" not in response.text:
        raise ProxyGotBlockedError("Proxy is blocked: " + current_proxy)
    if time_request_finished > 4.0:
        raise SlowProxyError("Proxy is too slow: " + current_proxy)
    if response.status_code == 200:
        return {
            'html': response.text,
            'proxy': current_proxy,
            'time': time_request_finished,
        }

    raise ProxyNotWorkingError("Proxy is not working: " + current_proxy)


def _get_proxies(proxy_urls: dict) -> list:
    """Creates a list with socks4, socks5 and http proxies"""
    logging.debug("Calling function get_proxies")

    get_proxy_iter: Iterator = lambda protocol: requests.get(proxy_urls[protocol]).iter_lines()

    socks4_proxies = [row.decode() for row in get_proxy_iter("socks4")]
    socks5_proxies = [row.decode() for row in get_proxy_iter("socks5")]
    http_proxies = [row.decode() for row in get_proxy_iter("http")]

    socks4_proxies = ["socks4://" + proxy for proxy in socks4_proxies]
    socks5_proxies = ["socks5h://" + proxy for proxy in socks5_proxies]

    proxy_list = http_proxies + socks4_proxies + socks5_proxies
    random.shuffle(proxy_list)

    return proxy_list
