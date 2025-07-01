# app.py
from flask import Flask, render_template, jsonify
import threading
import time
import os
from backend.main import main as run_backtest  # Import the backtest function

app = Flask(__name__)

# Global status tracking
backtest_status = {
    "running": False,
    "progress": 0,
    "message": "Ready to start",
    "results": []
}

@app.route("/")
def index():
    return render_template("index.html")

def run_backtest_thread():
    try:
        backtest_status["running"] = True
        backtest_status["progress"] = 0
        backtest_status["message"] = "Starting backtest..."
        backtest_status["results"] = []
        
        # Run the backtest
        results = run_backtest()
        if results is None or not isinstance(results, (list, tuple)):
            results = []
        
        # Format results for frontend
        formatted_results = []
        if all(isinstance(item, (list, tuple)) and len(item) == 4 for item in results):
            for symbol, pnl, win_ratio, accuracy in results:
                formatted_results.append({
                    "symbol": symbol,
                    "pnl": pnl,
                    "win_ratio": win_ratio,
                    "accuracy": accuracy
                })
            backtest_status["message"] = "Backtest completed successfully!"
        else:
            backtest_status["message"] = "No results returned from backtest."
            results = []
        
        backtest_status["results"] = formatted_results
        
    except Exception as e:
        backtest_status["message"] = f"System error: {str(e)}"
    finally:
        backtest_status["running"] = False
        backtest_status["progress"] = 100

@app.route("/run-backtest", methods=["POST"])
def start_backtest():
    if backtest_status["running"]:
        return jsonify({"success": False, "error": "Backtest already running"})
    
    # Start backtest in a separate thread
    threading.Thread(target=run_backtest_thread).start()
    return jsonify({"success": True, "message": "Backtest started"})

@app.route("/backtest-status")
def get_backtest_status():
    return jsonify(backtest_status)

@app.route("/get-results")
def get_results():
    return jsonify(backtest_status["results"])

if __name__ == "__main__":
    app.run(debug=True, port=5000)