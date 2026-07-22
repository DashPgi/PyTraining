import os
import json
from telegram.constants import ChatAction
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, MessageHandler, CommandHandler, filters, ContextTypes
from openai import OpenAI

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# آدرس صفحه GUI (bot_gui.html) که باید روی یک هاست HTTPS عمومی آپلود بشه.
# مثال: https://yourdomain.com/bot_gui.html
GUI_URL = os.getenv("GUI_URL", "")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY
)

MODEL = "anthropic/claude-sonnet-5"
# اگه اعتبار حساب OpenRouter کم باشه، این عدد رو کاهش بده (مثلاً 1200)
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "1500"))

CREDIT_ERROR_MESSAGE = (
    "💳 اعتبار حساب OpenRouter شما کافی نیست (خطای ۴۰۲).\n\n"
    "این ربطی به کد نداره؛ یعنی حساب OpenRouter‌ات یا اعتبار نداره یا تمومش کردی.\n"
    "برای رفع:\n"
    "۱. به https://openrouter.ai/settings/credits سر بزن و شارژ کن.\n"
    "۲. یا در فایل .env مقدار MAX_TOKENS رو کمتر کن (مثلاً 800) تا هزینه هر درخواست کمتر بشه.\n"
    "۳. یا موقتاً یک مدل ارزان‌تر/رایگان‌تر رو در متغیر MODEL جایگزین کن."
)

# ---------------------------------------------------------
# پرامپت‌های سیستمی
# ---------------------------------------------------------

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

FLOW_BUILD_PROMPT = """
تو یک برنامه‌نویس متخصص پایتون و کتابخانه python-telegram-bot هستی.
ورودی تو یک فایل JSON است که یک فلوی بصری (شبیه n8n) را توصیف می‌کند؛
این فلو توسط کاربر با کشیدن و وصل‌کردن نودها در یک رابط گرافیکی ساخته شده.

ساختار JSON:
- nodes: لیستی از نودها، هرکدام با id، type (نوع نود) و data (تنظیمات نود)
- links: لیستی از اتصالات بین نودها (from -> to) که مسیر اجرای فلو را مشخص می‌کند

انواع نود ممکن: trigger_message, trigger_command, condition, delay,
send_message, send_buttons, save_data, read_data, http_request, ai_response, end

وظیفه‌ات:
1. ساختار JSON را بخوان و مسیر اجرا را از روی links دنبال کن.
2. بر اساس ترتیب و نوع نودها، کد کامل و قابل‌اجرای ربات تلگرام را با
   python-telegram-bot (نسخه ۲۰ به بالا) تولید کن.
3. برای نود condition از منطق if/else واقعی استفاده کن.
4. برای نود send_buttons از InlineKeyboardMarkup استفاده کن.
5. برای نود save_data/read_data یک فایل JSON ساده به‌عنوان ذخیره‌ساز پیاده کن،
   مگر این‌که در data چیز دیگری مشخص شده باشد.
6. برای نود ai_response یک فراخوانی OpenAI-compatible client (مثل OpenRouter) بگذار.
7. فقط کد پایتون کامل تولید کن (در بلاک کد)، به‌همراه حداکثر ۲ خط توضیح کوتاه قبل از آن.
"""

REFUSAL_MESSAGE = (
    "🤖 این ربات فقط برای «ساخت ربات‌های تلگرامی» طراحی شده.\n"
    "لطفاً فقط ایده یا مشخصات رباتی که می‌خواهی ساخته بشه رو بفرست."
)

# ---------------------------------------------------------
# توابع کمکی برای فراخوانی مدل
# ---------------------------------------------------------

class InsufficientCreditsError(Exception):
    pass


def ask_model(system_prompt: str, user_content: str) -> str:
    try:
        response = client.chat.completions.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            temperature=0.3,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content},
            ],
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        msg = str(e)
        if "402" in msg or "more credits" in msg or "afford" in msg:
            raise InsufficientCreditsError(msg) from e
        raise


def classify_message(text: str) -> str:
    result = ask_model(CLASSIFIER_PROMPT, text)
    return "BUILD_REQUEST" if "BUILD_REQUEST" in result else "OTHER"


async def show_typing(context: ContextTypes.DEFAULT_TYPE, chat_id: int):
    """نشون دادن نشانه 'در حال تایپ...' به کاربر تا حس نکنه ربات هنگ کرده."""
    try:
        await context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
    except Exception:
        pass


# ---------------------------------------------------------
# state هر کاربر در context.user_data:
#   "state"     -> None یا "awaiting_answers"
#   "idea"      -> متن ایده اولیه کاربر
#   "questions" -> سوالاتی که از کاربر پرسیده شد
# ---------------------------------------------------------

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    chat_id = update.effective_chat.id
    state = context.user_data.get("state")

    # پیام موقت «در حال فکر کردن» تا کاربر حس نکنه ربات هنگ کرده
    thinking_msg = await update.message.reply_text("🤔 در حال بررسی درخواست شما...")
    await show_typing(context, chat_id)

    try:
        # ---------- حالت ۱: منتظر پاسخ به سوالات قبلی ----------
        if state == "awaiting_answers":
            idea = context.user_data.get("idea", "")
            questions = context.user_data.get("questions", "")

            full_context = (
                f"ایده اولیه کاربر:\n{idea}\n\n"
                f"سوالاتی که پرسیده شد:\n{questions}\n\n"
                f"پاسخ‌های کاربر:\n{user_text}\n\n"
                "حالا با توجه به همه این اطلاعات، کد کامل ربات تلگرام را بساز."
            )

            await thinking_msg.edit_text("⚙️ در حال ساخت کد ربات...")
            await show_typing(context, chat_id)
            code_result = ask_model(BUILD_PROMPT, full_context)

            await thinking_msg.edit_text(code_result)
            context.user_data.clear()
            return

        # ---------- حالت ۲: پیام جدید (منتظر ایده) ----------
        category = classify_message(user_text)

        if category != "BUILD_REQUEST":
            await thinking_msg.edit_text(REFUSAL_MESSAGE)
            return

        # بررسی نیاز به سوال قبل از ساخت
        await show_typing(context, chat_id)
        questions = ask_model(QUESTIONS_PROMPT, user_text)

        if "NO_QUESTIONS_NEEDED" in questions:
            await thinking_msg.edit_text("⚙️ در حال ساخت کد ربات...")
            await show_typing(context, chat_id)
            code_result = ask_model(BUILD_PROMPT, user_text)
            await thinking_msg.edit_text(code_result)
            context.user_data.clear()
        else:
            context.user_data["state"] = "awaiting_answers"
            context.user_data["idea"] = user_text
            context.user_data["questions"] = questions
            await thinking_msg.edit_text(questions)

    except InsufficientCreditsError:
        await thinking_msg.edit_text(CREDIT_ERROR_MESSAGE)
        context.user_data.clear()
    except Exception as e:
        await thinking_msg.edit_text(f"خطا:\n{e}")
        context.user_data.clear()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """پیام خوش‌آمد + دکمه اختیاری GUI (فقط برای کاربرهای کاربلد)."""
    text = (
        "سلام! ایده‌ی ربات تلگرامی‌ات رو برام بنویس تا برات بسازمش.\n\n"
        "اگه دوست داری فلوی ربات رو با کشیدن و وصل‌کردن نودها (مثل n8n) طراحی کنی، "
        "از دکمه‌ی زیر استفاده کن (کاملاً اختیاری)."
    )
    if GUI_URL:
        keyboard = InlineKeyboardMarkup([[
            InlineKeyboardButton("🧩 باز کردن محیط طراحی فلو", web_app=WebAppInfo(url=GUI_URL))
        ]])
        await update.message.reply_text(text, reply_markup=keyboard)
    else:
        await update.message.reply_text(text)


async def handle_webapp_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """داده‌ی JSON فلو که از GUI ارسال شده رو می‌گیره و ربات نهایی رو می‌سازه."""
    chat_id = update.effective_chat.id
    raw = update.effective_message.web_app_data.data

    thinking_msg = await update.message.reply_text("⚙️ در حال ساخت ربات از روی فلوی طراحی‌شده...")
    await show_typing(context, chat_id)

    try:
        flow = json.loads(raw)
        code_result = ask_model(FLOW_BUILD_PROMPT, json.dumps(flow, ensure_ascii=False, indent=2))
        await thinking_msg.edit_text(code_result)
    except json.JSONDecodeError:
        await thinking_msg.edit_text("خطا: داده‌ی دریافتی از GUI معتبر نبود.")
    except InsufficientCreditsError:
        await thinking_msg.edit_text(CREDIT_ERROR_MESSAGE)
    except Exception as e:
        await thinking_msg.edit_text(f"خطا:\n{e}")


app = Application.builder().token(TELEGRAM_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, handle_webapp_data))
app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, chat)
)

print("Bot Start Shod...")
app.run_polling()