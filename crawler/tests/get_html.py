import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}

response = requests.get("https://www.amazon.de/dp/B084DWG2VQ?ref_=cm_sw_r_cp_ud_dp_93J9GCGXC997VW26Y0ES", headers=headers)
html = response.text
open("html.txt","w+")
with open("html.txt", "w", encoding="utf-8") as f:
    f.write(html)
