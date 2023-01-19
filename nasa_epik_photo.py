import requests
from get_info import get_nasa_api_key ,get_path

def nasa_epik_photos(url, path , api_token):

    params = {
        "api_key": api_token,
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    for index, data in enumerate(response.json()):

        date_time_obj = datetime.datetime.fromisoformat(data["date"])
        date =datetime.date(date_time_obj.year, date_time_obj.month, date_time_obj.day)
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
    api_token = get_nasa_api_key()
    path = get_path()
    url_nasa_epik_photos = '  https://api.nasa.gov/EPIC/api/natural/images'

    nasa_epik_photos(url_nasa_epik_photos, path, api_token)

if __name__ == '__main__':
    main()