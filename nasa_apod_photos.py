import pathlib
import os

from dotenv import load_dotenv
import requests

from download import download_photo

def nasa_apod_photos(url, path, api_token):
    params= {
        "api_key": api_token,
        "count": 20
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    photo_info=response.json()
    formatting_download_url(photo_info, folder_name)

def formatting_download_url(photo_info):

    for index,  data in enumerate(photo_info):
        photo_url = data['url']
        parse = urllib.parse.urlsplit(photo_url)
        extension = os.path.splitext(parse.path)[1]
        filename = os.path.join(path, f"nasa_apod{index}{extension}")

        download_photo(photo_url,filename,params)


def main():
    path = "image"
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)

    load_dotenv()
    api_token = os.getenv('API_TOKEN_NASA')

    url_nasa_apod_photos = "https://api.nasa.gov/planetary/apod"

    nasa_apod_photos(url_nasa_apod_photos, path, api_token)


if __name__ == '__main__':
    main()
