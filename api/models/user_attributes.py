from flask_sqlalchemy.query import Query as BaseQuery

from api import db
from api.mixins import TimestampMixin


class UserAttributesQuery(BaseQuery):
    def get_existing_user_attributes(self, user_id):
        user_attributes = self.filter(
            UserAttributes.user_id == user_id,
        ).all()
        return {attribute.field_name: attribute for attribute in user_attributes}


class UserAttributes(TimestampMixin, db.Model):
    query_class = UserAttributesQuery

    __tablename__ = "user_attributes"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user_phone = db.Column(db.BigInteger, nullable=False, index=True)
    field_name = db.Column(db.String(255))
    field_value = db.Column(db.String(255))
