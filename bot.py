import asyncio
import schedule
import time
from telegram import Bot

BOT_TOKEN = "8386118060:AAFWxYyWIBj-PXqvhriVaQab_FkZ849PvUE"
CHAT_ID = "6801660950"
MESSAGE = "Good morning! ☀️ Have a great day!"
SEND_TIME = "07:00"

async def send_message():
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=MESSAGE)

def job():
    asyncio.run(send_message())

schedule.every().day.at(SEND_TIME).do(job)

while True:
    schedule.run_pending()
    time.sleep(30)
