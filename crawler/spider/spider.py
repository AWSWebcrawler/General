import requests

def executeRequest(url, user_agent):
    """Methode erhält eine URL und einen user_agent als String übergeben.
    Stellt damit eine Request an besagte URL und liefert den HTML Inhalt der Response als String zurück."""
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': user_agent
        }

    response = requests.get(url, headers=headers)
    return response.text
