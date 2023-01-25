import requests

def download(photo_url, filename):
    response = requests.get(photo_url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)



