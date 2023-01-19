import requests
from get_info import get_nasa_api_key , get_path


def nasa_apod_photos(url, path, api_token):
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
        with open(filename, 'wb') as file:
            file.write(response.content)


def main():
    api_token = get_nasa_api_key()
    path = get_path()
    url_nasa_apod_photos = "https://api.nasa.gov/planetary/apod"

    nasa_apod_photos(url_nasa_apod_photos, path, api_token)


if __name__ == '__main__':
    main()
