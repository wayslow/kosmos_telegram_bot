import os
from dotenv import load_dotenv

import telegram

load_dotenv()
api_token = os.getenv('API_TOKEN_TELEGRAM')
BOT = telegram.Bot(token=api_token)

def main():
    chat_id = "@photo_kosmos"
    BOT.send_document(chat_id=chat_id, document=open(filename, 'rb'))

if __name__ == '__main__':
    main()