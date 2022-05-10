from crawler.proxy.proxy import get_proxy
import requests

header_dict = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,"
              "*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
    "viewport-width": "1080",
    'Connection': 'keep-alive'}

# proxy = {
#     "https" : "147.75.88.40:80"
#     "https": "147.75.88.40:10001"
# }

proxy = get_proxy("https://www.amazon.de/Zertifiziert-general%C3%BCberholt-Display-HD-Bildschirm-Anthrazit/dp/B07SNPP6P3", header_dict)

response = requests.get("https://www.amazon.de/Zertifiziert-general%C3%BCberholt-Display-HD-Bildschirm-Anthrazit/dp/B07SNPP6P3", headers=header_dict, proxies=proxy)
print(response.text)
print(response.status_code)
print("Proxy:" + proxy["https"])
print(response.headers)
