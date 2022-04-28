from item_factory import create_item

html= ""
with open('html.txt', 'r') as file:
    html = file.read()

item = create_item(html)
print(item)