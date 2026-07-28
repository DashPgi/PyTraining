import os
import datetime
import pytz
import jdatetime

from PIL import Image, ImageDraw, ImageFont


# روی Vercel، مسیر نسبی همیشه از ریشه‌ی پروژه خونده میشه (نه از کنار همین فایل)
# پس sticker.png و فونت رو توی ریشه‌ی پروژه بذار.
IMAGE_PATH = os.getenv("STICKER_IMAGE_PATH", "sticker.png")

# مسیر فونت رو خودت میدی (با env var FONT_PATH) - دیگه به arial.ttf گیر نمی‌کنه
FONT_PATH = os.getenv("FONT_PATH", "font.ttf")

# استیکر تلگرام باید مربعی و WEBP باشه، هر ضلع حداکثر 512 پیکسل
STICKER_SIZE = 512

# روی Vercel فقط پوشه‌ی /tmp قابل نوشتنه
OUTPUT_PATH = "/tmp/daily_sticker.webp"


def get_date_info() -> str:
    tz = pytz.timezone("Asia/Tehran")
    now = datetime.datetime.now(tz)

    shamsi = jdatetime.date.fromgregorian(date=now.date()).strftime("%Y/%m/%d")
    gregorian = now.strftime("%Y-%m-%d")

    return f"📅 {shamsi}\n🌍 {gregorian}"


def _make_square(img: Image.Image) -> Image.Image:
    """عکس ورودی رو مربعی میکنه (crop از وسط) و به سایز استاندارد استیکر ریسایز میکنه."""
    width, height = img.size
    side = min(width, height)

    left = (width - side) // 2
    top = (height - side) // 2

    img = img.crop((left, top, left + side, top + side))
    img = img.resize((STICKER_SIZE, STICKER_SIZE), Image.LANCZOS)

    return img


def create_sticker_image(text: str, font_size: int = 60) -> str:
    """
    عکس sticker.png رو مربعی میکنه، تاریخ رو روش مینویسه
    و به صورت WEBP (فرمت مورد نیاز استیکر تلگرام) ذخیره میکنه.
    خروجی: مسیر فایل ساخته‌شده.
    """
    if not os.path.exists(IMAGE_PATH):
        raise FileNotFoundError(
            f"فایل sticker.png پیدا نشد: {IMAGE_PATH} - مطمئن شو کنار پروژه گذاشتیش."
        )

    if not os.path.exists(FONT_PATH):
        raise FileNotFoundError(
            f"فایل فونت پیدا نشد: {FONT_PATH} - مسیرش رو با env var به اسم "
            f"FONT_PATH بده یا فایل فونتت رو با همین اسم کنار پروژه بذار."
        )

    img = Image.open(IMAGE_PATH).convert("RGBA")
    img = _make_square(img)

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT_PATH, font_size)

    width, height = img.size

    # از multiline_textbbox استفاده میکنیم چون متن دو خطیه (\n داره)
    bbox = draw.multiline_textbbox((0, 0), text, font=font, align="center")
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    position = (
        (width - text_width) // 2,
        height - text_height - 50,
    )

    shadow_pos = (position[0] + 3, position[1] + 3)

    draw.multiline_text(shadow_pos, text, font=font, fill="black", align="center")
    draw.multiline_text(position, text, font=font, fill="white", align="center")

    img.save(OUTPUT_PATH, format="WEBP")

    return OUTPUT_PATH
