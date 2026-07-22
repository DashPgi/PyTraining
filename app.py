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

MODEL = "anthropic/claude-sonnet-5"

CLASSIFIER_PROMPT = """
تو یک کلاسیفایر هستی. وظیفه‌ات فقط این است که مشخص کنی آیا پیام کاربر
"درخواست ساخت یک ربات تلگرام" است یا نه.

فقط یکی از این دو کلمه را برگردان، بدون هیچ توضیح اضافه:
- BUILD_REQUEST  (اگر کاربر می‌خواهد یک ربات تلگرام ساخته شود، یا در حال توضیح
  ویژگی/ایده‌ای برای همین منظور است)
- OTHER          (هر چیز دیگری: سوال عمومی، چت، درخواست بی‌ربط، یا هر دستوری
  که هدفش ساخت ربات تلگرام نیست)
"""

QUESTIONS_PROMPT = """
تو دستیار متخصص ساخت ربات تلگرام هستی.
کاربر یک ایده برای ساخت ربات تلگرام داده. کارت این است:

1. فقط و فقط سوالات ضروری و مرتبط با همان ایده را از کاربر بپرس تا بتوانی
   کد نهایی ربات را کامل و درست بسازی
   (مثلاً: زبان/کتابخانه مورد نظر، نیاز به دیتابیس، نوع دکمه‌ها و منوها،
   فرمت پیام‌ها، نیاز به ذخیره‌سازی وضعیت کاربر، و غیره).
2. سوالات را شماره‌گذاری‌شده و کوتاه بپرس (حداکثر ۵ سوال).
3. هیچ کد یا توضیح اضافه‌ای ننویس؛ فقط سوالات.
4. اگر پیام کاربر آنقدر کامل و واضح است که نیازی به سوال نیست، فقط دقیقاً
   بنویس: NO_QUESTIONS_NEEDED
"""

BUILD_PROMPT = """
تو یک برنامه‌نویس متخصص پایتون و کتابخانه python-telegram-bot هستی.
وظیفه‌ات فقط و فقط ساخت کد کامل یک ربات تلگرام بر اساس ایده و پاسخ‌های کاربر است.

قوانین:
- فقط کد پایتون کامل و قابل‌اجرا تولید کن (در بلاک کد).
- از کتابخانه python-telegram-bot (نسخه ۲۰ به بالا) استفاده کن، مگر اینکه
  کاربر کتابخانه دیگری خواسته باشد.
- توکن‌ها و کلیدها را از environment variables بخوان (با dotenv).
- کامنت‌های کوتاه فارسی برای بخش‌های مهم کد بگذار.
- خارج از کد فقط یک توضیح خیلی کوتاه (حداکثر ۲ خط) بده، نه بیشتر.
"""

REFUSAL_MESSAGE = (
    "🤖 این ربات فقط برای «ساخت ربات‌های تلگرامی» طراحی شده.\n"
    "لطفاً فقط ایده یا مشخصات رباتی که می‌خواهی ساخته بشه رو بفرست."
)

def ask_model(system_prompt: str, user_content: str) -> str:
    response = client.chat.completions.create(
        model=MODEL,
        max_tokens=3000,
        temperature=0.3,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
        ],
    )
    return response.choices[0].message.content.strip()


def classify_message(text: str) -> str:
    result = ask_model(CLASSIFIER_PROMPT, text)
    return "BUILD_REQUEST" if "BUILD_REQUEST" in result else "OTHER"

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    state = context.user_data.get("state")

    try:
        if state == "awaiting_answers":
            idea = context.user_data.get("idea", "")
            questions = context.user_data.get("questions", "")

            full_context = (
                f"ایده اولیه کاربر:\n{idea}\n\n"
                f"سوالاتی که پرسیده شد:\n{questions}\n\n"
                f"پاسخ‌های کاربر:\n{user_text}\n\n"
                "حالا با توجه به همه این اطلاعات، کد کامل ربات تلگرام را بساز."
            )

            code_result = ask_model(BUILD_PROMPT, full_context)
            await update.message.reply_text(code_result)
            context.user_data.clear()
            return

        category = classify_message(user_text)

        if category != "BUILD_REQUEST":
            await update.message.reply_text(REFUSAL_MESSAGE)
            return

        questions = ask_model(QUESTIONS_PROMPT, user_text)

        if "NO_QUESTIONS_NEEDED" in questions:
            code_result = ask_model(BUILD_PROMPT, user_text)
            await update.message.reply_text(code_result)
            context.user_data.clear()
        else:
            context.user_data["state"] = "awaiting_answers"
            context.user_data["idea"] = user_text
            context.user_data["questions"] = questions
            await update.message.reply_text(questions)

    except Exception as e:
        await update.message.reply_text(f"خطا:\n{e}")
        context.user_data.clear()


app = Application.builder().token(TELEGRAM_TOKEN).build()

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, chat)
)

print("Bot Start Shod...")
app.run_polling()