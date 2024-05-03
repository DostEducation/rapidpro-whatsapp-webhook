from flask_sqlalchemy.query import Query as BaseQuery
from sqlalchemy import desc

from api import db
from api.mixins import TimestampMixin


class UserActivitiesQuery(BaseQuery):
    def get_started_activity_for_user(self, user_id, user_phone, user_flow_id):
        return (
            self.filter_by(
                user_id=user_id,
                user_phone=user_phone,
                user_flow_id=user_flow_id,
                is_started=True,
            )
            .order_by(desc("started_on"))
            .first()
        )

    def get_succeeded_activity_for_user(self, user_id, user_phone, user_flow_id):
        return (
            self.filter_by(
                user_id=user_id,
                user_phone=user_phone,
                user_flow_id=user_flow_id,
                is_succeeded=True,
            )
            .order_by(desc("succeeded_on"))
            .first()
        )


class UserActivities(TimestampMixin, db.Model):
    query_class = UserActivitiesQuery

    __tablename__ = "user_activities"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user_phone = db.Column(db.BigInteger, nullable=False, index=True)
    user_flow_id = db.Column(db.Integer, db.ForeignKey("user_flows.id"))
    activity = db.Column(db.String(500))
    is_started = db.Column(db.Boolean, default=False, nullable=False)
    started_on = db.Column(db.DateTime)
    is_succeeded = db.Column(db.Boolean, default=False, nullable=False)
    succeeded_on = db.Column(db.DateTime)
    is_completed = db.Column(db.Boolean, default=False, nullable=False)
    completed_on = db.Column(db.DateTime)
