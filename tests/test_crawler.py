"""Test for the crawler."""
import os
import unittest
import yaml
from crawler import main


class TestCrawler(unittest.TestCase):
    """Test for the crawler"""

    def test_crawler_html(self):
        """Test for the crawler"""
        url = [
            "https://www.amazon.de/ATG-Schutzhandschuhe-MaxiFlex-Ultimate-Gr%C3%B6%C3%9Fe/dp/B07B8P7CP1"
        ]
        settings = {
            "client": "linux",
            "logconfig": {
                "version": 1,
                "root": {
                    "handlers": ["console_handler"],
                    "propagate": True,
                    "level": "DEBUG",
                },
                "formatters": {
                    "simple": {"format": "%(asctime)s %(levelname)s:%(message)s"},
                    "standard": {
                        "datefmt": "%m/%d/%Y|%I:%M:%S|%p",
                        "format": " %(asctime)s: (%(filename)s): %(levelname)s: %(funcName)s Line: %(lineno)d - %(message)s",
                    },
                },
                "disable_existing_loggers": True,
                "handlers": {
                    "console_handler": {
                        "formatter": "simple",
                        "class": "logging.StreamHandler",
                        "level": "WARNING",
                    },
                },
            },
        }

        with open("testURL.yaml", mode="w", encoding="utf-8") as url_file:
            yaml.dump(url, url_file)

        with open("testsettings.yaml", mode="w", encoding="utf-8") as settings_file:
            yaml.dump(settings, settings_file)

        # start of the actual test

        main.crawl("testURL.yaml", "testsettings.yaml")
        os.remove("testsettings.yaml")
        os.remove("testURL.yaml")

        last_line_dict = {}
        with open("../output/linux.csv", mode="r", encoding="utf-8") as output_file:
            last_line_dict = output_file.readlines()[-1].split(",")
        expected_name = "ATG Schutzhandschuh Maxiflex®Ultimate 34-874 Größe 9 schwarz EN388 Kategorie II Inhalt: 5 Paar"
        expected_asin = "B07B8P7CP1"
        self.assertEqual(expected_name, last_line_dict[3], "Wrong value for name.")
        self.assertEqual(expected_asin, last_line_dict[15], "Wrong value for asin")
