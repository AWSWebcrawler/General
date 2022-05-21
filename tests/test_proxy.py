"""Class to test the proxy module."""
import time
import yaml
from yaml import SafeLoader
from proxy.proxy import get_html


header_dict = {
    "user-agent": 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                  'Mobile/15E148',
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,"
              "*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
    "viewport-width": "1080",
    'Connection': 'keep-alive'}

with open('../crawler/input/url.yaml', 'r', encoding="utf-8") as file:
    url_list = yaml.load(file, Loader=SafeLoader)

times = []
PROXY = None
start_time = time.time()
for url in url_list:

    html_with_proxy = get_html(url, header_dict, PROXY)
    print(html_with_proxy["proxy"])
    times.append(html_with_proxy["time"])
    PROXY = html_with_proxy["proxy"]
    if float(html_with_proxy['time']) > 4.0:
        PROXY = None

print(time.time() - start_time + " sec to complete")
AVERAGE_TIME_FOR_REQUEST = 0.0
for time in times:
    AVERAGE_TIME_FOR_REQUEST += float(time)
AVERAGE_TIME_FOR_REQUEST = AVERAGE_TIME_FOR_REQUEST / len(times)
print(AVERAGE_TIME_FOR_REQUEST)
