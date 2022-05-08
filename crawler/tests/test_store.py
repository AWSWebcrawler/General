# example test script
import crawler.store.store as st
import csv
import unittest
import os

""" Möglicher Test:
            - Anlegen eines Items
            - aufrufen der Methode mit Item und tmp-Datei (im tests ordner)
            - Einlesen der letzten Zeile der tmp-Datei
            - Assertion ob Werte aus Datei mit den Werten der Items übereinstimmen"""


class test_store(unittest.TestCase):
    def test_store_to_csv(self):
        sample_dict = {"name": "python", "version": 3.9}
        expected = "['header1', 'header2']['python', '3.9']"
        st.store_item(sample_dict)
        filename = 'test4'

        with open('..\\output\\' + filename + '.csv', newline='') as f:
            csvFile = csv.reader(f)
            complete = ''
            for line in csvFile:
                complete = str(complete) + str(line)

            f.close()
            os.remove('..\\output\\' + filename + '.csv')
            self.assertEqual(complete, expected, "The result and the expected value were not compliant. Please refer to the difference log in the run terminal")
