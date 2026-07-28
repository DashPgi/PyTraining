"""
این اسکریپت رو فقط یک بار، روی سیستم خودت (نه روی Vercel) اجرا کن،
درست بعد از اینکه پروژه رو روی Vercel دیپلوی کردی.

اجرا:
    BOT_TOKEN=xxx python set_webhook.py https://your-project.vercel.app [secret]
"""

import sys
import os
import urllib.request
import urllib.parse
import json

BOT_TOKEN = os.getenv("BOT_TOKEN")

if len(sys.argv) < 2:
    print("استفاده: python set_webhook.py https://your-project.vercel.app [webhook_secret]")
    sys.exit(1)

base_url = sys.argv[1].rstrip("/")
secret = sys.argv[2] if len(sys.argv) > 2 else None

webhook_url = f"{base_url}/api/webhook"

params = {"url": webhook_url}
if secret:
    params["secret_token"] = secret

url = f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook?" + urllib.parse.urlencode(params)

with urllib.request.urlopen(url) as resp:
    print(json.loads(resp.read()))
