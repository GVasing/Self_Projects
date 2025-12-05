# Installed imports
from flask import Blueprint
from sqlalchemy import text

# Created module imports
from init import db
from models.to_do import ToDo
from models.in_progress import InProgress
from models.completed import Completed

# Define create a blueprint for 'app'
db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_tables():
    db.create_all()
    print("Tables created.")

@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()
    print("Tables dropped.")

@db_commands.cli.command("seed")
def seed_tables():

    # Create 'ToDo' secton items
    to_do_items = [
        ToDo(
            item_name = "testOne"
        ),
        ToDo(
            item_name = "testTwo"
        ),
        ToDo(
            item_name = "testThree"
        )
    ]

    # Add to session
    db.session.add_all(to_do_items)

    # Create 'InProgress' section items
    in_progress_items = [
        InProgress(
            item_name = "testingOne"
        ),
        InProgress(
            item_name = "testingTwo"
        ),
        InProgress(
            item_name = "testingThree"
        )
    ]

    # Add to session
    db.session.add_all(in_progress_items)

    # Create 'Completed' section items
    completed_items = [
        Completed(
            item_name = "testedOne"
        ),
        Completed(
            item_name = "testedTwo"
        ),
        Completed(
            item_name = "testedThree"
        )
    ]

    # Add to session
    db.session.add_all(completed_items)

    # Commit session here
    db.session.commit()

    print("Tables seeded.")