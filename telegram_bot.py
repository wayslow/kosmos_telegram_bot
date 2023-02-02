import os
from dotenv import load_dotenv

import telegram

load_dotenv()
api_token = os.getenv('TELEGRAM_API_TOKEN')
BOT = telegram.Bot(token=api_token)

def main():
    chat_id = "@photo_kosmos"
    BOT.send_photo(chat_id=chat_id, photo=open('image/epic_1b_20230126000830.png', 'rb'))


if __name__ == '__main__':
    main()