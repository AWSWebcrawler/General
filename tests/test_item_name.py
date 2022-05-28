"""Class to test the item name."""
import unittest
from exceptions.item_factory_exception import LxmlTreeNotInitializedError
from crawler.item_factory import item_factory


class TestItemFactory(unittest.TestCase):
    """Test Class for item name"""

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
        expected = 'Echo Dot (4. Generation) | Smarter Lautsprecher mit Alexa | Anthrazit'
        self.assertEqual(expected, product["name"], "The created item name does not match the expected output.")

        product = item_factory.create_item(self.test_html_2, self.url2)
        expected = 'Xbox Wireless Controller Electric Volt'
        self.assertEqual(expected, product["name"], "The created item name does not match the expected output.")

        product = item_factory.create_item(self.test_html_3, self.url3)
        expected = '1152 Stück Anzündwürfel Paraffin (12 x 96 Würfel) vom deutschen Hersteller, Grillanzünder, Kami' \
                   'nanzünder, Ofenanzünder, Würfel, Anzündwolle, Made in Germany - 12 Schachteln x 96 Anzündwürfeln'
        self.assertEqual(expected, product["name"], "The created item name does not match the expected output.")
