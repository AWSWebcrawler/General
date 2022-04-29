import yaml
from yaml.loader import SafeLoader


def read_file(file_path):
    """Einlesen eines yaml-Files in dem die Konfiguration vorgenommen wird. Speicherung in einem Dictionary.
    Rückgabe des Dictionary"""
    with open(file_path, 'r') as file:
        file_to_map = yaml.load(file, Loader=SafeLoader)
    return file_to_map


def read_settings_file(file_path):
    pass

