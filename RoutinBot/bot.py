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

# مسیر فونت رو خودت میدی؛ فایل فونتت (مثلاً یه فونت فارسی) رو کنار همین
# اسکریپت بذار و اسمش رو اینجا یا توی .env با FONT_PATH بده
FONT_PATH = os.getenv("FONT_PATH", "font.ttf")

IMAGE_PATH = "sticker.png"
OUTPUT_PATH = "daily_sticker.webp"   # استیکر تلگرام باید WEBP باشه

STICKER_SIZE = 512   # استیکر تلگرام باید مربعی و حداکثر 512x512 باشه


class DateBot:

    def __init__(self):
        self.scheduler = AsyncIOScheduler(
            timezone="Asia/Tehran"
        )

    async def get_date_info(self):

        tz = pytz.timezone("Asia/Tehran")
        now = datetime.datetime.now(tz)

        shamsi = jdatetime.date.fromgregorian(
            date=now.date()
        ).strftime("%Y/%m/%d")

        gregorian = now.strftime("%Y-%m-%d")

        return (
            f"📅 {shamsi}\n"
            f"🌍 {gregorian}"
        )

    def _make_square(self, img):
        """عکس رو از وسط crop میکنه تا مربعی بشه، بعد به سایز استاندارد استیکر ریسایز میکنه."""
        width, height = img.size
        side = min(width, height)

        left = (width - side) // 2
        top = (height - side) // 2

        img = img.crop((left, top, left + side, top + side))
        img = img.resize((STICKER_SIZE, STICKER_SIZE), Image.LANCZOS)

        return img

    def create_sticker_image(self, text):

        if not os.path.exists(IMAGE_PATH):
            raise FileNotFoundError(f"فایل {IMAGE_PATH} پیدا نشد.")

        if not os.path.exists(FONT_PATH):
            raise FileNotFoundError(
                f"فایل فونت پیدا نشد: {FONT_PATH}\n"
                f"فایل فونتت رو کنار این اسکریپت بذار یا مسیرش رو توی .env "
                f"با FONT_PATH بده."
            )

        img = Image.open(IMAGE_PATH).convert("RGBA")
        img = self._make_square(img)

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(FONT_PATH, 60)

        width, height = img.size

        # چون متن دوخطیه (\n داره)، از multiline استفاده میکنیم تا وسط‌چین درست بشه
        bbox = draw.multiline_textbbox((0, 0), text, font=font, align="center")
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        position = (
            (width - text_width) // 2,
            height - text_height - 50
        )

        shadow_pos = (position[0] + 3, position[1] + 3)

        # shadow
        draw.multiline_text(shadow_pos, text, font=font, fill="black", align="center")

        # main text
        draw.multiline_text(position, text, font=font, fill="white", align="center")

        img.save(OUTPUT_PATH, format="WEBP")

    async def send_daily_sticker(self, application):

        print("Creating sticker...")

        date_text = await self.get_date_info()

        self.create_sticker_image(date_text)

        with open(OUTPUT_PATH, "rb") as sticker_file:
            await application.bot.send_sticker(
                chat_id=CHAT_ID,
                sticker=sticker_file
            )

        await application.bot.send_message(
            chat_id=CHAT_ID,
            text="☀️ صبح بخیر"
        )

        print("Sticker sent")

    async def date_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        text = await self.get_date_info()
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    async def id_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Chat ID:\n{update.effective_chat.id}"
        )

    async def error_handler(self, update: object, context: ContextTypes.DEFAULT_TYPE):
        # هر خطایی توی هندلرها بیفته اینجا لاگ میشه و کل ربات کرش نمیکنه
        print(f"⚠️ Error while handling update: {context.error}")

    def start_scheduler(self, application):

        self.scheduler.add_job(
            self.send_daily_sticker,
            trigger="cron",
            hour=20,
            minute=42,
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

    application.add_handler(CommandHandler("date", bot_logic.date_command))
    application.add_handler(CommandHandler("id", bot_logic.id_command))
    application.add_error_handler(bot_logic.error_handler)

    await application.initialize()
    await application.start()

    bot_logic.start_scheduler(application)

    await application.updater.start_polling(drop_pending_updates=True)

    print("🤖 Bot running")

    while True:
        await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())