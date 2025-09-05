from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route("/midnight/balance/<address>", methods=["GET"])
def get_balance(address):
    return jsonify({"address": address, "balance": random.randint(100, 1000)})

@app.route("/midnight/history/<address>", methods=["GET"])
def get_history(address):
    return jsonify({
        "address": address,
        "history": [
            {"tx_hash": "abc123", "amount": 50, "type": "send"},
            {"tx_hash": "xyz456", "amount": 20, "type": "receive"}
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
