from flask import Flask, jsonify
import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
app = Flask(__name__)


def load_data():
    with open(BASE_DIR / "data.json", "r", encoding="utf-8") as file:
        return json.load(file)


@app.get("/health")
def health():
    return jsonify({"status": "ok", "service": "aws-backend"})


@app.get("/api/dashboard")
def dashboard():
    return jsonify(load_data())


if __name__ == "__main__":
    with open(BASE_DIR / "config.json", "r", encoding="utf-8") as file:
        config = json.load(file)

    app.run(
        host=config.get("host", "0.0.0.0"),
        port=config.get("port", 5000),
        debug=config.get("debug", True),
    )
