import requests
import pathlib
from get_info import get_path

from urllib.parse import urlparse
import argparse


def fetch_spacex_last_launch(path,id):
    url = 'https://api.spacexdata.com/v5/launches/'

    params={
        "id":id
    }

    if id == 'latest':
        url= f'https://api.spacexdata.com/v5/launches/{id}'


    response = requests.get(url, params=params)
    response.raise_for_status()
    pprint(response.json())
    for dick_photo_url in response.json()['links']['flickr']['original']:
        for index,photo_url in enumerate(dick_photo_url):
            response = requests.get(photo_url)
            response.raise_for_status()
            filename = os.path.join(path, f"spaseX{index}.")
            with open(filename, 'wb') as file:
                file.write(response.content)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-id', help='Ваша ссылка', default='latest')
    args = parser.parse_args()
    id = args.id
    path = get_path()
    fetch_spacex_last_launch(path, id)


if __name__ == '__main__':
    main()