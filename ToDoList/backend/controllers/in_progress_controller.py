# Installed imports
from flask import Blueprint, jsonify, request

# Created Module Imports
from init import db
from models.in_progress import InProgress
from schemas.schemas import InProgress_schema, InProgresses_schema

# Define blueprint for in_progress
in_progress_bp = Blueprint("in_progress", __name__, url_prefix="/in_progresses")

# Routes
# GET
@in_progress_bp.route("/")
def get_in_progresss():
    
    # Define GET Statement
    stmt = db.select(InProgress)
    # Execute it
    in_progress_list = db.session.scalars(stmt)
    # Serialise it
    data = InProgresses_schema.dump(in_progress_list)
    # Error handling and Return
    if data:
        return jsonify(data)
    else:
        return {"message": "No 'ToDo' items found"}, 404