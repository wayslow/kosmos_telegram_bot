import pathlib

import os
from dotenv import load_dotenv

def get_path():
    path = "image"
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)
    return path

def get_api_key():
    load_dotenv()
    api_token = os.getenv('API_TOKEN')
    return api_token
