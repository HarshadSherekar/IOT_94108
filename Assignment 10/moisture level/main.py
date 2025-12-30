from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
from datetime import datetime
import paho.mqtt.client as mqtt

# ---------------- Configuration ----------------
MYSQL_CONFIG = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "root",
    "database": "moisture_level"
}

MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "farm/alerts/moisture"
MOISTURE_THRESHOLD = 30

# ---------------- Flask App ----------------
app = Flask(__name__)

# ---------------- MQTT Client Setup ----------------
mqtt_client = mqtt.Client()
try:
    mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
    mqtt_client.loop_start()
except Exception as e:
    print(f"[ERROR] MQTT connection failed: {e}")

# ---------------- Database Helper ----------------
def insert_soil_moisture(sensor_id, moisture_level):
    try:
        conn = mysql.connector.connect(**MYSQL_CONFIG)

        if not conn.is_connected():
            raise Exception("MySQL connection failed")

        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO moisture_data (sensor_id, moisture_level, date_time)
            VALUES (%s, %s, %s)
        """, (sensor_id, moisture_level, datetime.now()))

        conn.commit()
        cursor.close()
        conn.close()

    except Error as e:
        print(f"[DB ERROR] {e}")
        raise

# ---------------- Flask Route ----------------
@app.route("/moisture", methods=["POST"])
def receive_moisture():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "JSON body required"}), 400

        if "sensor_id" not in data or "moisture_level" not in data:
            return jsonify({"error": "sensor_id and moisture_level required"}), 400

        sensor_id = str(data["sensor_id"])

        try:
            moisture_level = float(data["moisture_level"])
        except ValueError:
            return jsonify({"error": "moisture_level must be numeric"}), 400

        # Store in MySQL
        insert_soil_moisture(sensor_id, moisture_level)

        # MQTT Alert
        alert_msg = None
        if moisture_level < MOISTURE_THRESHOLD:
            alert_msg = f"ALERT: Sensor {sensor_id} moisture low ({moisture_level}%)"
            mqtt_client.publish(MQTT_TOPIC, alert_msg)

        return jsonify({
            "status": "stored",
            "alert": alert_msg
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------- Main ----------------
if __name__ == "__main__":
    # Ensure table exists (testing only)
    try:
        conn = mysql.connector.connect(**MYSQL_CONFIG)

        if not conn.is_connected():
            raise Exception("MySQL connection failed")

        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS moisture_data (
                id INT AUTO_INCREMENT PRIMARY KEY,
                sensor_id VARCHAR(50) NOT NULL,
                moisture_level FLOAT NOT NULL,
                date_time DATETIME NOT NULL
            )
        """)

        conn.commit()
        cursor.close()
        conn.close()
        print("[INFO] Database moisture_level and table moisture_data ready")

    except Error as e:
        print(f"[DB INIT ERROR] {e}")

    app.run(host="0.0.0.0", port=5000, debug=True)
