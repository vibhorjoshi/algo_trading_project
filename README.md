# 📈 ML-Powered Algorithmic Trading System

A comprehensive algorithmic trading system featuring backtesting, machine learning predictions, and real-time alerts via Google Sheets and Telegram. Includes an interactive dashboard built with Flask.

---

## ✨ Features

- **📊 Advanced Backtesting Engine**  
  Simulate trading strategies on historical data with metrics like PNL and Win Ratio.

- **🤖 Machine Learning Integration**  
  Uses a Decision Tree classifier to predict price movements.

- **📉 Technical Analysis**  
  Implements RSI, Moving Averages, MACD, Volume indicators.

- **📝 Google Sheets Logging**  
  Logs trade entries, ML predictions, and backtest results in real-time.

- **📨 Telegram Alerts**  
  Sends live alerts on trades, signals, and system errors.

- **🌐 Interactive Web Dashboard**  
  Built with Flask to control and monitor your algorithmic trading system.

- **🔌 Modular REST API**  
  Exposes endpoints to control, monitor, and fetch performance data programmatically.

---

## 🚀 Screenshots

> Click on any image to view full size.

### 📊 Backtest Control Panel  
[![Backtest Dashboard](https://via.placeholder.com/600x300.png?text=Backtest+Dashboard)](Screenshot%202025-07-01%20221307.jpg)

### 📡 Live Signal Monitor  
[![Signal Overview](https://via.placeholder.com/600x300.png?text=Live+Signals)](Screenshot%202025-07-01%20221909.png)

### 📈 API Metrics Output  
[![API JSON Output](https://via.placeholder.com/600x300.png?text=API+Metrics)](Screenshot%202025-07-01%20223036.png)

---

## 🛠️ Technologies Used

- **Python 3.x**
- **Flask** – Web API and frontend integration
- **Pandas, NumPy** – Data handling and preprocessing
- **Scikit-learn** – ML model (Decision Tree Classifier)
- **gspread + google-auth-oauthlib** – Google Sheets integration
- **Requests** – HTTP requests for Telegram & Alpha Vantage
- **Altair** – (optional) for charts and visualizations

---

## ⚙️ Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/algo_trading_project.git
cd algo_trading_project
