# backend/strategy.py
import pandas as pd
import numpy as np

def calculate_rsi(data, window=14):
    delta = data["Close"].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    
    avg_gain = gain.rolling(window).mean()
    avg_loss = loss.rolling(window).mean()
    
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_moving_averages(data):
    data["MA20"] = data["Close"].rolling(20).mean()
    data["MA50"] = data["Close"].rolling(50).mean()
    return data

def generate_signals(data):
    # Add RSI and moving averages
    data["RSI"] = calculate_rsi(data)
    data = calculate_moving_averages(data)
    
    # Generate signals
    data["Buy_Signal"] = (data["RSI"] < 30) & (data["MA20"] > data["MA50"])
    data["Sell_Signal"] = (data["RSI"] > 70) | (data["MA20"] < data["MA50"])
    
    # Clean up any infinite values
    data.replace([np.inf, -np.inf], np.nan, inplace=True)
    data.dropna(inplace=True)
    
    return data