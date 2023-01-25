import requests
import pathlib

from get_info import get_path

from urllib.parse import urlparse
import argparse


def fetch_spacex_launch(path,id):

    url = 'https://api.spacexdata.com/v5/launches/'

    params={
        "id":id
    }

    if id == 'latest':
        url= f'https://api.spacexdata.com/v5/launches/{id}'


    response = requests.get(url, params=params)
    response.raise_for_status()

    for dick_photo_url in response.json()['links']['flickr']['original']:
        for index,photo_url in enumerate(dick_photo_url):
            filename = os.path.join(path, f"spaseX{index}.")
            download(photo_url, filename)




def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-id', help='Ваша ссылка', default='latest')
    args = parser.parse_args()
    id_fetch_spacex = args.id

    path = "image"
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)

    fetch_spacex_launch(path, id_fetch_spacex)


if __name__ == '__main__':
    main()