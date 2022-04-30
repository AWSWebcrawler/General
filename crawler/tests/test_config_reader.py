import yaml
from crawler.config_reader import config_reader
import os


def test_settings_reader():
    data = {"client": "safari"}
    file = open("test_settings.yaml", "w")
    yaml.dump(data, file)
    file.close()
    test_read = config_reader.read_settings_file("./test_settings.yaml")
    assert test_read["client"] == "safari", "Error in config_reader method read_settings_file. Expected value for " \
                                            "client is safari. "
    os.remove("test_settings.yaml")


def test_url_reader():
    data = ["https://amazon.de", "https://tagesschau.de"]
    file = open("test_urls.yaml", "w")
    yaml.dump(data, file)
    file.close()
    test_read = config_reader.read_settings_file("./test_urls.yaml")
    assert test_read[1] == "https://tagesschau.de", "Error in config_reader method read_url_list. Expected value for " \
                                            "list at index 1 is https://tagesschau.de. "
    os.remove("test_urls.yaml")


test_settings_reader()
test_url_reader()