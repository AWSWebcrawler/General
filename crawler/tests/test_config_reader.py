import yaml
from crawler.config_reader import config_reader
import os
import unittest


class TestConfigReader(unittest.TestCase):

    def test_settings_reader(self):
        data = {"client": "safari"}
        file = open("test_settings.yaml", "w")
        yaml.dump(data, file)
        file.close()
        test_read = config_reader.read_settings_file("./test_settings.yaml")
        os.remove("test_settings.yaml")
        # assert test_read["client"] == "safari", "Error in config_reader method read_settings_file. Expected value for " \
        #                                         "client is safari. "
        self.assertEqual(test_read["client"], "safari",
                         "Error in config_reader method read_settings_file. Expected value for " \
                         "client is safari. ")

    def test_url_reader(self):
        data = ["https://amazon.de", "https://tagesschau.de"]
        file = open("test_urls.yaml", "w")
        yaml.dump(data, file)
        file.close()
        test_read = config_reader.read_settings_file("./test_urls.yaml")
        os.remove("test_urls.yaml")
        # assert test_read[
        #            1] == "https://tagesschau.de", "Error in config_reader method read_url_list. Expected value for " \
        #                                           "list at index 1 is https://tagesschau.de. "
        self.assertEqual(test_read[1], "https://tagesschau.de",
                         "Error in config_reader method read_url_list. Expected value for " \
                         "list at index 1 is https://tagesschau.de. ")

    def test_settings_reader_aws(self):
        test_read = config_reader.read_config('../input/url.yaml', '../input/settings.yaml')
        self.assertEqual(test_read["aws_env"], False,
                         "Error in config_reader method read_settings_file. Expected value for " \
                         "aws_env is not 'False'. ")
