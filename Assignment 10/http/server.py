from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Flask Server Running"

@app.route('/temperature', methods=['POST'])
def temperature():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON received"}), 400

    temp = data.get("temperature")
    hum  = data.get("humidity")

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"[{time}] Temp: {temp} °C | Humidity: {hum} %")

    return jsonify({"status": "success"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)
