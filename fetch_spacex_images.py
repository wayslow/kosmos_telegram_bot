import argparse
import pathlib
import datetime

import requests
from urllib.parse import urlparse

from download import download_photo

def fetch_spacex_launch(folder_name , spacex_id):

    spacex_url = 'https://api.spacexdata.com/v5/launches/'

    params={
        "id":id_spacex
    }

    if id_spacex == 'latest':
        spacex_url= f'https://api.spacexdata.com/v5/launches/{spacex_id}'

    response = requests.get(spacex_url, params=params)
    response.raise_for_status()

    for photo_urls in response.json()['links']['flickr']['original']:
        for index, photo_url in enumerate(photo_urls):
            path = os.path.join(folder_name, f"spaseX_{index}.jpg")
            download_photo(photo_url, path)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-id', help='Ваша ссылка', default='latest')
    args = parser.parse_args()
    spacex_id = args.id

    folder_name = "image"
    pathlib.Path(folder_name).mkdir(parents=True, exist_ok=True)

    fetch_spacex_launch(folder_name, spacex_id)


if __name__ == '__main__':
    main()
