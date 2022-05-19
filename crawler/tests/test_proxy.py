import yaml
from yaml import SafeLoader

from crawler.proxy.proxy import get_html
import requests
import time

header_dict = {
    "user-agent": 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,"
              "*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
    "viewport-width": "1080",
    'Connection': 'keep-alive'}

with open('..\\input\\url.yaml', 'r') as file:
    url_list = yaml.load(file, Loader=SafeLoader)

# start_time = time.time()
# proxy = get_proxy()
# print("--- %s seconds ---" % (time.time() - start_time))
# print(proxy)
# for url in url_list:
#
#     try:
#         print(proxy)
#         start_time = time.time()
#         response = requests.get(url, headers=header_dict, proxies=proxy, timeout=2, verify=False)
#         print("--- %s seconds ---" % (time.time() - start_time))
#
#         if (response.status_code == 200 and "(MEOW)" in response.text):
#             print("Läuft mit proxy:" + proxy['http'])
#             if (time.time() - start_time) > 4:
#                 print("neuer Proxy, weil zu langsam")
#                 proxy = get_proxy()
#         else:
#             print("neuer Proxy, weil geblockt")
#             proxy = get_proxy()
#     except:
#         print("neuer Proxy, weil kaputt")
#         proxy = get_proxy()
#
# print("--- %s seconds ---" % (time.time() - start_time))

# proxy = {
#     "http": "203.24.109.115:80",
#     "https" : "203.24.109.115:80"
#
# }
# proxy = {
#     "http": 'socks5h://72.217.216.239:4145',
#     "https": 'socks5h://72.217.216.239:4145'
# }
times = []
proxy = None
start_time = time.time()
for url in url_list:



    html_with_proxy = get_html(url, header_dict, proxy)
    print(html_with_proxy["proxy"])
    times.append(html_with_proxy["time"])
    proxy = html_with_proxy["proxy"]
    if (float(html_with_proxy['time']) > 4.0):
        proxy = None

print("--- %s seconds for complete---" % (time.time() - start_time))
average_time_for_request = 0.0
for time in times:
    average_time_for_request += float(time)
average_time_for_request = average_time_for_request/len(times)
print(average_time_for_request)
# html_with_proxy = get_html("http://www.amazon.de/Garmin-Venu-GPS-Fitness-Smartwatch-AMOLED-Touchdisplay-Gesundheitsfunktionen/dp/B091ZXYQXF", header_dict, None)
# print(html_with_proxy["html"])
# print(html_with_proxy["proxy"])
# html_with_proxy = get_html("http://www.amazon.de/Apple-iPhone-Pro-Max-128-GB/dp/B09G91T787", header_dict, html_with_proxy["proxy"])
# print(html_with_proxy["html"])
# print(html_with_proxy["proxy"])
# response = requests.get("https://www.amazon.de/Garmin-Venu-GPS-Fitness-Smartwatch-AMOLED-Touchdisplay-Gesundheitsfunktionen/dp/B091ZXYQXF", headers=header_dict, proxies=proxy, timeout=5, verify=False)
# print(response.text)
# print(response.status_code)
# print("Proxy:" + proxy["https"])
# print(response.headers)
