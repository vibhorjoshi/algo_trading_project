# 📈 ML-Powered Algorithmic Trading System

A comprehensive algorithmic trading system featuring backtesting, machine learning predictions, and real-time alerts via Google Sheets and Telegram. Includes an interactive dashboard built with Flask.

---

## ✨ Features

- **📊 Advanced Backtesting Engine**  
  Simulate trading strategies on historical data with metrics like PNL and Win Ratio.

- **🤖 Machine Learning Integration**  
  Uses a Decision Tree classifier to predict price movements.

- **📉 Technical Analysis**  
  Implements RSI, Moving Averages, MACD, and Volume indicators.

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
[![Backtest Dashboard](https://via.placeholder.com/600x300.png?text=Backtest+Dashboard)](https://your-image-host.com/backtest_dashboard.jpg)

### 📡 Live Signal Monitor  
[![Signal Overview](https://via.placeholder.com/600x300.png?text=Live+Signals)](https://your-image-host.com/signal_overview.png)

### 📈 API Metrics Output  
[![API JSON Output](https://via.placeholder.com/600x300.png?text=API+Metrics)](https://your-image-host.com/api_metrics.png)

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
2. Create a Virtual Environment
bash

Collapse

Wrap

Run

Copy
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
3. Install Dependencies
bash

Collapse

Wrap

Run

Copy
pip install -r requirements.txt
If you don’t have a requirements.txt, create it with:

ini

Collapse

Wrap

Copy
Flask==2.3.2
Flask-Cors==3.0.10
pandas==2.0.3
scikit-learn==1.3.0
gspread==5.10.0
google-auth-oauthlib==1.0.0
requests==2.31.0
numpy==1.24.3
📄 Google Sheets API Setup
Enable APIs: Enable Google Sheets API and Google Drive API in Google Cloud Console.
Create Service Account: Go to IAM & Admin > Service Accounts → Create new → Add a JSON key.
Rename JSON key file to credentials.json and place it in the project root.
Share your Google Sheet with the email from client_email in credentials.json.
📬 Telegram Bot Setup
Talk to @BotFather on Telegram and create a new bot. Save the token.
Send any message to your new bot.
Hit this URL in a browser to get the chat_id:
bash

Collapse

Wrap

Run

Copy
https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
🔑 Alpha Vantage API Key
Register at Alpha Vantage and get your free API key.

🔧 Configure Settings
Update your keys and IDs in:

backend/config.py

python

Collapse

Wrap

Run

Copy
ALPHA_VANTAGE_API_KEY = "your_api_key"
SHEET_ID = "your_google_sheet_id"
TELEGRAM_TOKEN = "your_bot_token"
TELEGRAM_CHAT_ID = "your_chat_id"

import os
CREDENTIALS_PATH = os.path.join(BASE_DIR, '..', 'credentials.json')
▶️ Running the App
Start the Flask backend:

bash

Collapse

Wrap

Run

Copy
cd backend
python app.py
Then open your browser and go to:

http://localhost:5000

🧭 Dashboard Features
🏁 Run Backtest: Simulates trades and computes metrics.
🔄 Refresh Signals: Gets the latest ML-predicted signal.
📈 Performance Summary: Aggregated stats like:
Total PNL
Average Win Ratio
ML Accuracy
Total Trades
📂 Project Structure
bash

Collapse

Wrap

Run

Copy
algo_trading_project/
├── backend/
│   ├── app.py              # Flask server
│   ├── config.py           # API keys & config
│   ├── data_ingestion.py   # Stock data fetch
│   ├── main.py             # Backtesting logic
│   ├── ml_model.py         # ML training and prediction
│   ├── sheet_logger.py     # Google Sheets integration
│   ├── strategy.py         # Signal generation
│   └── telegram_alert.py   # Telegram alert system
├── templates/
│   └── index.html          # Frontend template
├── credentials.json        # Google auth file
└── README.md               # This file
💡 Future Enhancements
🔄 Real-time stock data feed
💼 Portfolio & risk management
🧠 Deep learning (LSTM, Transformers)
🗃 Database (PostgreSQL, SQLite)
📊 Charts (Chart.js, D3.js)
🔐 User authentication
📄 License
This project is licensed under the MIT License.

Made with 💡 and 📈 by passionate developers.
