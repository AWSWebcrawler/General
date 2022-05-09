import yaml

from yaml import SafeLoader
import validators
import os

from exceptions import exceptions_config_reader

"""The read_config method ist the one that should be called by the crawler main-script.
It returns a dictionary which contains the urls and the settings from the config Files."""


def read_config(url_file, settings_file) -> dict:
    """Calling of the other methods"""
    # reading and validating the settings
    config_dict = read_settings_file(settings_file)
    validate_settings(config_dict)
    # reading and validating the urls
    urls = read_url_list(url_file)
    validate_urls(urls)
    # saving urls into the config_dict
    config_dict["urls"] = urls

    if os.environ.get('AWS_LAMBDA_FUNCTION_NAME') or os.environ.get('AWS_EXECUTION_ENV'):
        aws_env = True
    else:
        aws_env = False
    config_dict['aws_env'] = aws_env
    return config_dict


def read_settings_file(file_path: str) -> dict:
    """Reading a yaml file in which the configuration is made. storage in a dictionary.
    Returning the dictionary"""
    with open(file_path, 'r') as file:
        file_to_map = yaml.load(file, Loader=SafeLoader)
        if file_to_map is None:
            raise exceptions_config_reader.EmptySettingsError("The settings.yaml file is either empty or it is not "
                                                              "compliant with the yaml file syntax")
        return file_to_map


def validate_settings(settings: dict):
    """Validation of the settings dictionary.
    For the client setting, a comparison is made with the clients supported by the script."""
    supported_clients = ["safari",
                         "iphone",
                         "android",
                         "chrome_windows",
                         "chrome_macintosh",
                         "firefox_windows",
                         "firefox_macintosh",
                         "linux"]
    if settings["client"] not in supported_clients:
        raise exceptions_config_reader.InvalidClientError("The specified client: "
                                                          + settings["client"]
                                                          + " is not supported. Supported Clients are "
                                                          + str(supported_clients))


def read_url_list(file_path: str) -> list:
    """Reading a file in which the URLs to be scraped are listed.
    Store in a list and return that list"""
    with open(file_path, 'r') as file:
        url_list = yaml.load(file, Loader=SafeLoader)
        return url_list


def validate_urls(urls: list):
    """Validation of URLs by using the validators external package.
    If an invalid URL is found the program terminates by throwing a MalformedUrlError"""
    for url in urls:
        valid = validators.url(url)
        if not valid:
            raise exceptions_config_reader.MalformedUrlError("URL " + url + " not valid.")


