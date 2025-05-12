from flask import Flask, request, jsonify
import os
import json
from datetime import datetime

app = Flask(__name__)

# Kansio datalle
DATA_DIR = "live_data"
os.makedirs(DATA_DIR, exist_ok=True)

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.json
        timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
        tf = data.get("timeframe", "1min")

        filename = f"{DATA_DIR}/live_{tf}_{timestamp}.json"
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)

        return jsonify({"status": "success", "message": f"Data saved to {filename}"}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/", methods=["GET"])
def home():
    return "Rahapaja webhook on käynnissä.", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

