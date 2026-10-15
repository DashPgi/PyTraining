import os
import requests

BOT_TOKEN = "8146929899:AAFkgSCUPxvpXQHVJj6cUSKtdIZs9vRieco"
CHAT_ID = "-5444879606"
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

response = requests.post(
    url,
    json={
        "chat_id": CHAT_ID,
        "text": "عموهایی داری همچو 2000"
    }
)

print("test")