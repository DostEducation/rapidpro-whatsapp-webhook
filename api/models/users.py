from api import db
from api.mixins import TimestampMixin


class Users(TimestampMixin, db.Model):

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    glific_user_id = db.Column(db.Integer)
    phone = db.Column(db.Integer, nullable=False, index=True)
    name = db.Column(db.String(255))
    location = db.Column(db.String(255))
