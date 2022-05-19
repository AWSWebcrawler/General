import time
import yaml
from yaml import SafeLoader
from crawler.proxy.proxy import get_html


header_dict = {
    "user-agent": 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                  'Mobile/15E148',
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,"
              "*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
    "viewport-width": "1080",
    'Connection': 'keep-alive'}

with open('..\\input\\url.yaml', 'r', encoding="utf-8") as file:
    url_list = yaml.load(file, Loader=SafeLoader)

times = []
proxy = None
start_time = time.time()
for url in url_list:

    html_with_proxy = get_html(url, header_dict, proxy)
    print(html_with_proxy["proxy"])
    times.append(html_with_proxy["time"])
    proxy = html_with_proxy["proxy"]
    if float(html_with_proxy['time']) > 4.0:
        proxy = None

print(time.time() - start_time + " sec to complete")
average_time_for_request = 0.0
for time in times:
    average_time_for_request += float(time)
average_time_for_request = average_time_for_request/len(times)
print(average_time_for_request)
