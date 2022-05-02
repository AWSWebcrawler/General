import yaml
import os
from crawler.crawler import crawl

def test_crawler():
    #this website is a site for webscraper training shouldn't change that much over time
    url = ["https://webscraper.io/test-sites/e-commerce/allinone"]
    settings = {"client": "linux",
                "logconfig": {
                    "version": 1,
                    "root": {
                      "handlers": [
                        "console_handler",
                        "file_handler"
                      ],
                      "propagate": True,
                      "level": "DEBUG"
                    },
                    "formatters": {
                      "simple": {
                        "format": "%(asctime)s %(levelname)s:%(message)s"
                      },
                      "standard": {
                        "datefmt": "%m/%d/%Y|%I:%M:%S|%p",
                        "format": " %(asctime)s: (%(filename)s): %(levelname)s: %(funcName)s Line: %(lineno)d - %(message)s"
                      }
                    },
                    "disable_existing_loggers": True,
                    "handlers": {
                      "console_handler": {
                        "formatter": "simple",
                        "class": "logging.StreamHandler",
                        "level": "WARNING"
                      },
                      "file_handler": {
                        "class": "logging.FileHandler",
                        "formatter": "standard",
                        "mode": "a",
                        "level": "DEBUG",
                        "filename": "log/log.log"
                      }
                    }
                  }
                }

    url_file = open("testURL.yaml", "w")
    yaml.dump(url, url_file)
    url_file.close()

    settings_file = open("testsettings.yaml", "w")
    yaml.dump(settings, settings_file)
    settings_file.close()

    #start of the actual test
    html_response = crawl(r"testURL.yaml", r"testsettings.yaml")

    #the testcase_string does only contain the first 200 lines, because the rest of the test site changes all the time
    testcase_file = open("crawler_testcase.html", "r")
    testcase_string = testcase_file.read()
    testcase_file.close()

    assert html_response.startswith(testcase_string), "The test string and the data scraped by the crawler do not match."

    os.remove("testsettings.yaml")
    os.remove("testURL.yaml")


test_crawler()