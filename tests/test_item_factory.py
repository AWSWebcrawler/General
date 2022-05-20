from src.crawler.item_factory import item_factory

import unittest


class TestItemFactory(unittest.TestCase):
    def test_create_item(self):
        """Tests the create item function of the item_factory module"""
        # url von der die Testseite im test_item_factory_testfile.html stammt: "https://www.amazon.de/dp/B084DWG2VQ?ref_=cm_sw_r_cp_ud_dp_93J9GCGXC997VW26Y0ES
        url = "https://www.amazon.de/dp/B084DWG2VQ?ref_=cm_sw_r_cp_ud_dp_93J9GCGXC997VW26Y0ES"
        html = ""
        with open('test_item_factory_testfile.html', 'r', encoding='utf8') as file:
            html = file.read()

        product = item_factory.create_item(html, url)
        #the values for time and date are created dynamically so this is a problem for a test with a hardcoded string as expected value, so i am setting it to None
        product["time"] = None
        product["date"] = None
        product["timestamp"] = None

        expected = "{'name': 'Echo Dot (4. Generation) | Smarter Lautsprecher mit Alexa | Anthrazit', 'current_price': 59.99, 'price_regular': 59.99, 'prime': True, 'discount_in_euros': 0.0, 'percent_discount': 0.0, 'sold_by_amazon': True, 'seller': 'Amazon', 'amazon_choice': True, 'asin': 'B084DWG2VQ', 'url': 'https://www.amazon.de/dp/B084DWG2VQ?ref_=cm_sw_r_cp_ud_dp_93J9GCGXC997VW26Y0ES', 'timestamp': None, 'date': None, 'time': None}"
        self.assertEqual(expected, str(product), "The created product does not match the expected output.")
