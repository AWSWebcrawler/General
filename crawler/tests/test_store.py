# example test script
import crawler.store.store as st
import csv


def test_store_to_csv():
    """ Möglicher Test:
        - Anlegen eines Items
        - aufrufen der Methode mit Item und tmp-Datei (im tests ordner)
        - Einlesen der letzten Zeile der tmp-Datei
        - Assertion ob Werte aus Datei mit den Werten der Items übereinstimmen"""
    sample_dict = {"name": "python", "version": 3.9}
    # sample_dict = {'name': '"Echo Dot (4. Generäääätion) | Smarter Lautsprecher mit Alexa" | Anthrazit', 'discount_in_euros': 29.99,
    #         'price_regular': 59.99, 'prime': False, 'sold_by_amazon': True, 'seller': 'amazon', 'asin': 'B084DWG2VQ',
    #         'url': 'https://www.amazon.de/der-neue-echo-dot-4-generation-smarter-lautsprecher-mit-alexa-anthrazit/dp/B084DWG2VQ',
    #         'timestamp': '1652119616.320101', 'date': '2022-05-09', 'time': '20:06:56', 'current_price': '12345', 'percent_discount':'45%', 'amazon_choice': False}
    # settings_dict = {'client':"linux"}
    st.store_item(sample_dict)
    filename = 'test4'

    with open('..\\output\\' + filename + '.csv', newline='') as f:
        csvFile = csv.reader(f)
        complete = ''
        for line in csvFile:
            complete = str(complete)+str(line)
            print(complete)

    f.close()
    #Need to append other rows/ lines if tested differently
    assert complete == "['1', '2', '3']['1', '2', '3']['1', '2', '3']['1', '2', '3']", 'Map of csv does not math with expected result'




test_store_to_csv()
