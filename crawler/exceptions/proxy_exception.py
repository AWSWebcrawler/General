from crawler.exceptions.crawlerException import CrawlerError


class ProxyGotBlockedError(CrawlerError):
    def __init__(self, message ="Proxy geblockt!"):
        super().__init__(message)
        print('Proxy geblockt!')
    pass


class ProxyListIsEmptyError(CrawlerError):
    def __init__(self, message ="ProxyListe leer!"):
        super().__init__(message)
        print('ProxyListe leer!')
    pass


class SlowProxyError(CrawlerError):
    def __init__(self, message ="Geschwindigkeitsproblem Proxy!"):
        super().__init__(message)
        print('Geschwindigkeitsproblem Proxy!')
    pass


class ProxyNotWorkingError(CrawlerError):
    def __init__(self, message="Proxy funktioniert nicht!"):
        super().__init__(message)
        print('Proxy funktioniert nicht!')

    pass
