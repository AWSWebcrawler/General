from src.crawler.header.header_creater import generate_header
import unittest

clients = [{'client': "android"}, {'client': "safari"}, {'client': "chrome_windows"}, {'client': "chrome_macintosh"},
           {'client': "firefox_windows"}, {'client': "firefox_macintosh"}, {'client': "linux"}]
expected = [{
           'user-agent': 'Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Mobile Safari/537.36',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'accept-encoding': 'gzip, deflate, br', 'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
           'viewport-width': '1080', 'Connection': 'keep-alive'},
       {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br', 'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
        'viewport-width': '1080', 'Connection': 'keep-alive'},
       {
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'accept-encoding': 'gzip, deflate, br', 'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
           'viewport-width': '1080', 'Connection': 'keep-alive'},
       {
           'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'accept-encoding': 'gzip, deflate, br', 'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
           'viewport-width': '1080', 'Connection': 'keep-alive'},
       {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br', 'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
        'viewport-width': '1080', 'Connection': 'keep-alive'},
       {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br', 'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
        'viewport-width': '1080', 'Connection': 'keep-alive'},
       {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.34 (KHTML, like Gecko) Qt/4.8.5 Safari/534.34',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br', 'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
        'viewport-width': '1080', 'Connection': 'keep-alive'},
       ]


class TestHeaders(unittest.TestCase):
    def test_android(self):
        for client, result in zip(clients, expected):
            self.assertEqual(generate_header(client), result, "The result and the expected value were not compliant. Please refer to the difference logging in the run terminal")
