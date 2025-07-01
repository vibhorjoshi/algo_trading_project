# backend/config.py
import os

# Get the current directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Configuration settings

ALPHA_VANTAGE_API_KEY= "6IOS3K0MPWMBNA9R"
SHEET_ID="verdant-bulwark-427217-j4-63faddba7bbb.json"
TELEGRAM_TOKEN="7910145286:AAH5AXmU_SSYIOwJ5uFyqZ2KQ49qr06pjt4"
TELEGRAM_CHAT_ID="1591824238"
STOCKS=["RELIANCE.BSE", "HDFCBANK.BSE", "INFY.BSE"]

#Path to credentials file
CREDENTIALS_PATH = os.path.join(BASE_DIR, "..", "credentials.json")