from crawler.item_factory import item_factory

html= ""
with open('./html.txt', 'r') as file:
    html = file.read()

item = item_factory.create_item(html)
print(item)