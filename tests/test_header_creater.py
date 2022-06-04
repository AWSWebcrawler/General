"""tests the header_creater module"""

import unittest
from header.header_creater import generate_header
from user_agents import parse


clients = [{'client': "android"},
           {'client': "iphone"},
           {'client': "chrome_windows"},
           {'client': "chrome_macintosh"},
           {'client': "firefox_windows"},
           {'client': "firefox_macintosh"},
           {'client': "linux"}]
translate = {'iOS': 'iphone',
             'Android': 'android',
             'Chrome_Windows': "chrome_windows",
             'Chrome_Mac OS X': 'chrome_macintosh',
             'Firefox_Windows': 'firefox_windows',
             'Firefox_Mac OS X': 'firefox_macintosh',
             'Linux': 'linux',
             'Ubuntu': 'linux'}


class TestUserAgent(unittest.TestCase):
    def test_android(self):
        for client in clients:
            user_agent = generate_header(client)['user-agent']
            ua_string = parse(user_agent)
            os_family = ua_string.os.family
            erg = os_family
            if '_' in client['client']:
                browser_family = ua_string.browser.family
                erg = browser_family.replace('Mobile Version', '') + '_' + os_family
            self.assertEqual(client.get('client'), translate[erg],
                             "The result and the expected value were not compliant. "
                             "Please refer to the difference logging in the run terminal")