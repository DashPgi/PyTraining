import os
import json
import datetime
import pytz
import asyncio
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import jdatetime

# Load environment variables
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
# Note: You need to provide a sticker_id in your.env or replace it here
STICKER_ID = os.getenv("STICKER_ID", "CAACAgIAAxkBAA...") 

class DateBot:
    def __init__(self):
        self.scheduler = AsyncIOScheduler(timezone="Asia/Tehran")

    async def get_date_info(self):
        now = datetime.datetime.now()
        shamsi_date = jdatetime.date.fromgregorian(date=now.date()).strftime('%Y/%m/%d')
        gregorian_date = now.strftime('%Y-%m-%d')
        
        # Simple holiday check logic (can be expanded with an API)
        holidays = ["01/01", "01/13"] # Example: Nowruz
        current_shamsi = now.strftime('%m/%d')
        holiday_msg = ""
        if current_shamsi in holidays:
            holiday_msg = "\n🎉 امروز یک مناسبت خاص است!"
            
        return f"📅 تاریخ امروز:\n🇮🇷 شمسی: {shamsi_date}\n🌍 میلادی: {gregorian_date}{holiday_msg}"

    async def date_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handles the /date command"""
        date_text = await self.get_date_info()
        await update.message.reply_text(date_text)

    async def scheduled_task(self, context: ContextTypes.DEFAULT_TYPE):
        """Task to run every day at 07:00 AM"""
        date_text = await self.get_date_info()
        
        # 1. Send "Good Morning" message
        await context.bot.send_message(chat_id=CHAT_ID, text=f"☀️ صبح بخیر!\n\n{date_text}")
        
        # 2. Edit/Send Sticker with text
        # Note: Telegram API does not allow 'editing' a sticker with text directly via standard methods.
        # The standard way is to send a photo or a caption with a sticker.
        # Here we send the sticker with the date as a caption.
        await context.bot.send_sticker(chat_id=CHAT_ID, sticker=STICKER_ID)
        await context.bot.send_message(chat_id=CHAT_ID, text=f"📅 {date_text}")

    def start_scheduler(self, application):
        # Schedule task for 07:00 AM every day
        self.scheduler.add_job(
            self.scheduled_task, 
            'cron', 
            hour=7, 
            minute=0, 
            timezone="Asia/Tehran"
        )
        self.scheduler.start()

async def main():
    if not TOKEN or not CHAT_ID:
        print("Error: TELEGRAM_TOKEN or CHAT_ID not found in.env")
        return

    bot_logic = DateBot()
    application = ApplicationBuilder().token(TOKEN).build()

    # Register commands
    application.add_handler(CommandHandler("date", bot_logic.date_command))

    # Start scheduler
    bot_logic.start_scheduler(application)

    # Run the bot
    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    
    print("Bot is running...")
    
    # Keep running until interrupted
    try:
        while True:
            await asyncio.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        await application.stop()
        await application.shutdown()

if __name__ == '__main__':
    import asyncio
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass