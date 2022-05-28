"""Class to test the item sold_by_amazon."""
import unittest
from exceptions.item_factory_exception import LxmlTreeNotInitializedError
from crawler.item_factory import item_factory


class TestItemFactory(unittest.TestCase):
    """Test Class for item sold_by_amazon"""

    def setUp(self) -> None:
        # url0 is just a dummy because we expect an error
        self.url0 = 'test_url'
        self.url1 = 'https://www.amazon.de/der-neue-echo-dot-4-generation-smarter-lautsprecher-mit-alexa-anthrazit/' \
                    'dp/B084DWG2VQ'
        self.url2 = 'https://www.amazon.de/Xbox-Wireless-Controller-Electric-Volt/dp/B091CK241X'
        self.url3 = 'https://www.amazon.de/FLAMMBURO-Paraffinbasis-Grillanz%C3%BCnder-Kaminanz%C3%BCnder-Paraffinw' \
                    '%C3%BCrfel/dp/B08YCWDLTQ'
        with open('./test_item_factory_testfile1.html', 'r', encoding='utf8') as file:
            self.test_html_1 = file.read()
        with open('./test_item_factory_testfile2.html', 'r', encoding='utf8') as file:
            self.test_html_2 = file.read()
        with open('./test_item_factory_testfile3.html', 'r', encoding='utf8') as file:
            self.test_html_3 = file.read()

    def test_create_item(self):
        """Tests the create item function of the item_factory module"""

        with self.assertRaises(LxmlTreeNotInitializedError):
            item_factory.create_item("", self.url0)

        product = item_factory.create_item(self.test_html_1, self.url1)
        self.assertTrue(product["sold_by_amazon"],
                        "The created item sold_by_amazon does not match the expected output.")

        product = item_factory.create_item(self.test_html_2, self.url2)
        self.assertFalse(product["sold_by_amazon"],
                         "The created item sold_by_amazon does not match the expected output.")

        product = item_factory.create_item(self.test_html_3, self.url3)
        self.assertFalse(product["sold_by_amazon"],
                         "The created item sold_by_amazon does not match the expected output.")
