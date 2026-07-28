import os
import sys
import json
from http.server import BaseHTTPRequestHandler

# اجازه بده utils.py و telegram_client.py که توی ریشه‌ی پروژه‌ن پیدا بشن
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from utils import get_date_info
from telegram_client import run_async, send_text

# اختیاری ولی توصیه‌شده: یه secret توی setWebhook ست کن تا مطمئن بشی
# درخواست واقعا از طرف تلگرامه. راهنماش توی README هست.
WEBHOOK_SECRET = os.getenv("TELEGRAM_WEBHOOK_SECRET")


class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        if WEBHOOK_SECRET:
            token = self.headers.get("X-Telegram-Bot-Api-Secret-Token")
            if token != WEBHOOK_SECRET:
                self.send_response(401)
                self.end_headers()
                self.wfile.write(b"unauthorized")
                return

        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length) if length else b"{}"

        try:
            update = json.loads(body)
        except json.JSONDecodeError:
            update = {}

        message = update.get("message") or update.get("edited_message") or {}
        text = (message.get("text") or "").strip()
        chat = message.get("chat") or {}
        chat_id = chat.get("id")

        if chat_id:
            # چون ربات ممکنه توی گروه باشه، دستور میتونه به شکل /date@your_bot هم بیاد
            command = text.split()[0].split("@")[0] if text else ""

            if command == "/date":
                run_async(send_text(chat_id, get_date_info()))
            elif command == "/id":
                run_async(send_text(chat_id, f"Chat ID:\n{chat_id}"))

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"ok": true}')
