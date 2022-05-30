"""The read_config method ist the one that should be called by the crawler main-script.
It returns a dictionary which contains the urls and the settings from the config Files."""
import os
import yaml
from yaml import SafeLoader
import validators
from crawler.exceptions.exceptions_config_reader import (
    EmptySettingsError,
    InvalidClientError,
    MalformedUrlError,
    AWSSettingsError,
)


def read_config_files(url_config_path, settings_config_path) -> dict:
    """Calling of the other methods"""
    config_dict = read_settings_file(settings_config_path)
    config_dict["aws_env"] = is_aws_environment()
    validate_settings(config_dict)

    urls = read_url_list(url_config_path)
    validate_urls(urls)
    config_dict["urls"] = urls

    return config_dict


def read_settings_file(file_path: str) -> dict:
    """Reading a yaml file in which the configuration is made. storage in a dictionary.
    Returning the dictionary"""
    with open(file_path, mode="r", encoding="utf-8") as file:
        file_to_map = yaml.load(file, Loader=SafeLoader)
        if file_to_map is None:
            raise EmptySettingsError(
                "The settings.yaml file is either empty or it is not "
                "compliant with the yaml file syntax"
            )
        return file_to_map


def is_aws_environment() -> bool:
    return bool(
        os.environ.get("AWS_LAMBDA_FUNCTION_NAME")
        or os.environ.get("AWS_EXECUTION_ENV")
    )


def validate_settings(settings: dict) -> None:
    """Validation of the settings dictionary.
    For the client setting, a comparison is made with the clients supported by the script."""
    validate_client_settings(settings)
    validate_aws_settings(settings)


def read_url_list(file_path: str) -> list:
    """Reading a file in which the URLs to be scraped are listed.
    Store in a list and return that list"""
    with open(file_path, mode="r", encoding="utf-8") as file:
        url_list = yaml.load(file, Loader=SafeLoader)
        return url_list


def validate_urls(urls: list) -> None:
    """Validation of URLs by using the validators external package.
    If an invalid URL is found the program terminates by throwing a MalformedUrlError"""
    for url in urls:
        valid = validators.url(url)
        if not valid:
            raise MalformedUrlError("URL " + url + " not valid.")


def validate_aws_settings(settings: dict) -> None:
    """Validates Settings in connection with AWS."""
    if not isinstance(settings["aws_env"], bool):
        raise AWSSettingsError(
            f'The Datatype of the aws_environment setting is not correct. Expected "bool" but '
            f'was {type(settings["client"])}'
        )

    if settings["aws_env"] and (
        not isinstance(settings["s3_bucket"], str) or settings["s3_bucket"] is None
    ):
        raise AWSSettingsError(
            "You are currently running in an AWS Environment but the name of your S3 Bucket is not set correctly. "
            "Please add it in the settings.yaml file like this. s3_bucket: <yourBucketName> "
        )


def validate_client_settings(settings: dict) -> None:
    """Validates the client settings"""
    supported_clients = [
        "safari",
        "iphone",
        "android",
        "chrome_windows",
        "chrome_macintosh",
        "firefox_windows",
        "firefox_macintosh",
        "linux",
    ]
    if settings["client"] is None:
        raise InvalidClientError(
            "The client is not set correctly in the settings.yaml file. Please add it like this. "
            "client: <clientName> Possible client names are safari, iphone, android, chrome_windows, "
            "chrome_macintosh, firefox_windows and firefox_macintosh"
        )

    if not isinstance(settings["client"] ,str):
        raise InvalidClientError(
            f'The Datatype of the client setting is not correct. Expected "str" but was {type(settings["client"])}'
        )

    if settings["client"] not in supported_clients:
        raise InvalidClientError(
            "The specified client: "
            + settings["client"]
            + " is not supported. Supported Clients are "
            + str(supported_clients)
        )

