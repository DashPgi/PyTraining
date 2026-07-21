import asyncio
from telegram import Bot

TOKEN = ""
CHAT_ID = ""


async def main():
    bot = Bot(token=TOKEN)

    await bot.send_message(
        chat_id=CHAT_ID,
        text="سلام! 🤖 بات من با پایتون اجرا شد."
    )

    print("پیام ارسال شد!")


asyncio.run(main())
