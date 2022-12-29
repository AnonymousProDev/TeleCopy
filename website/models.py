from . import db
from sqlalchemy.sql import func

class Tele(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(100))
    token = db.Column(db.String(100))
    iid = db.Column(db.String(100))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    