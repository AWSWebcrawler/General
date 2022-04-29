import yaml
from yaml import SafeLoader
"""The read_config method ist the one that should be called by the crawler main-script.
It returns a dictionary which contains the urls and the settings from the config Files."""



def read_config() -> dict:
    """Calling of the other methods"""
    config_dict = read_settings_file("./settings.yaml")
    config_dict["urls"] = read_url_list("./url.yaml")
    return config_dict


def read_settings_file(file_path:str) -> dict:
    """Reading a yaml file in which the configuration is made. storage in a dictionary.
    Returning the dictionary"""
    with open(file_path, 'r') as file:
        file_to_map = yaml.load(file, Loader=SafeLoader)
        return file_to_map


def read_url_list(file_path: str) -> list:
    """Reading a file in which the URLs to be scraped are listed.
    Store in a list and return that list"""
    with open(file_path, 'r') as file:
        file_to_map = yaml.load(file, Loader=SafeLoader)
        return file_to_map

