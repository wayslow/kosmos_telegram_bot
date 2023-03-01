import pathlib
import os
import datetime

from dotenv import load_dotenv
import requests

from download import download_photo


def get_nasa_epic_photos(url_nasa_epic_photos, folder_name, api_token, type_file="png"):


    params = {
        "api_key": api_token,
    }

    response = requests.get(url_nasa_epic_photos, params=params)
    response.raise_for_status()
    epic_images = response.json()

    for index, images in enumerate(epic_images):
        date_time_obj = datetime.datetime.fromisoformat(images["date"])
        date =datetime.date(date_time_obj.year, date_time_obj.month, date_time_obj.day)
        formatted_date = date.strftime("%Y/%m/%d")
        image_name = images["image"]
        file_name = f"{image_name}.{type_file}"
        photo_url = f"https://epic.gsfc.nasa.gov/archive/natural/{formatted_date}/{type_file}/{file_name}"
        path = os.path.join(folder_name, file_name)

        download_photo(photo_url, path, params)


def main():
    folder_name = "image"
    pathlib.Path(folder_name).mkdir(parents=True, exist_ok=True)

    load_dotenv()
    nasa_api_token = os.getenv("NASA_API_TOKEN")

    url_nasa_epic_photos = 'https://api.nasa.gov/EPIC/api/natural/images'

    get_nasa_epic_photos(url_nasa_epic_photos, folder_name, nasa_api_token)


if __name__ == '__main__':
    main()
