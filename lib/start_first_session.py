from pyrogram import Client
from lib.config import API_HASH, API_ID, LOGIN, PHONE


# bot = Client(name=LOGIN, api_id=API_ID, api_hash=API_HASH, phone_number=PHONE)
# print(bot.export_session_string())
# bot.run()

with Client(name=LOGIN, api_id=API_ID, api_hash=API_HASH, phone_number=PHONE) as bot:
    print(bot.export_session_string())