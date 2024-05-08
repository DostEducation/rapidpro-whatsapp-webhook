from datetime import date
from flask_sqlalchemy.query import Query as BaseQuery
from sqlalchemy import desc, func

from api import db
from api.mixins import TimestampMixin


class UserActivitiesQuery(BaseQuery):
    def get_todays_started_activity_for_user(self, user_id, user_phone):
        return (
            self.filter(
                UserActivities.user_id == user_id,
                UserActivities.user_phone == user_phone,
                UserActivities.is_started.is_(True),
                func.DATE(UserActivities.started_on) == date.today(),
            )
            .order_by(desc("started_on"))
            .first()
        )

    def get_todays_succeeded_activity_for_user(self, user_id, user_phone):
        return (
            self.filter(
                UserActivities.user_id == user_id,
                UserActivities.user_phone == user_phone,
                UserActivities.is_succeeded.is_(True),
                func.DATE(UserActivities.succeeded_on) == date.today(),
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
    is_started = db.Column(db.Boolean)
    started_on = db.Column(db.DateTime(timezone=True))
    is_succeeded = db.Column(db.Boolean)
    succeeded_on = db.Column(db.DateTime(timezone=True))
    is_completed = db.Column(db.Boolean)
    completed_on = db.Column(db.DateTime(timezone=True))
