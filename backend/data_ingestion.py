import requests
import pandas as pd
from backend.config import ALPHA_VANTAGE_API_KEY
# Ensure the config file is correctly imported
# from config import SHEET_ID, TELEGRAM_TOKEN, TELEGRAM_CHAT_ID, STOCKS
# backend/data_ingestion.py
# This module fetches stock data from Alpha Vantage and processes it into a DataFrame.
# backend/data_ingestion.py

def fetch_stock_data(symbol):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={ALPHA_VANTAGE_API_KEY}&outputsize=compact"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if "Time Series (Daily)" not in data:
            print(f"Error fetching data for {symbol}: {data}")
            return None
            
        df = pd.DataFrame.from_dict(data["Time Series (Daily)"], orient="index")
        df = df.rename(columns={
            "1. open": "Open", 
            "2. high": "High",
            "3. low": "Low",
            "4. close": "Close",
            "5. volume": "Volume"
        })
        df.index = pd.to_datetime(df.index)
        df = df.sort_index()
        
        # Convert to float
        for col in df.columns:
            df[col] = df[col].astype(float)
            
        return df
        
    except Exception as e:
        print(f"Error fetching data for {symbol}: {str(e)}")
        return None