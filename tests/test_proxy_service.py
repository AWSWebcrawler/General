"""Class to test the proxy_service module."""
import unittest
import time
import yaml
from yaml import SafeLoader
from proxy.proxy_service import ProxyService


class TestProxy(unittest.TestCase):
    """Test Class for proxy_service module"""

    def setUp(self):
        """Initializes the required variables for the test."""
        self.config = {
            "start_time": time.time(),
            "times": [],
            "average_time_for_request": 0.0,
            "max_time": 200,
            "time_for_completion": 0.0,
            "urls_with_problem": {},
            "test_header": {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/102.0.5005.61 Safari/537.36",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,"
                "*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
                "viewport-width": "1080",
                "Connection": "keep-alive",
            },
        }
        with open("../config/url.yaml", "r", encoding="utf-8") as file:
            self.url_list = yaml.load(file, Loader=SafeLoader)

    def test_proxy_module(self):
        """Tests the proxy_service module and checks if the time for completion is lower than 3 minutes and 20
        seconds"""
        proxy_service = ProxyService()

        for url in self.url_list:
            response = proxy_service.get_html(
                url, self.config["test_header"], self.config["urls_with_problem"]
            )
            if response is None:
                continue
            print("Successful request with proxy: " + response["proxy"])
            self.config["times"].append(response["time"])

        self.config["time_for_completion"] = time.time() - self.config["start_time"]

        for request_time in self.config["times"]:
            self.config["average_time_for_request"] += float(request_time)

        self.config["average_time_for_request"] = self.config[
            "average_time_for_request"
        ] / len(self.config["times"])
        print(
            "Average time for a request: "
            + str(self.config["average_time_for_request"])
        )
        print("Urls with problems: ")
        print(self.config["urls_with_problem"])
        self.assertLessEqual(
            self.config["time_for_completion"],
            self.config["max_time"],
            "The time for completion is greater than 3 " "minutes and 20 seconds!",
        )


if __name__ == "__main__":
    unittest.main()
