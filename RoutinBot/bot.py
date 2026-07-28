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

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

FONT_PATH = os.getenv("FONT_PATH", os.path.join(BASE_DIR, "font.ttf"))

IMAGE_PATH = os.path.join(BASE_DIR, "sticker.png")
OUTPUT_PATH = os.path.join(BASE_DIR, "daily_sticker.webp")

STICKER_SIZE = 512


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

        img = Image.open(IMAGE_PATH).convert("RGBA")
        img = self._make_square(img)

        try:
            if os.path.exists(FONT_PATH):
                font = ImageFont.truetype(FONT_PATH, 60)
            else:
                print(f"⚠️ فایل فونت پیدا نشد ({FONT_PATH})، از فونت پیش‌فرض استفاده میشه.")
                try:
                    font = ImageFont.load_default(size=60)
                except TypeError:
                    font = ImageFont.load_default()

            draw = ImageDraw.Draw(img)
            width, height = img.size

            bbox = draw.multiline_textbbox((0, 0), text, font=font, align="center")
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]

            position = (
                (width - text_width) // 2,
                height - text_height - 50
            )

            shadow_pos = (position[0] + 3, position[1] + 3)

            draw.multiline_text(shadow_pos, text, font=font, fill="black", align="center")
            draw.multiline_text(position, text, font=font, fill="white", align="center")

        except Exception as e:
            print(f"⚠️ نوشتن متن روی استیکر رد شد: {e}")

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

    async def _delete_command_message(self, update: Update):
        """پیام کامندی که کاربر فرستاده رو از چت پاک میکنه (اگه اجازه داشته باشیم)."""
        try:
            await update.message.delete()
        except Exception as e:
            chat_type = update.effective_chat.type if update.effective_chat else "?"
            print(f"⚠️ نتونستم پیام کامند رو پاک کنم (نوع چت: {chat_type}): {type(e).__name__}: {e}")

    async def date_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await self._delete_command_message(update)
        text = await self.get_date_info()
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    async def id_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await self._delete_command_message(update)
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Chat ID:\n{update.effective_chat.id}"
        )

    async def daily_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """اجرای دستی همون کاری که هر روز سر ساعت مشخص خودکار انجام میشه."""
        await self._delete_command_message(update)
        await self.send_daily_sticker(context.application)

    async def error_handler(self, update: object, context: ContextTypes.DEFAULT_TYPE):
        print(f"⚠️ Error while handling update: {context.error}")

    def start_scheduler(self, application):

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

    application.add_handler(CommandHandler("date", bot_logic.date_command))
    application.add_handler(CommandHandler("id", bot_logic.id_command))
    application.add_handler(CommandHandler("daily", bot_logic.daily_command))
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