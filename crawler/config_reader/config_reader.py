import yaml
from yaml.loader import SafeLoader


def read_settings_file(file_path):
    """Einlesen eines yaml-Files in dem die Konfiguration vorgenommen wird. Speicherung in einem Dictionary.
    Rückgabe des Dictionary"""
    with open(file_path, 'r') as stream:
        yamlFile = yaml.load(stream, Loader=yaml.FullLoader)
    return yamlFile

def read_URL_list(file_path):
    """Einlesen eines Files in dem die zu scrapenden URLs aufgeführt sind.
    Speicherung in einer Liste und Rückgabe dieser Liste"""
    pass

#    how to do it
#     with open(file_path, 'r') as file:
#         file_to_map = yaml.load(file, Loader=SafeLoader)
#     return file_to_map
#

