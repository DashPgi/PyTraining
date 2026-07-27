import os
import datetime
import asyncio
import pytz
import jdatetime

from dotenv import load_dotenv
from PIL import Image, ImageDraw, ImageFont

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)

from apscheduler.schedulers.asyncio import AsyncIOScheduler


load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


IMAGE_PATH = "sticker.png"
OUTPUT_PATH = "daily_sticker.png"


class DateBot:

    def __init__(self):
        self.scheduler = AsyncIOScheduler(
            timezone="Asia/Tehran"
        )


    async def get_date_info(self):

        tz = pytz.timezone(
            "Asia/Tehran"
        )

        now = datetime.datetime.now(tz)

        shamsi = jdatetime.date.fromgregorian(
            date=now.date()
        ).strftime("%Y/%m/%d")

        gregorian = now.strftime(
            "%Y-%m-%d"
        )

        return (
            f"📅 {shamsi}\n"
            f"🌍 {gregorian}"
        )


    def create_sticker_image(self, text):

        img = Image.open(
            IMAGE_PATH
        ).convert(
            "RGBA"
        )


        draw = ImageDraw.Draw(img)


        # Change font path if needed
        font = ImageFont.truetype(
            "arial.ttf",
            60
        )


        width, height = img.size


        bbox = draw.textbbox(
            (0,0),
            text,
            font=font
        )


        text_width = (
            bbox[2] - bbox[0]
        )

        text_height = (
            bbox[3] - bbox[1]
        )


        position = (
            (width - text_width)//2,
            height - text_height - 50
        )


        # shadow
        draw.text(
            (
                position[0]+3,
                position[1]+3
            ),
            text,
            font=font,
            fill="black"
        )


        # main text
        draw.text(
            position,
            text,
            font=font,
            fill="white"
        )


        img.save(
            OUTPUT_PATH
        )


    async def send_daily_sticker(
            self,
            application
    ):

        print("Creating sticker...")


        date_text = await self.get_date_info()


        self.create_sticker_image(
            date_text
        )


        await application.bot.send_photo(
            chat_id=CHAT_ID,
            photo=open(
                OUTPUT_PATH,
                "rb"
            ),
            caption="☀️ صبح بخیر"
        )


        print(
            "Sticker sent"
        )



    async def date_command(
            self,
            update: Update,
            context: ContextTypes.DEFAULT_TYPE
    ):

        text = await self.get_date_info()

        await update.message.reply_text(
            text
        )


    async def id_command(
            self,
            update: Update,
            context: ContextTypes.DEFAULT_TYPE
    ):

        await update.message.reply_text(
            f"Chat ID:\n{update.effective_chat.id}"
        )



    def start_scheduler(
            self,
            application
    ):

        self.scheduler.add_job(
            self.send_daily_sticker,
            trigger="cron",
            hour=20,
            minute=52,
            args=[application],
            id="daily_sticker",
            replace_existing=True
        )


        self.scheduler.start()



async def main():

    bot_logic = DateBot()


    application = (
        ApplicationBuilder()
        .token(TOKEN)
        .build()
    )


    application.add_handler(
        CommandHandler(
            "date",
            bot_logic.date_command
        )
    )


    application.add_handler(
        CommandHandler(
            "id",
            bot_logic.id_command
        )
    )


    await application.initialize()

    await application.start()


    bot_logic.start_scheduler(
        application
    )


    await application.updater.start_polling()


    print(
        "🤖 Bot running"
    )


    while True:
        await asyncio.sleep(1)



if __name__ == "__main__":

    asyncio.run(main())