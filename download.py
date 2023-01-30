import requests

def download_photo(photo_url, path, params=None):
    response = requests.get(photo_url,params=params)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)
    print(f"{path} сачен")



