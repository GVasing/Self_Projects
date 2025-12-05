from init import db

class InProgress(db.Model):
    __tablename__ = "in_progress"

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), nullable=False)