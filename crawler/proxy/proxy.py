import logging
import requests
from lxml import etree
from io import StringIO

"""The proxy module gets an url and a dictionary for the headers and returns a functioning proxy"""


def get_proxy(url, header):
    """Calls the implemented functions and returns proxy"""

    logging.debug("Calling function get_proxy")

    list_of_proxies = get_proxies()
    proxy = get_working_proxy(list_of_proxies, url, header)
    return proxy


def get_proxies():
    """Creates a list of all proxies listed in the txt file of the proxy_url"""

    logging.debug("Calling function get_proxies")

    proxy_url = "https://github.com/saschazesiger/Free-Proxies/blob/94732c66982abfc273cfb41056efe7a062b78d01/proxies/ultrafast.txt"

    response = requests.get(proxy_url)

    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(response.text), parser)

    list_of_proxies = tree.findall('.//td[@class = "blob-code blob-code-inner js-file-line"]')
    list_of_proxies = [proxy.text for proxy in list_of_proxies]

    return list_of_proxies


def get_working_proxy(list_of_proxies, url, header):
    """Calls the test methode till a functional proxy is found or all proxies are tested"""

    logging.debug("Calling function get_working_proxy")

    count = 0
    proxy = None

    while count < len(list_of_proxies) and proxy is None:
        proxy = test_proxy(list_of_proxies, count, url, header)
        count += 1

    if proxy is not None:
        return proxy
    else:
        logging.error("No working proxy found")
        # raise no_working_proxy_found_Exception()


def test_proxy(list_of_proxies, count, url, header):
    """Tests the proxy with the given header and url"""

    logging.debug("Calling function test_proxy")

    proxy_domain = list_of_proxies[count]
    proxy = {
        "https": proxy_domain
    }

    try:
        logging.debug("Testing proxy:" + proxy["https"])
        # print("Testing proxy:" + proxy["https"])
        response = requests.get(url, headers=header, proxies=proxy, timeout=5)

        if response.status_code == 200:
            logging.debug("functioning proxy found")
            return proxy

    except:
        return None
