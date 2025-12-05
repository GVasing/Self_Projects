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
    
# GET /id
@to_do_bp.route("/<int:to_do_id>")
def get_a_to_do_item(to_do_id):
    # Define GET statment
    stmt = db.select(ToDo).where(ToDo.id == to_do_id)

    # Execute it
    to_do = db.session.scalar(stmt)

    # Error Handling
    if to_do:
        # Serialise
        data = ToDo_schema.dump(to_do)
        # Return data
        return jsonify(data)
    else:
        return {"message":f"To Do Item with id {to_do_id} not found."}, 404
    
# POST /
@to_do_bp.route("/", methods=["POST"])
def create_to_do_item():
    try:
        # GET info from the request body
        body_data = request.get_json()
        
        new_to_do_item = ToDo_schema.load(
            body_data,
            session=db.session
        )
        # Add new airline data to session
        db.session.add(new_to_do_item)
        # Commit the session
        db.session.commit()
        # Return
        return jsonify(ToDo_schema.dump(new_to_do_item)), 201
    except ValueError as err:
        return {"message": "Invalid format given"}, 400
        
# PUT/PATCH /id
@to_do_bp.route("/<int:to_do_id>", methods=["PUT", "PATCH"])
def update_to_do_item(to_do_id):
    try:
        # Define GET Statement
        stmt = db.select(ToDo).where(ToDo.id == to_do_id)

        # Execute statement
        to_do = db.session.scalar(stmt)

        if not to_do:
            return {"message": f"To Do Item with id {to_do_id} does not exist/cannot be found."}, 404

        body_data = request.get_json()

        updated_to_do_item = ToDo_schema.load(
            body_data,
            instance=to_do,
            partial=True,
            session=db.session
        )

        # Commit changes
        db.session.commit()
        # Return data
        return jsonify(ToDo_schema.dump(updated_to_do_item))

    except ValueError as err:
        return {"message": "Invalid format given, no data or non-positive integer provided."}, 400

# DELETE /id
@to_do_bp.route("/<int:to_do_id>", methods=["DELETE"])
def delete_to_item(to_do_id):
    # Find the airline with the airline_id
    stmt = db.select(ToDo).where(ToDo.id == to_do_id)
    to_do = db.session.scalar(stmt)
    # if exists
    if to_do:
        # delete the airline entry
        db.session.delete(to_do)
        db.session.commit()

        return {"message": f"To Do Item '{to_do.item_name}' has been removed successfully."}, 200
    # else:
    else:
        # return an acknowledgement message
        return {"message": f"To Do Item with id '{to_do_id}' does not exist"}, 404