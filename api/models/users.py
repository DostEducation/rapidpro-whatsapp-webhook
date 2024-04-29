from flask_sqlalchemy.query import Query as BaseQuery

from api import db
from api.mixins import TimestampMixin


class UserQuery(BaseQuery):
    def get_user_by_phone(self, user_phone):
        return self.filter(Users.phone == user_phone).first()


class Users(TimestampMixin, db.Model):
    query_class = UserQuery
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    glific_user_id = db.Column(db.Integer)
    phone = db.Column(db.BigInteger, nullable=False, index=True)
    name = db.Column(db.String(255))
    location = db.Column(db.String(255))
