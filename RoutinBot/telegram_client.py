import os
import asyncio

from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


def run_async(coro):
    """چون هندلرهای Vercel سنکرون هستن ولی python-telegram-bot v20+ فقط async ـه."""
    return asyncio.run(coro)


async def send_text(chat_id, text):
    async with Bot(token=BOT_TOKEN) as bot:
        await bot.send_message(chat_id=chat_id, text=text)


async def send_sticker(chat_id, sticker_path):
    async with Bot(token=BOT_TOKEN) as bot:
        with open(sticker_path, "rb") as f:
            await bot.send_sticker(chat_id=chat_id, sticker=f)
