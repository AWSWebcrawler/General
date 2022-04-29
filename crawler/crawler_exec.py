"""Control of the program logic:
    - Reading the config files by calling the config_reader
    - Iterate over the defined scraping URLs in a loop
    - Call spider module to get HTML-text from the response
    - Call item_factory to extract individual tags
    - Calling the store module to save to csv file or S3 Bucket"""
import requests
import config_reader.config_reader as config_reader
from header_creater.create_header import generate_header

clients = config_reader.read_file('input/clients.yaml')
urls = config_reader.read_file('input/url.yaml')

for url in urls:
    for client in clients:
        header = generate_header(client)
        print(header)
