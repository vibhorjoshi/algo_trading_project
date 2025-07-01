import gspread
from google.oauth2.service_account import Credentials
import os
from backend.config import SHEET_ID, CREDENTIALS_PATH

def init_gsheets():
    try:
        scope = ["https://www.googleapis.com/auth/spreadsheets",
                 "https://www.googleapis.com/auth/drive"]
        
        print(f"Using credentials file at: {CREDENTIALS_PATH}")
        if not os.path.exists(CREDENTIALS_PATH):
            raise FileNotFoundError(f"Credentials file not found at {CREDENTIALS_PATH}")
        
        creds = Credentials.from_service_account_file(CREDENTIALS_PATH, scopes=scope)
        client = gspread.authorize(creds)
        return client.open_by_key(SHEET_ID)
    except Exception as e:
        print(f"Error initializing Google Sheets: {str(e)}")
        return None

def log_trade(sheet, symbol, date, action, price, quantity):
    if sheet is None:
        print("Skipping trade log - Sheet not initialized")
        return
        
    try:
        trade_log = sheet.worksheet("Trade Log")
        trade_log.append_row([symbol, str(date), action, price, quantity])
    except Exception as e:
        print(f"Error logging trade: {str(e)}")

def update_summary(sheet, symbol, pnl, win_ratio, accuracy):
    if sheet is None:
        print("Skipping summary update - Sheet not initialized")
        return
        
    try:
        summary = sheet.worksheet("Summary")
        summary.append_row([symbol, pnl, win_ratio, accuracy])
    except Exception as e:
        print(f"Error updating summary: {str(e)}")