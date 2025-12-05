# Installed imports
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow.validate import OneOf
from marshmallow import validates, ValidationError, fields

# Created imports
from models.to_do import ToDo
from models.in_progress import InProgress
from models.completed import Completed

class ToDoSchema(SQLAlchemyAutoSchema):

    class Meta:
        model = ToDo
        load_instance = True
        ordered = True

class InProgressSchema(SQLAlchemyAutoSchema):

    class Meta:
        model = InProgress
        load_instance = True
        ordered = True

class CompletedSchema(SQLAlchemyAutoSchema):

    class Meta:
        model = Completed
        load_instance = True
        ordered = True

# ToDo Schema for converting a single entry
ToDo_schema = ToDoSchema()
# ToDo Schema for converting multiple entries
ToDos_schema = ToDoSchema(many=True)

# InProgress Schema for converting a single entry
InProgress_schema = InProgressSchema()
# InProgress Schema for converting multiple entries
InProgresses_schema = InProgressSchema(many=True)

# Completed Schema for converting a single entry
Completed_schema = CompletedSchema()
# Completed Schema for converting multiple entries
Completeds_schema = CompletedSchema(many=True)