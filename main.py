import os
from dotenv import load_dotenv

import requests
import pathlib

from urllib.parse import urlparse
import argparse



def fetch_spacex_last_launch(url, path):
    response = requests.get(url)
    response.raise_for_status()
    for dick_photo_url in response.json()['links']['flickr']['original']:
        for index,photo_url in enumerate(dick_photo_url):
            response = requests.get(photo_url)
            response.raise_for_status()
            filename = os.path.join(path, f"spaseX{index}.jpg")
            with open(filename, 'wb') as file:
                file.write(response.content)


def nasa_apod_photo(url, path, api_token):
    params= {
        "api_key": api_token,
        "count":20
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    for index,  data in enumerate(response.json()):
        photo_url = data['url']
        response = requests.get(photo_url)
        response.raise_for_status()
        parse = urllib.parse.urlsplit(photo_url)
        extension = os.path.splitext(parse.path)[1]

        filename = os.path.join(path, f"nasa_apod{index}{extension}")
        print(filename)
        with open(filename, 'wb') as file:
            file.write(response.content)


def nasa_epik_photo(url, path , api_token):
    params = {
        "api_key": api_token,
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    for index, data in enumerate(response.json()):

        date_time_obj = datetime.datetime.fromisoformat(data["date"])
        date=datetime.date(date_time_obj.year, date_time_obj.month, date_time_obj.day)
        formatted_date = date.strftime("%Y/%m/%d")

        nameimage = data["image"]
        type_file ="png"
        photo_url = f"https://epic.gsfc.nasa.gov/archive/natural/{formatted_date}/{type_file}/{nameimage}.{type_file}"

        response = requests.get(photo_url)
        response.raise_for_status()
        filename = os.path.join(path, f"nasa_epik{index}.{type_file}")

        with open(filename, 'wb') as file:
            file.write(response.content)


def main():

    path = "image"
    load_dotenv()
    api_token = os.getenv('API_TOKEN')

    pathlib.Path(path).mkdir(parents=True, exist_ok=True)

    spacex_url = 'https://api.spacexdata.com/v5/launches/latest'
    url_nasa_apod_photos = "https://api.nasa.gov/planetary/apod"
    url_nasa_epik_photos = '  https://api.nasa.gov/EPIC/api/natural/images'

    #fetch_spacex_last_launch(spacex_url, path)
    #nasa_apod_photos(url_nasa_apod_photos, path, api_token)
    nasa_epik_photos(url_nasa_epik_photos, path, api_token)



if __name__ == '__main__':
    main()
