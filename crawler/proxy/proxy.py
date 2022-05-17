import logging
import requests
from random import choice
"""The proxy module gets an url and a dictionary for the headers and returns a functioning proxy"""

PROXY_LIST = None
proxy_urls = {
    "socks4" : "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/94732c66982abfc273cfb41056efe7a062b78d01/proxies/socks4.txt",
    "socks5" : "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/94732c66982abfc273cfb41056efe7a062b78d01/proxies/socks5.txt",
    "http" : "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/94732c66982abfc273cfb41056efe7a062b78d01/proxies/http.txt"
}

def get_html(url, header, old_proxy) -> dict:

    if old_proxy is None:
        proxy = get_random_proxy()
        return call_url(url, header, proxy)

    return call_url(url, header, old_proxy)

def call_url(url, header, proxy) -> dict:
    try:
        response = requests.get(url, headers=header, proxies=proxy, timeout=3, verify=False)
        if(response.status_code == 200 and "(MEOW)" in response.text):
            html_with_proxy = {
                'html' : response.text,
                'proxy' : proxy
            }
            return html_with_proxy
        logging.error("Timeout")
    except:
        logging.error("Proxy not working")

    remove_proxy_from_list(proxy)
    return call_url(url, header, get_random_proxy())

def get_proxies():
    """Creates a list of all proxies listed in the txt file of the proxy_url"""

    global PROXY_LIST
    logging.debug("Calling function get_proxies")

    response_socks4 = requests.get(proxy_urls["socks4"])
    response_socks5 = requests.get(proxy_urls["socks5"])
    response_http = requests.get(proxy_urls["http"])

    socks4_proxies = [row.decode() for row in response_socks4.iter_lines()]
    socks5_proxies = [row.decode() for row in response_socks5.iter_lines()]
    http_proxies = [row.decode() for row in response_http.iter_lines()]

    socks4_proxies = ["socks4://"+proxy for proxy in socks4_proxies]
    socks5_proxies = ["socks5h://" + proxy for proxy in socks5_proxies]

    PROXY_LIST = http_proxies
    PROXY_LIST.extend(socks4_proxies)
    PROXY_LIST.extend(socks5_proxies)

def get_random_proxy() -> dict:
    """Tests the proxy with the given header and url"""

    logging.debug("Calling function test_proxy")

    if PROXY_LIST is None:
        get_proxies()

    proxy_ip = choice(PROXY_LIST)

    proxy = {
        "http": proxy_ip
    }
    print(proxy)
    return proxy

def remove_proxy_from_list(proxy):
    proxy = proxy['http']
    if PROXY_LIST is not None and proxy in PROXY_LIST:
        PROXY_LIST.remove(proxy)
        print(len(PROXY_LIST))