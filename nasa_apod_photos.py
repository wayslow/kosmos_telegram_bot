import pathlib

import requests

from download import download


def nasa_apod_photos(url, path, api_token):
    params= {
        "api_key": api_token,
        "count":20
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    for index,  data in enumerate(response.json()):
        photo_url = data['url']
        parse = urllib.parse.urlsplit(photo_url)
        extension = os.path.splitext(parse.path)[1]

        filename = os.path.join(path, f"nasa_apod{index}{extension}")
        download(photo_url,filename)


def main():
    path = "image"
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)

    load_dotenv()
    api_token = os.getenv('API_TOKEN_NASA')

    url_nasa_apod_photos = "https://api.nasa.gov/planetary/apod"

    nasa_apod_photos(url_nasa_apod_photos, path, api_token)


if __name__ == '__main__':
    main()
