import requests

def download_photo(photo_url, filename, params=None):
    print(params)
    response = requests.get(photo_url,params=params)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)



