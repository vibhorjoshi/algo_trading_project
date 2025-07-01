# backend/telegram_alert.py
import requests
from backend.config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

def send_telegram_alert(message):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message
        }
        response = requests.post(url, json=payload)
        response.raise_for_status()
    except Exception as e:
        print(f"Error sending Telegram alert: {str(e)}")