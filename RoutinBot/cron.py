import os
import sys
from http.server import BaseHTTPRequestHandler

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from utils import get_date_info, create_sticker_image
from telegram_client import run_async, send_sticker

CHAT_ID = os.getenv("CHAT_ID")

# اختیاری: برای اینکه هرکسی نتونه با زدن این آدرس، استیکر ارسال کنه
CRON_SECRET = os.getenv("CRON_SECRET")


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        if CRON_SECRET:
            auth = self.headers.get("Authorization", "")
            if auth != f"Bearer {CRON_SECRET}":
                self.send_response(401)
                self.end_headers()
                self.wfile.write(b"unauthorized")
                return

        try:
            text = get_date_info()
            sticker_path = create_sticker_image(text)
            run_async(send_sticker(CHAT_ID, sticker_path))

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"sticker sent")

        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode("utf-8"))
