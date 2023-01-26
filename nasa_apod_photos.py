import pathlib
import os

import requests
import urllib
from dotenv import load_dotenv


from download import download_photo

def nasa_apod_photos(url, folder_name, api_token):
    params= {
        "api_key": api_token,
        "count": 20
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    photo_info=response.json()
    formatting_download_url(photo_info, folder_name,params)


def formatting_download_url(photo_info, folder_name,params ):

    for index,  data in enumerate(photo_info):
        photo_url = data['url']
        parse = urllib.parse.urlsplit(photo_url)
        extension = os.path.splitext(parse.path)[1]
        filename = os.path.join(folder_name, f"nasa_apod{index}{extension}")

        download_photo(photo_url,filename,params)
    print("скачка завершенена")


def main():
    path = "image"
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)

    load_dotenv()
    api_token = os.getenv('API_TOKEN_NASA')

    url_nasa_apod_photos = "https://api.nasa.gov/planetary/apod"

    nasa_apod_photos(url_nasa_apod_photos, path, api_token)


if __name__ == '__main__':
    main()
