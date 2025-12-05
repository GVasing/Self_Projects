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
        return {"message": "No 'Completed' items found"}, 404
    
# GET /id
@completed_bp.route("/<int:completed_id>")
def get_a_completed_item(completed_id):
    # Define GET statment
    stmt = db.select(Completed).where(Completed.id == completed_id)

    # Execute it
    completed = db.session.scalar(stmt)

    # Error Handling
    if completed:
        # Serialise
        data = Completed_schema.dump(completed)
        # Return data
        return jsonify(data)
    else:
        return {"message":f"Completed Item with id {completed_id} not found."}, 404
    
# POST /
@completed_bp.route("/", methods=["POST"])
def create_completed_item():
    try:
        # GET info from the request body
        body_data = request.get_json()
        
        new_completed_item = Completed_schema.load(
            body_data,
            session=db.session
        )
        # Add new completed data to session
        db.session.add(new_completed_item)
        # Commit the session
        db.session.commit()
        # Return
        return jsonify(Completed_schema.dump(new_completed_item)), 201
    except ValueError as err:
        return {"message": "Invalid format given"}, 400
        
# PUT/PATCH /id
@completed_bp.route("/<int:completed_id>", methods=["PUT", "PATCH"])
def update_completed_item(completed_id):
    try:
        # Define GET Statement
        stmt = db.select(Completed).where(Completed.id == completed_id)

        # Execute statement
        completed = db.session.scalar(stmt)

        if not completed:
            return {"message": f"Completed Item with id {completed_id} does not exist/cannot be found."}, 404

        body_data = request.get_json()

        updated_completed_item = Completed_schema.load(
            body_data,
            instance=completed,
            partial=True,
            session=db.session
        )

        # Commit changes
        db.session.commit()
        # Return data
        return jsonify(Completed_schema.dump(updated_completed_item))

    except ValueError as err:
        return {"message": "Invalid format given, no data or non-positive integer provided."}, 400

# DELETE /id
@completed_bp.route("/<int:completed_id>", methods=["DELETE"])
def delete_to_item(completed_id):
    # Find the completed with the completed_id
    stmt = db.select(Completed).where(Completed.id == completed_id)
    completed = db.session.scalar(stmt)
    # if exists
    if completed:
        # delete the completed entry
        db.session.delete(completed)
        db.session.commit()

        return {"message": f"Completed Item '{completed.item_name}' has been removed successfully."}, 200
    # else:
    else:
        # return an acknowledgement message
        return {"message": f"Completed Item with id '{completed_id}' does not exist"}, 404