import os
from dotenv import load_dotenv

import telegram
load_dotenv()
api_token = os.getenv('API_TOKEN_TELEGRAM')
bot = telegram.Bot(token=api_token)



def main():
    chat_id = "@photo_kosmos"
    bot.send_message(chat_id=chat_id, text="I'm sorry Dave I'm afraid I can't do that.")

if __name__ == '__main__':
    main()