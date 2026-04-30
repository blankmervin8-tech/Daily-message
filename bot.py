import asyncio
import schedule
import time
from telegram import Bot

BOT_TOKEN = BOT_TOKEN = "8386118060:AAFxIr9vwBhZQxua1SKVyFVczixvNhdvXgQ
CHAT_ID = "-1001263402382"
IMAGE_URL = "https://i.imgur.com/I6E1oN2.png"
MESSAGE = "Kayaks for rent!!! 🌊🚣\n13 single kayaks and double kayak available!! Canoe and trailer also available.. $30 a day,$25 for additional days.. call or text 484-340-8966"
SEND_TIME = "07:00"

async def send_message():
    bot = Bot(token=BOT_TOKEN)
    await bot.send_photo(chat_id=CHAT_ID, photo=IMAGE_URL, caption=MESSAGE)

def job():
    asyncio.run(send_message())

schedule.every().day.at(SEND_TIME).do(job)

while True:
    schedule.run_pending()
    time.sleep(30)
