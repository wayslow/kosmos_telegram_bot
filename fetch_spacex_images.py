import argparse
import pathlib
import datetime

import requests
from urllib.parse import urlparse

from download import download_photo

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-id', help='Ваша ссылка', default='latest')
    args = parser.parse_args()
    id_fetch_spacex = args.id

    folder_name = "image"
    pathlib.Path(folder_name).mkdir(parents=True, exist_ok=True)

    fetch_spacex_launch(folder_name, id_fetch_spacex)


def fetch_spacex_launch(folder_name,id_fetch_spacex):

    url = 'https://api.spacexdata.com/v5/launches/'

    params={
        "id":id_fetch_spacex
    }

    if id_fetch_spacex == 'latest':
        url= f'https://api.spacexdata.com/v5/launches/{id_fetch_spacex}'

    response = requests.get(url, params=params)
    response.raise_for_status()

    if print(response.json()['links']['flickr']['original']) == []:
        print('фотографий нет ')

    for dick_photo_url in response.json()['links']['flickr']['original']:
        for index,photo_url in enumerate(dick_photo_url):
            path = os.path.join(folder_name, f"spaseX_{index}.jpg")
            download_photo(photo_url, path)


if __name__ == '__main__':
    main()
