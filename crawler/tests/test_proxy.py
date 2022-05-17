from crawler.proxy.proxy import get_html
import requests

header_dict = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,"
              "*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
    "viewport-width": "1080",
    'Connection': 'keep-alive'}

# proxy = {
#     "http": "203.24.109.115:80",
#     "https" : "203.24.109.115:80"
#
# }
# proxy = {
#     "http": 'socks5h://72.217.216.239:4145',
#     "https": 'socks5h://72.217.216.239:4145'
# }

html_with_proxy = get_html("http://www.amazon.de/Garmin-Venu-GPS-Fitness-Smartwatch-AMOLED-Touchdisplay-Gesundheitsfunktionen/dp/B091ZXYQXF", header_dict, None)
print(html_with_proxy["html"])
print(html_with_proxy["proxy"])
html_with_proxy = get_html("http://www.amazon.de/Apple-iPhone-Pro-Max-128-GB/dp/B09G91T787", header_dict, html_with_proxy["proxy"])
print(html_with_proxy["html"])
print(html_with_proxy["proxy"])
# response = requests.get("https://www.amazon.de/Garmin-Venu-GPS-Fitness-Smartwatch-AMOLED-Touchdisplay-Gesundheitsfunktionen/dp/B091ZXYQXF", headers=header_dict, proxies=proxy, timeout=5, verify=False)
# print(response.text)
# print(response.status_code)
# print("Proxy:" + proxy["https"])
# print(response.headers)
