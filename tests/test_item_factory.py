"""Class to test the item factory module."""
import unittest

from crawler.item_factory import item_factory


class TestItemFactory(unittest.TestCase):
    """Test Class for item factory module"""

    def setUp(self) -> None:
        self.urls = {
            "url1": "https://www.amazon.de/der-neue-echo-dot-4-generation-smarter-lautsprecher-mit-alexa-anthrazit/"
            "dp/B084DWG2VQ",
            "url2": "https://www.amazon.de/Xbox-Wireless-Controller-Electric-Volt/dp/B091CK241X",
            "url3": "https://www.amazon.de/FLAMMBURO-Paraffinbasis-Grillanz%C3%BCnder-Kaminanz%C3%BCnder-Paraffinw"
            "%C3%BCrfel/dp/B08YCWDLTQ",
            "url4": "https://www.amazon.de/CYBERPUNK-2077-DAY-Standard-Xbox/dp/B07SF1LZ9Q",
        }

        with open(
            "./test_item_factory_testfile1.html", "r", encoding="utf8"
        ) as file:
            test_html_1 = file.read()
        with open(
            "./test_item_factory_testfile2.html", "r", encoding="utf8"
        ) as file:
            test_html_2 = file.read()
        with open(
            "./test_item_factory_testfile3.html", "r", encoding="utf8"
        ) as file:
            test_html_3 = file.read()
        with open(
            "./test_item_factory_testfile4.html", "r", encoding="utf8"
        ) as file:
            test_html_4 = file.read()

        self.test_html = {
            "test_html_1": test_html_1,
            "test_html_2": test_html_2,
            "test_html_3": test_html_3,
            "test_html_4": test_html_4,
        }
        self.function_name_with_html = {}

    def test_create_item(self):
        """Tests the create item function of the item_factory module"""

        product = item_factory.create_item(
            self.test_html["test_html_1"],
            self.urls["url1"],
            self.function_name_with_html,
        )
        # the values for time and date are created dynamically so this is a problem for a test with a hardcoded string
        # as expected value, so i am setting it to None
        product["time"] = None
        product["date"] = None
        product["timestamp"] = None

        expected = {
            "name": "Echo Dot (4. Generation) | Smarter Lautsprecher mit Alexa | Anthrazit",
            "current_price": 29.18,
            "price_regular": 59.99,
            "prime": True,
            "discount_in_euros": 30.81,
            "percent_discount": 51.0,
            "sold_by_amazon": True,
            "seller": "Amazon",
            "brand": "Amazon",
            "shipping": None,
            "amazon_choice": True,
            "amazon_choice_for": "alexa",
            "asin": "B084DWG2VQ",
            "product_id": None,
            "manufacturer": None,
            "country_of_origin": None,
            "product_dimensions": "100 x 100 x 89 mm",
            "number_of_reviews": 165656,
            "review_score": "4.6",
            "on_sale_since": None,
            "url": "https://www.amazon.de/der-neue-echo-dot-4-generation-smarter-lautsprecher-mit-alexa-"
            "anthrazit/dp/B084DWG2VQ",
            "timestamp": None,
            "date": None,
            "time": None,
        }
        self.assertDictEqual(
            expected, product, "The created product does not match the expected output."
        )

        product = item_factory.create_item(
            self.test_html["test_html_2"],
            self.urls["url2"],
            self.function_name_with_html,
        )
        product["time"] = None
        product["date"] = None
        product["timestamp"] = None

        expected = {
            "name": "Xbox Wireless Controller Electric Volt",
            "current_price": 104.90,
            "price_regular": 104.90,
            "prime": True,
            "discount_in_euros": None,
            "percent_discount": None,
            "sold_by_amazon": False,
            "seller": "Trade-Unlimited",
            "brand": "Xbox",
            "shipping": None,
            "amazon_choice": False,
            "amazon_choice_for": None,
            "asin": "B091CK241X",
            "product_id": "QAU-00022",
            "manufacturer": None,
            "country_of_origin": "Deutschland",
            "product_dimensions": "17.8 x 7.3 x 17.7 cm",
            "number_of_reviews": 56549,
            "review_score": "4.6",
            "on_sale_since": None,
            "url": "https://www.amazon.de/Xbox-Wireless-Controller-Electric-Volt/dp/B091CK241X",
            "timestamp": None,
            "date": None,
            "time": None,
        }
        self.assertDictEqual(
            expected, product, "The created product does not match the expected output."
        )

        product = item_factory.create_item(
            self.test_html["test_html_3"],
            self.urls["url3"],
            self.function_name_with_html,
        )
        product["time"] = None
        product["date"] = None
        product["timestamp"] = None

        expected = {
            "name": "1152 Stück Anzündwürfel Paraffin (12 x 96 Würfel) vom deutschen Hersteller, Grillanzünder, Kami"
            "nanzünder, Ofenanzünder, Würfel, Anzündwolle, Made in Germany - 12 Schachteln x 96 Anzündwürfeln",
            "current_price": 24.99,
            "price_regular": 24.99,
            "prime": False,
            "discount_in_euros": None,
            "percent_discount": None,
            "sold_by_amazon": False,
            "seller": "Flammburo",
            "brand": "FLAMMBURO",
            "shipping": None,
            "amazon_choice": False,
            "amazon_choice_for": None,
            "asin": "B08YCWDLTQ",
            "product_id": "34097",
            "manufacturer": "FLAMMBURO",
            "country_of_origin": None,
            "product_dimensions": "28 x 20 x 27.5 cm",
            "number_of_reviews": 701,
            "review_score": "4.5",
            "on_sale_since": "31.3.2021",
            "url": "https://www.amazon.de/FLAMMBURO-Paraffinbasis-Grillanz%C3%BCnder-Kaminanz%C3%BCnder-"
            "Paraffinw%C3%BCrfel/dp/B08YCWDLTQ",
            "timestamp": None,
            "date": None,
            "time": None,
        }
        self.assertDictEqual(
            expected, product, "The created product does not match the expected output."
        )

        product = item_factory.create_item(
            self.test_html["test_html_4"],
            self.urls["url4"],
            self.function_name_with_html,
        )
        product["time"] = None
        product["date"] = None
        product["timestamp"] = None

        expected = {
            "name": "CYBERPUNK 2077 - DAY 1 Standard Edition - (kostenloses Upgrade auf Xbox Series X) - [Xbox One]",
            "current_price": 35.51,
            "price_regular": 35.51,
            "prime": False,
            "discount_in_euros": None,
            "percent_discount": None,
            "sold_by_amazon": False,
            "seller": "Cmal2_GmbH",
            "brand": "BANDAI NAMCO Entertainment Germany",
            "shipping": 5.0,
            "amazon_choice": False,
            "amazon_choice_for": None,
            "asin": "B07SF1LZ9Q",
            "product_id": "425978",
            "manufacturer": None,
            "country_of_origin": "Deutschland",
            "product_dimensions": "1.9 x 17.2 x 13.6 cm",
            "number_of_reviews": 1763,
            "review_score": "4.1",
            "on_sale_since": None,
            "url": "https://www.amazon.de/CYBERPUNK-2077-DAY-Standard-Xbox/dp/B07SF1LZ9Q",
            "timestamp": None,
            "date": None,
            "time": None,
        }
        self.assertDictEqual(
            expected, product, "The created product does not match the expected output."
        )
