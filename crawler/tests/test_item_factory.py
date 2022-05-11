from crawler.item_factory import item_factory

url="https://www.amazon.de/dp/B084DWG2VQ?ref_=cm_sw_r_cp_ud_dp_93J9GCGXC997VW26Y0ES"
html= ""
with open('./html.txt', 'r', encoding='utf8') as file:
    html = file.read()

item = item_factory.create_item(html,url)
print(item)