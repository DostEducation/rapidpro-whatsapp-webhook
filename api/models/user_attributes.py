from api import db
from api.mixins import TimestampMixin


class UserAttributes(TimestampMixin, db.Model):

    __tablename__ = "user_attributes"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user_phone = db.Column(db.String(50), nullable=False)
    field_name = db.Column(db.String(255))
    field_value = db.Column(db.String(255))
