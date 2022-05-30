"""Generates a header for the subsequent web request based on the settings dictionary.
Returns the header information as a dictionary."""

import random
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem, SoftwareEngine


def generate_header(settings) -> dict:
    """Generates Header based on the chosen setting for the request"""
    check_client = settings['client']
    software = 'chrome'
    if '_' in check_client:
        all = settings['client']
        index = all.index('_')
        software = all[:index]
        device = all[index+1:]
    else:
        device = check_client
        if device == 'iphone':
            software = 'safari'
        else:
            software = 'chrome'
    user_agent = get_user_agent(device, software)
    header_dict = {"user-agent": user_agent,
                   "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
                             "image/avif,image/webp,image/apng,"
                             "*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                   "accept-encoding": "gzip, deflate, br",
                   "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
                   "viewport-width": "1080",
                   'Connection': 'keep-alive'}
    return header_dict


def get_user_agent(device, software):
    """Get random User Agent based on the given Client and browser
    (chrome is default if nothing else is given)"""
    device_dict = {
        'windows': OperatingSystem.WINDOWS.value,
        'linux':OperatingSystem.LINUX.value,
        'iphone': OperatingSystem.IOS.value,
        'android':OperatingSystem.ANDROID.value,
        'macintosh': OperatingSystem.MAC_OS_X.value
    }
    software_dict = {
        'chrome': SoftwareName.CHROME.value,
        'firefox':SoftwareName.FIREFOX.value,
        'safari': SoftwareName.SAFARI.value
    }
    software_engine_dict = [SoftwareEngine.GECKO, SoftwareEngine.KHTML]
    software_names = software_dict[software]
    operating_systems = device_dict[device]
    user_agent_rotator = UserAgent(
        software_names=software_names,
        operating_systems=operating_systems,
        software_engine=random.choice(software_engine_dict),
        limit=100)

    user_agent = user_agent_rotator.get_random_user_agent()
    print(user_agent)
    return user_agent

