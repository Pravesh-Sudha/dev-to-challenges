from flask import Flask, request, jsonify
from flask_cors import CORS
import uuid

app = Flask(__name__)
CORS(app)

transactions = {}

@app.route("/midnight/tx", methods=["POST"])
def send_tx():
    tx = request.json
    tx_hash = str(uuid.uuid4())
    transactions[tx_hash] = {"status": "pending", "payload": tx}
    return jsonify({"tx_hash": tx_hash})

@app.route("/midnight/tx/<tx_hash>", methods=["GET"])
def get_tx(tx_hash):
    tx = transactions.get(tx_hash)
    if not tx:
        return jsonify({"error": "not found"}), 404
    tx["status"] = "confirmed"  # auto-confirm for mock
    return jsonify(tx)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
