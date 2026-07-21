import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from openai import OpenAI

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY
)


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    try:
        response = client.chat.completions.create(
            model="anthropic/claude-sonnet-5",
            max_tokens=2000,
            temperature=0.7,
            messages=[
                {
                    "role": "system",
                    "content": "تو یک دستیار هوش مصنوعی فارسی برای تلگرام هستی. دقیق و مفید جواب بده."
                },
                {
                    "role": "user",
                    "content": user_text
                }
            ]
        )
        answer = response.choices[0].message.content

        await update.message.reply_text(answer)

    except Exception as e:
        await update.message.reply_text(
            f"Erorr :\n{e}"
        )


app = Application.builder().token(TELEGRAM_TOKEN).build()

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, chat)
)

print("Bot Start Shod...")
app.run_polling()
