# Installed imports
from flask import Blueprint, jsonify, request

# Created Module Imports
from init import db
from models.completed import Completed
from schemas.schemas import Completed_schema, Completeds_schema

# Define blueprint for completed
completed_bp = Blueprint("completed", __name__, url_prefix="/completeds")

# Routes
# GET
@completed_bp.route("/")
def get_completeds():
    
    # Define GET Statement
    stmt = db.select(Completed)
    # Execute it
    completed_list = db.session.scalars(stmt)
    # Serialise it
    data = Completeds_schema.dump(completed_list)
    # Error handling and Return
    if data:
        return jsonify(data)
    else:
        return {"message": "No 'ToDo' items found"}, 404