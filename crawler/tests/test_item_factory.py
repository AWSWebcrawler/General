from ..item_factory.item_factory import create_item

html= ""
with open('../item_factory/html.txt', 'r') as file:
    html = file.read()

item = create_item(html)
print(item)