"""Class to test the item current_price."""
import unittest

from crawler.item_factory import item_factory


class TestItemFactory(unittest.TestCase):
    """Test Class for item current_price"""

    def setUp(self) -> None:
        self.urls = {
            'url1': 'https://www.amazon.de/der-neue-echo-dot-4-generation-smarter-lautsprecher-mit-alexa-anthrazit/' \
                    'dp/B084DWG2VQ',
            'url2': 'https://www.amazon.de/Xbox-Wireless-Controller-Electric-Volt/dp/B091CK241X',
            'url3': 'https://www.amazon.de/FLAMMBURO-Paraffinbasis-Grillanz%C3%BCnder-Kaminanz%C3%BCnder-Paraffinw' \
                    '%C3%BCrfel/dp/B08YCWDLTQ',
            'url4': 'https://www.amazon.de/CYBERPUNK-2077-DAY-Standard-Xbox/dp/B07SF1LZ9Q',
        }

        with open('./test_item_factory_testfile1.html', 'r', encoding='utf8') as file:
            test_html_1 = file.read()
        with open('./test_item_factory_testfile2.html', 'r', encoding='utf8') as file:
            test_html_2 = file.read()
        with open('./test_item_factory_testfile3.html', 'r', encoding='utf8') as file:
            test_html_3 = file.read()
        with open('./test_item_factory_testfile4.html', 'r', encoding='utf8') as file:
            test_html_4 = file.read()

        self.test_html = {
            'test_html_1': test_html_1,
            'test_html_2': test_html_2,
            'test_html_3': test_html_3,
            'test_html_4': test_html_4,
        }

    def test_create_item(self):
        """Tests the create item function of the item_factory module"""

        product = item_factory.create_item(self.test_html['test_html_1'], self.urls['url1'])
        expected = 29.18
        self.assertEqual(expected, product["current_price"],
                         "The created item price_regular does not match the expected output.")

        product = item_factory.create_item(self.test_html['test_html_2'], self.urls['url2'])
        expected = 104.90
        self.assertEqual(expected, product["current_price"],
                         "The created item current_price does not match the expected output.")

        product = item_factory.create_item(self.test_html['test_html_3'], self.urls['url3'])
        expected = 24.99
        self.assertEqual(expected, product["current_price"],
                         "The created item current_price does not match the expected output.")

        product = item_factory.create_item(self.test_html['test_html_4'], self.urls['url4'])
        expected = 35.51
        self.assertEqual(expected, product["current_price"],
                         "The created item current_price does not match the expected output.")
