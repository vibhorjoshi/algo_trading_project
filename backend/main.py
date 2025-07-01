import pandas as pd
from datetime import datetime, timedelta
import time
from backend.data_ingestion import fetch_stock_data
from backend.strategy import generate_signals
from backend.ml_model import prepare_features, train_model
from backend.sheet_logger import init_gsheets, log_trade, update_summary
from backend.telegram_alert import send_telegram_alert
from backend.config import STOCKS
from backend.config import ALPHA_VANTAGE_API_KEY
# from config import ALPHA_VANTAGE_API_KEY  # Removed: symbol does not exist or is not used
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import uvicorn
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def render_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)


def backtest_strategy(symbol):
    print(f"\nProcessing {symbol}...")
    
    # Fetch and prepare data
    data = fetch_stock_data(symbol)
    if data is None or data.empty:
        print(f"No data available for {symbol}")
        return [], 0, 0, 0
    
    # Filter last 6 months
    end_date = datetime.now()
    start_date = end_date - timedelta(days=180)
    data = data.loc[start_date:end_date]
    
    if len(data) < 50:
        print(f"Not enough data for {symbol} (only {len(data)} records)")
        return [], 0, 0, 0
    
    # Generate signals
    data = generate_signals(data)
    
    # Prepare for ML and train model
    ml_data = prepare_features(data.copy())
    model, accuracy = train_model(ml_data)
    print(f"ML Accuracy for {symbol}: {accuracy:.2%}")
    
    # Backtesting logic
    capital = 100000
    position = 0
    trades = []
    buy_price = 0
    
    for i in range(len(data)):
        if i < 50:  # Skip first 50 days for moving averages
            continue
            
        row = data.iloc[i]
        
        # Buy signal
        if row["Buy_Signal"] and capital > 0 and position == 0:
            position = capital // row["Close"]
            buy_price = row["Close"]
            capital -= position * buy_price
            trades.append({
                "date": row.name,
                "type": "BUY",
                "price": buy_price,
                "quantity": position
            })
        
        # Sell signal
        elif position > 0 and (row["Sell_Signal"] or i == len(data)-1):
            sell_price = row["Close"]
            capital += position * sell_price
            trades.append({
                "date": row.name,
                "type": "SELL",
                "price": sell_price,
                "quantity": position
            })
            position = 0
    
    # Calculate performance
    final_value = capital + (position * data.iloc[-1]["Close"])
    pnl = final_value - 100000
    
    # Calculate win ratio
    win_count = 0
    trade_pairs = []
    for i in range(len(trades)):
        if trades[i]["type"] == "BUY" and i+1 < len(trades) and trades[i+1]["type"] == "SELL":
            trade_pairs.append((trades[i], trades[i+1]))
            if trades[i+1]["price"] > trades[i]["price"]:
                win_count += 1
    
    win_ratio = win_count / len(trade_pairs) if trade_pairs else 0
    
    return trades, pnl, win_ratio, accuracy

def main():
    print("Starting backtest...")
    
    # Initialize Google Sheets
    sheet = init_gsheets()
    
    for symbol in STOCKS:
        try:
            print(f"\nProcessing {symbol}...")
            trades, pnl, win_ratio, accuracy = backtest_strategy(symbol)
            
            # Log trades to Google Sheets
            for trade in trades:
                log_trade(sheet, symbol, trade["date"], trade["type"], trade["price"], trade["quantity"])
            
            # Update summary
            update_summary(sheet, symbol, pnl, win_ratio, accuracy)
            
            # Send alert
            send_telegram_alert(
                f"{symbol} Backtest Complete\nPNL: ₹{pnl:.2f}\nWin Ratio: {win_ratio:.2%}\nAccuracy: {accuracy:.2%}"
            )
            
            print(f"Completed {symbol} | PNL: ₹{pnl:.2f} | Win Ratio: {win_ratio:.2%}")
            
        except Exception as e:
            error_msg = f"Error processing {symbol}: {str(e)}"
            print(error_msg)
            send_telegram_alert(error_msg)
            
        # Add delay between stocks to avoid API rate limits
        time.sleep(15)
    
    print("\nBacktest completed successfully!")

if __name__ == "__main__":
    main()