"""Steuerung der Ablauflogik:
    - Einlesen der Configdateien
    - In Schleife über die definierten Scraping URLs iterieren
    - Aufrufen des spider.py Scripts um HTML response zu erhalten
    - Aufrufen der item_factory um einzelne Tags zu extrahieren
    - Aufrufen des Store Moduls"""