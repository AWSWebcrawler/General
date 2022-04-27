import requests

def executeRequest(url, header):
    """Methode erhält eine URL und einen header_creater als String übergeben.
    Stellt damit eine Request an besagte URL und liefert den HTML Inhalt der Response als String zurück."""

    response = requests.get(url, headers=header)
    return response.text
