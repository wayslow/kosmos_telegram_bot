import os
from dotenv import load_dotenv

import requests
import pathlib

from urllib.parse import urlparse
import argparse

from pprint import pprint
import datetime



def fetch_spacex_last_launch(url, path):
    response = requests.get(url)
    response.raise_for_status()
    for dick_foto_url in response.json()['links']['flickr']['original']:
        for index,foto_url in enumerate(dick_foto_url):
            response = requests.get(foto_url)
            response.raise_for_status()
            filename = os.path.join(path, f"spaseX{index}")
            with open(filename, 'wb') as file:
                file.write(response.content)


def nasa_apod_fotos(url, path, api_token):
    params= {
        "api_key": api_token,
        "count":20
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    for index,  data in enumerate(response.json()):
        foto_url = data['url']
        response = requests.get(foto_url)
        response.raise_for_status()
        parse = urllib.parse.urlsplit(foto_url)
        extension = os.path.splitext(parse.path)[1]

        filename = os.path.join(path, f"nasa_apod{index}{extension}")
        print(filename)
        with open(filename, 'wb') as file:
            file.write(response.content)


def nasa_epik_fotos(url, path , api_token):
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
        foto_url = f"https://epic.gsfc.nasa.gov/archive/natural/{formatted_date}/{type_file}/{nameimage}.{type_file}"

        response = requests.get(foto_url)
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
    url_nasa_apod_fotos = "https://api.nasa.gov/planetary/apod"
    url_nasa_epik_fotos = '  https://api.nasa.gov/EPIC/api/natural/images'

    #fetch_spacex_last_launch(spacex_url, path)
    #nasa_apod_fotos(url_nasa_apod_fotos, path, api_token)
    nasa_epik_fotos(url_nasa_epik_fotos, path, api_token)



if __name__ == '__main__':
    main()
