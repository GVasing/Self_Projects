# Installed imports
from flask import Blueprint, jsonify, request

# Created Module Imports
from init import db
from models.to_do import ToDo
from schemas.schemas import ToDo_schema, ToDos_schema

# Define blueprint for to_do
to_do_bp = Blueprint("to_do", __name__, url_prefix="/to_dos")

# Routes
# GET
@to_do_bp.route("/")
def get_to_dos():
    
    # Define GET Statement
    stmt = db.select(ToDo)
    # Execute it
    to_do_list = db.session.scalars(stmt)
    # Serialise it
    data = ToDos_schema.dump(to_do_list)
    # Error handling and Return
    if data:
        return jsonify(data)
    else:
        return {"message": "No 'ToDo' items found"}, 404