"""Generates a header for the subsequent web request based on the settings dictionary.
Returns the header information as a dictionary."""
#import crawler.header_creater.user_agent_creator as user_agent_creator
from crawler.header_creater.user_agent_creator import get_user_agent


def generate_header(client) -> dict:
    user_agent = get_user_agent(client)
    header_dict = {"user-agent": user_agent,
                   "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,"
                             "*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                   "accept-encoding": "gzip, deflate, br",
                   "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
                   "viewport-width": "1080"}
    # header = {"user-agent: " + user_agent +" Accept: text/html,application/xhtml+xml,application/xml;q=0.9,
    # */*;q=0.8; " + " Accept-Language: de,en-US;q=0.7,en;q=0.3" + " Accept-Encoding: gzip, deflate,
    # br" + " Content-Type": "application/json; " + " charset=utf-8;" } data = {'key': 'value'}
    return header_dict

