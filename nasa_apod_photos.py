import pathlib
import os

import requests
import urllib
from dotenv import load_dotenv

from download import download_photo

def get_nasa_apod_photos(nasa_apod_url, folder_name, nasa_api_token):
    params= {
        "api_key": nasa_api_token,
        "count": 30
    }

    response = requests.get(nasa_apod_url, params=params)
    response.raise_for_status()

    for index, photo_apod in enumerate(response.json()):
        photo_apod_url = photo_apod['url']
        parse = urllib.parse.urlsplit(photo_apod_url)
        extension = os.path.splitext(parse.path)[-1]
        path = os.path.join(folder_name, f"nasa_apod{index}{extension}")

        download_photo(photo_apod_url, path, params)


def main():
    folder_name = "image"
    pathlib.Path(folder_name).mkdir(parents=True, exist_ok=True)

    load_dotenv()
    nasa_api_token = os.getenv("NASA_API_TOKEN")

    nasa_apod_url = "https://api.nasa.gov/planetary/apod"

    get_nasa_apod_photos(nasa_apod_url, folder_name, nasa_api_token)


if __name__ == '__main__':
    main()
