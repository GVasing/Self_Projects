from init import db

class ToDo(db.Model):
    __tablename__ = "to_do"

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), nullable=False)

    