# pip installation guide
To install the required external packages you can either use the conda environment contained in the requirements.yaml File (attention there are different files for Windows and MacOS/Linux) or the following libraries can be installed directly with the package management program pip.

## validators
Used in the config_reader module to check if the urls are valid.

```pip install validators```

## PyYAML
Used in the config_reader module to read the settings and url file which are in the YAML format.

```pip install PyYAML```

## lxml
Used in the item_factory module to parse the html of a website and extract specific tags.

```pip install lxml```

## requests
Used in the proxy module to create a reqeust to a specific url.

```pip install requests```

## random-user-agent
Used in the header module to create a more random header for the request.

```pip install random-user-agent```