from config_reader import config_reader
import logging.config
from header_creater.create_header import generate_header
from datetime import date

"""Control of the program logic:
    - Reading the config files by calling the config_reader
    - Iterate over the defined scraping URLs in a loop
    - Call spider module to get HTML-text from the response
    - Call item_factory to extract individual tags
    - Calling the store module to save to csv file or S3 Bucket"""
# If matthias is nice to us, we can activate this code ;)
# yamlFile = config_reader.read_settings_file('./input/settings.yaml')
# config = yamlFile["logconfig"]
# config['handlers']['file_handler']['filename'] = 'log/'+str(date.today())+'.log'
# logging.config.dictConfig(config)
