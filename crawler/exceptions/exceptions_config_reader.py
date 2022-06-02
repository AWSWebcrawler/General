
from crawler.exceptions.crawlerException import CrawlerError


class MalformedUrlError(CrawlerError):
    def __init__(self, message ="URL Fehler!"):
        super().__init__(message)
        print('URL Fehler!')
    pass


class EmptySettingsError(CrawlerError):
    def __init__(self, message ="Einstellungen leer!"):
        super().__init__(message)
        print('Einstellungen leer!')
    pass


class InvalidClientError(CrawlerError):
    def __init__(self, message ="Client Fehler!"):
        super().__init__(message)
        print('Client Fehler!')
    pass


class InvalidDatatypeError(CrawlerError):
    def __init__(self, message ="Dateityp Fehler!"):
        super().__init__(message)
        print('Dateityp Fehler!')
    pass


class AWSSettingsError(CrawlerError):
    def __init__(self, message ="AWS Fehler!"):
        super().__init__(message)
        print('AWS Fehler!')
    pass


class CouldNotWriteToFileError(CrawlerError):
    def __init__(self, message ="Konnte nicht in File schreiben!"):
        super().__init__(message)
        print('Konnte nicht in File schreiben!')
    pass

