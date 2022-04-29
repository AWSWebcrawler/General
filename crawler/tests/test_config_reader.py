import yaml
from crawler.config_reader import config_reader
import os


def test_settings_reader():
    data = {"client": "safari"}
    file = open("test_settings.yaml", "w")
    yaml.dump(data, file)
    file.close()
    test_read = config_reader.read_settings_file("./test_settings.yaml")
    assert test_read["client"] == "safari", "Fehler in config_reader methode read_settings_file. Erwarteter Wert für " \
                                            "client ist safari. "
    os.remove("test_settings.yaml")

def test_url_reader():
    data = ["https://amazon.de", "https://tagesschau.de"]
    file = open("test_urls.yaml", "w")
    yaml.dump(data, file)
    file.close()
    test_read = config_reader.read_settings_file("./test_urls.yaml")
    assert test_read[1] == "https://tagesschau.de", "Fehler in config_reader methode read_url_list. Erwarteter Wert für " \
                                            "Liste an Index 1 ist https://tagesschau.de. "
    os.remove("test_urls.yaml")


test_settings_reader()
test_url_reader()