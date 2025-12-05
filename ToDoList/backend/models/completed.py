from init import db

class Completed(db.Model):
    __tablename__ = "completed"

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), nullable=False)