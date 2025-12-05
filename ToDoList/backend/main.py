# Built in imports
import os

# Installed imports
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv # This allows 'main.py' to read the contents of the .env file

# Created module imports
from database.db import get_db_connection

# Initialise flask app
app = Flask(__name__)

# Enable CORS to allow frontend to communicate with backend
CORS (app)

@app.route("/")
def home():
    return jsonify({
        "message": "Flask app works"
    })

@app.route("/api-test")
def endpoint_test():
    return jsonify({
        "message": "Endpoint test works"
    })

@app.route("/db_connection")
def db_connection_test():
    conn = get_db_connection()

    if conn:
        # conn.close()
        return jsonify({
            "message": "database connected"
        })
    else:
        return jsonify({
            "message": "database connection failed"
        }), 500

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',  # Makes it accessible from your frontend
        port=5500,
        debug=True
    )