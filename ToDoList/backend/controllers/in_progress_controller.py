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
        return {"message": "No 'InProgress' items found"}, 404
    
# GET /id
@in_progress_bp.route("/<int:in_progress_id>")
def get_an_in_progress_item(in_progress_id):
    # Define GET statment
    stmt = db.select(InProgress).where(InProgress.id == in_progress_id)

    # Execute it
    in_progress = db.session.scalar(stmt)

    # Error Handling
    if in_progress:
        # Serialise
        data = InProgress_schema.dump(in_progress)
        # Return data
        return jsonify(data)
    else:
        return {"message":f"In Progress Item with id {in_progress_id} not found."}, 404
    
# POST /
@in_progress_bp.route("/", methods=["POST"])
def create_in_progress_item():
    try:
        # GET info from the request body
        body_data = request.get_json()
        
        new_in_progress_item = InProgress_schema.load(
            body_data,
            session=db.session
        )
        # Add new in progress data to session
        db.session.add(new_in_progress_item)
        # Commit the session
        db.session.commit()
        # Return
        return jsonify(InProgress_schema.dump(new_in_progress_item)), 201
    except ValueError as err:
        return {"message": "Invalid format given"}, 400
        
# PUT/PATCH /id
@in_progress_bp.route("/<int:in_progress_id>", methods=["PUT", "PATCH"])
def update_in_progress_item(in_progress_id):
    try:
        # Define GET Statement
        stmt = db.select(InProgress).where(InProgress.id == in_progress_id)

        # Execute statement
        in_progress = db.session.scalar(stmt)

        if not in_progress:
            return {"message": f"In Progress Item with id {in_progress_id} does not exist/cannot be found."}, 404

        body_data = request.get_json()

        updated_in_progress_item = InProgress_schema.load(
            body_data,
            instance=in_progress,
            partial=True,
            session=db.session
        )

        # Commit changes
        db.session.commit()
        # Return data
        return jsonify(InProgress_schema.dump(updated_in_progress_item))

    except ValueError as err:
        return {"message": "Invalid format given, no data or non-positive integer provided."}, 400

# DELETE /id
@in_progress_bp.route("/<int:in_progress_id>", methods=["DELETE"])
def delete_to_item(in_progress_id):
    # Find the in progress with the in progress_id
    stmt = db.select(InProgress).where(InProgress.id == in_progress_id)
    in_progress = db.session.scalar(stmt)
    # if exists
    if in_progress:
        # delete the in progress entry
        db.session.delete(in_progress)
        db.session.commit()

        return {"message": f"In Progress Item '{in_progress.item_name}' has been removed successfully."}, 200
    # else:
    else:
        # return an acknowledgement message
        return {"message": f"In Progress Item with id '{in_progress_id}' does not exist"}, 404