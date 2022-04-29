import crawler.config_reader.config_reader as reader

clients = reader.read_file('/crawler/input/clients.yaml')

print(clients)