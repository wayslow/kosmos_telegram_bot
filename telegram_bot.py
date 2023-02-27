import os
import time
import random
import argparse

from dotenv import load_dotenv

import telegram


def photo_upload(folder_name, chat_id, files, time_sleep,bot):
    while True:
        random.shuffle(files)
        for file in files:
            path = os.path.join(folder_name, file)
            with open(path, 'rb') as photo
                bot.send_photo(chat_id=chat_id, photo=photo)
            time.sleep(time_sleep)
        files = os.listdir(folder_name)


def main():
    load_dotenv()
    api_token = os.getenv('TELEGRAM_API_TOKEN')
    chat_id = os.getenv('CHAT_ID')
    bot = telegram.Bot(token=api_token)
    folder_name = "image"
    pathlib.Path(folder_name).mkdir(parents=True, exist_ok=True)
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--time", type=int, default=1440, help="время между отправками сообщение в минутах")
    parser.add_argument("-p", "--photo", type=str, help="путь/и (через пробел) до фото которе хотите вывести ")
    args = parser.parse_args()

    if not args.photo:
        files = os.listdir(folder_name)
    else:
        files = args.photo.split()

    time_sleep = args.time * 60

    pfoto_uplod(folder_name, chat_id, files, time_sleep, bot)


if __name__ == '__main__':
    main()
