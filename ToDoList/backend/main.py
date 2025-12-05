# Built in imports
import os

# Installed imports
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv # This allows 'main.py' to read the contents of the .env file

# Created module imports
# from database.db import get_db_connection
from init import db
from controllers.cli_controller import db_commands

# Load .env variables into application environment
load_dotenv()

def create_app():

    # Initialise flask app
    app = Flask(__name__)

    # Configure database connection using environment variable
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI")

    # Enable CORS to allow frontend to communicate with backend
    CORS (app)

    # Initialise SQLAlchemy Database
    db.init_app(app)

    # Disable automatic sorting of JSON responses
    app.json.sort_keys = False

    # Register blueprints
    app.register_blueprint(db_commands)

    # Return configured app instance
    return app