import pathlib
import os
import datetime

from dotenv import load_dotenv
import requests

from download import download_photo

def nasa_epik_photos_response(url, folder_name , api_token):

    params = {
        "api_key": api_token,
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    photo_info=response.json()
    formatting_download_url(photo_info, folder_name,params)


def formatting_download_url(photo_info,folder_name,params):
    for index, data in enumerate(photo_info):
        date_time_obj = datetime.datetime.fromisoformat(data["date"])
        date =datetime.date(date_time_obj.year, date_time_obj.month, date_time_obj.day)
        formatted_date = date.strftime("%Y/%m/%d")
        name_image = data["image"]
        type_file ="png"
        photo_url = f"https://epic.gsfc.nasa.gov/archive/natural/{formatted_date}/{type_file}/{name_image}.{type_file}"
        path = os.path.join(folder_name, f"nasa_epik{index}.{type_file}")
        download_photo(photo_url, path, params)


def main():
    folder_name = "image"
    pathlib.Path(folder_name).mkdir(parents=True, exist_ok=True)

    load_dotenv()
    api_token = os.getenv('API_TOKEN_NASA')

    url_nasa_epik_photos = '  https://api.nasa.gov/EPIC/api/natural/images'

    nasa_epik_photos_response(url_nasa_epik_photos, folder_name, api_token)

if __name__ == '__main__':
    main()