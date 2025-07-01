# backend/ml_model.py
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

def prepare_features(data):
    # Calculate MACD
    data["EMA12"] = data["Close"].ewm(span=12, adjust=False).mean()
    data["EMA26"] = data["Close"].ewm(span=26, adjust=False).mean()
    data["MACD"] = data["EMA12"] - data["EMA26"]
    data["Signal_Line"] = data["MACD"].ewm(span=9, adjust=False).mean()
    
    # Calculate price change for target
    data["Price_Change"] = data["Close"].pct_change().shift(-1)
    data["Target"] = np.where(data["Price_Change"] > 0, 1, 0)
    
    # Drop unnecessary columns and missing values
    data = data.drop(["EMA12", "EMA26"], axis=1)
    data.dropna(inplace=True)
    
    return data

def train_model(data):
    features = ["RSI", "MACD", "Signal_Line", "Volume"]
    
    # Ensure we have all required features
    for feature in features:
        if feature not in data.columns:
            print(f"Warning: Missing feature {feature}")
            return None, 0
    
    X = data[features]
    y = data["Target"]
    
    if len(X) < 10:
        print("Not enough data for training")
        return None, 0
        
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = DecisionTreeClassifier(max_depth=5, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    return model, accuracy