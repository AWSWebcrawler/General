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
