"""Test the write_to_csv method in store_scraper_data"""
import csv
import unittest
import os
from persistence.store_scraper_data import store_to_csv
from persistence.store_error_html import store_to_csv_html
from persistence.store_error_url import store_to_csv_error_url


class TestStore(unittest.TestCase):
    """Test the write_to_csv method in store_scraper_data"""

    def test_store_to_csv(self):
        """Tests the store_to_csv method of the persistence module.
        Stores given productinformation into a file
        and checks if the written data matches the excepted values"""
        sample_product_list = [
            {
                "name": '"Echo Dot (4. Generation) | '
                        'Smarter Lautsprecher mit Alexa" | Anthrazit',
                "discount_in_euros": 29.99,
                "price_regular": 59.99,
                "prime": False,
                "sold_by_amazon": True,
                "seller": "amazon",
                "asin": "B084DWG2VQ",
                "url": "https://www.amazon.de/der-neue-echo-dot-4-"
                       "generation-smarter-lautsprecher-mit-alexa-anthrazit"
                       "/dp/B084DWG2VQ",
                "timestamp": "1652119616.320101",
                "date": "2022-05-09",
                "time": "20:06:56",
                "current_price": "12345",
                "percent_discount": "45%",
                "amazon_choice": False,
                "brand": None,
                "shipping": None,
                "amazon_choice_for": None,
                "product_id": None,
                "manufacturer": None,
                "country_of_origin": None,
                "product_dimensions": None,
                "number_of_reviews": None,
                "review_score": None,
                "on_sale_since": None,
            }]
        header_list = [
            "timestamp",
            "date",
            "time",
            "name",
            "current_price",
            "price_regular",
            "prime",
            "discount_in_euros",
            "percent_discount",
            "sold_by_amazon",
            "seller",
            "brand",
            "shipping",
            "amazon_choice",
            "amazon_choice_for",
            "asin",
            "product_id",
            "manufacturer",
            "country_of_origin",
            "product_dimensions",
            "number_of_reviews",
            "review_score",
            "on_sale_since",
            "url",
        ]
        filepath = "testCSV.csv"
        store_to_csv(sample_product_list, filepath, header_list)
        last_line = ""
        with open(filepath, newline="", encoding="utf-8") as file:
            last_line = file.readlines()[-1]
            print(last_line)
        file.close()
        # removing the created file so there is no dead weight in the module directories
        os.remove(filepath)
        expected_string = ("1652119616.320101,2022-05-09,20:06:56,"
                           "Echo Dot (4. Generation) | Smarter Lautsprecher mit "
                           "Alexa | Anthrazit,12345,59.99,False,29.99,45%,"
                           "True,amazon,,,False,,B084DWG2VQ,"
                           ",,,,,,,"
                           "https://www.amazon.de/der-neue-echo-dot-4-"
                           "generation-smarter-lautsprecher-mit-alexa"
                           "-anthrazit/dp/B084DWG2VQ ")

        # Need to append other rows/ lines if tested differently
        self.assertEqual(
            expected_string.rstrip(),
            last_line.rstrip(),
            "The last line does not match with expected result",
        )

    def test_store_to_html(self):
        """tests the store html module"""
        test_list = ["<body><button>1 Tisch,,,, sauber</button></body>",
                     "<body><button>2 Tische sauber</button></body>",
                     "<body><button>3 Tische sauber</button></body>"]
        filepath = "../output/testHTML.csv"
        store_to_csv_html("testHTML", test_list)
        erg = ''

        with open(filepath, newline="", encoding="utf-8") as file:
            csv_file = csv.reader(file)
            for lines in csv_file:
                for line in lines:
                    erg += line.replace(",", '')
        os.remove(filepath)
        file.close()
        expected_string = "<body><button>1 Tisch sauber</button></body>" \
                          "<body><button>2 Tische sauber</button></body>" \
                          "<body><button>3 Tische sauber</button></body>"
        self.assertEqual(
            expected_string.rstrip(),
            erg.rstrip(),
            "The last line does not match with expected result",
        )

    def test_store_to_url(self):
        """tests the store url method"""
        error_dict_test = {"irgendein_text": "noch krasserer text",
                           "bananen": "bananen",
                           "irgendein_text132": "noch krasserer text"}
        test = {'noch krasserer text': ['irgendein_text', 'irgendein_text132'], 'bananen': ['bananen']}
        store_to_csv_error_url(error_dict_test)
        erg = ''
        for item in test:
            with open("../output/" + item + ".csv",
                      newline="", encoding="utf-8") as file:
                erg += file.readlines()[-1]
                print(erg)
            os.remove("../output/" + item + ".csv")
        file.close()

        expected_string = "irgendein_text,irgendein_text132,bananen,"
        self.assertEqual(
            expected_string.rstrip(),
            erg.rstrip(),
            "The last line does not match with expected result",
        )
