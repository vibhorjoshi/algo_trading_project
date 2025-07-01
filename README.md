# algo_trading_project

📈 ML-Powered Algorithmic Trading System
This project presents a comprehensive algorithmic trading system featuring backtesting capabilities, live trading signal generation (simulated), and performance monitoring, all powered by machine learning and integrated with Google Sheets and Telegram for logging and alerts.

✨ Features
Advanced Backtesting Engine: Test your trading strategies against historical data with detailed performance metrics.

Machine Learning Integration: Utilizes a Decision Tree classifier to predict price movements, enhancing signal generation.

Technical Analysis: Incorporates popular indicators like RSI and Moving Averages for robust signal generation.

Google Sheets Logging: Automatically logs all trades and summarizes backtest performance directly to a Google Sheet.

Telegram Alerts: Receive real-time notifications on backtest completion and critical system errors.

Interactive Web Dashboard: A user-friendly Flask-based frontend for controlling backtests, viewing live signals, and monitoring overall performance.

Modular Backend: Cleanly separated modules for data ingestion, strategy, ML model, logging, and alerts.

API Endpoints: Exposes RESTful APIs for backtest control, status, results, live signals, and performance metrics, allowing for programmatic interaction.

🚀 Screenshots
Live Trading Dashboard - Backtest Control
The main dashboard provides controls to initiate backtests and view the results for various stocks, including Profit & Loss (PNL), Win Ratio, and ML Accuracy.

(Replace this placeholder with Screenshot 2025-07-01 221307.jpg)

Live Trading Signals & Performance Overview
Monitor simulated live trading signals and get an immediate overview of the system's performance, including Total PNL, Average Win Ratio, ML Accuracy, and Total Trades.

(Replace this placeholder with Screenshot 2025-07-01 221909.png)

API Performance Metrics (JSON Output)
The backend exposes API endpoints to retrieve detailed performance metrics in JSON format, useful for external integrations or further analysis.

(Replace this placeholder with Screenshot 2025-07-01 223036.png)

🛠️ Technologies Used
Python 3.x

Flask: Web framework for the backend API and serving the frontend.

Pandas: Data manipulation and analysis.

Scikit-learn: Machine learning functionalities (Decision Tree Classifier).

gspread: Python API for Google Sheets.

google-auth-oauthlib: Google authentication for service accounts.

Requests: HTTP library for API interactions (Alpha Vantage, Telegram).

Altair (for charts): Although not directly in the project code, used for generating the performance charts.

⚙️ Setup and Installation
Follow these steps to get the project up and running on your local machine.

1. Clone the Repository
git clone https://github.com/your-username/algo_trading_project.git
cd algo_trading_project

2. Create a Virtual Environment (Recommended)
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

(If you don't have a requirements.txt file, create one with the following content and then run pip install -r requirements.txt):

Flask==2.3.2
Flask-Cors==3.0.10
pandas==2.0.3
scikit-learn==1.3.0
gspread==5.10.0
google-auth-oauthlib==1.0.0
requests==2.31.0
numpy==1.24.3

4. Google Sheets API Setup
This project uses Google Sheets for logging trades and summaries.

Enable APIs: Go to the Google Cloud Console and create a new project (or select an existing one). Enable the Google Sheets API and Google Drive API for your project.

Create Service Account: Navigate to IAM & Admin > Service Accounts. Create a new service account.

Generate Key: After creating the service account, click on it, go to the Keys tab, and Add Key > Create new key. Choose JSON and download the credentials.json file.

Place Credentials File: Rename the downloaded file to credentials.json and place it in the root directory of your algo_trading_project (i.e., one level up from the backend folder).

Share Google Sheet: Create a new Google Sheet. Share this sheet with the client email of your service account (found in the credentials.json file under the client_email field).

5. Telegram Bot Setup
For receiving alerts:

Create a Bot: Open Telegram and search for @BotFather. Use the /newbot command to create a new bot. BotFather will give you a HTTP API Token.

Get Chat ID: Start a conversation with your new bot. Then, send a message to https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates (replace <YOUR_BOT_TOKEN> with your bot's token). Look for the chat object and find the id field – this is your TELEGRAM_CHAT_ID.

6. Alpha Vantage API Key
This project fetches stock data using Alpha Vantage.

Get API Key: Sign up for a free API key at Alpha Vantage.

7. Configure config.py
Open backend/config.py and update the following variables with your obtained keys and IDs:

# backend/config.py

# ... other imports and BASE_DIR ...

ALPHA_VANTAGE_API_KEY = "YOUR_ALPHA_VANTAGE_API_KEY" # <--- Update this
SHEET_ID = "YOUR_ACTUAL_GOOGLE_SHEET_ID"           # <--- Update this (from your Google Sheet URL)
TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"         # <--- Update this
TELEGRAM_CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"         # <--- Update this

# Ensure credentials.json is in the project root
CREDENTIALS_PATH = os.path.join(BASE_DIR, "..", "credentials.json")

▶️ Usage
Start the Flask Application:
Navigate to the backend directory in your terminal and run:

python app.py

You should see output indicating the Flask server is running, typically on http://localhost:5000.

Access the Web Dashboard:
Open your web browser and go to http://localhost:5000.

Interact with the Dashboard:

Backtest Control: Click "RUN BACKTEST" to initiate the backtesting process. The results (PNL, Win Ratio, ML Accuracy) for each configured stock will appear in the table. Use "REFRESH RESULTS" to update the display if the backtest is running in the background.

Live Trading Signals: Click "REFRESH SIGNALS" to see simulated live trading signals based on the latest available data or backtest results.

Performance Overview: This section automatically updates to show aggregated performance metrics from the completed backtests.

📂 Project Structure
algo_trading_project/
├── backend/
│   ├── app.py              # Flask application, API endpoints
│   ├── config.py           # Configuration settings (API keys, sheet ID, etc.)
│   ├── data_ingestion.py   # Handles fetching historical stock data
│   ├── main.py             # Main backtesting logic, orchestrates modules
│   ├── ml_model.py         # Machine learning model for signal prediction
│   ├── sheet_logger.py     # Functions for interacting with Google Sheets
│   ├── strategy.py         # Defines trading strategy and technical indicators
│   └── telegram_alert.py   # Sends alerts via Telegram
├── templates/
│   └── index.html          # Frontend HTML for the dashboard
├── credentials.json        # Google Service Account credentials (downloaded)
└── README.md               # This file

💡 Future Enhancements
Real-time Data Integration: Connect to a live data feed for actual real-time trading signals.

More Sophisticated Strategies: Implement additional trading strategies and indicators.

Portfolio Management: Add features for managing a virtual portfolio, including risk management.

Database Integration: Use a database (e.g., SQLite, PostgreSQL) for persistent storage of historical data, trades, and performance metrics instead of relying solely on Google Sheets.

Improved ML Models: Experiment with more advanced machine learning models (e.g., LSTMs, Transformers) or deep learning approaches.

Frontend Enhancements: Add interactive charts (e.g., using Chart.js, D3.js) for better visualization of stock performance and signals.

User Authentication: Implement user login for multi-user access.

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.
