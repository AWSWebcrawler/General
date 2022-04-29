"""The item factory parses the passed html text and extracts the desired attributes. The attributes are then stored in a
dictionary and returned."""


def create_item(html):
    """The dictionary contains the attributes als name:value pairs. The value is generated by a method call. """
    dic = {
        "name": get_name(html),
        "price": get_price(html),
    }
    return dic


"""The individual methods receive the html text. Select the correct values using the appropriate html tags. 
Validate whether the values make any sense at all and, if necessary, 
transform the values to get the desired return value."""


def get_name(html):
    """select, validate and transform the name from the html"""
    pass


def get_price(html):
    """select, validate and transform the price from the html"""
    pass


