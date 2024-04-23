from api import db
from api.mixins import TimestampMixin


class UserActivities(TimestampMixin, db.Model):

    __tablename__ = "user_activities"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user_flow_id = db.Column(db.Integer, db.ForeignKey("user_flows.id"))
    activity = db.Column(db.String(500))
    is_started = db.Column(db.Boolean, default=False, nullable=False)
    started_on = db.Column(db.DateTime)
    is_succeeded = db.Column(db.Boolean, default=False, nullable=False)
    succeeded_on = db.Column(db.DateTime)
    is_completed = db.Column(db.Boolean, default=False, nullable=False)
    completed_on = db.Column(db.DateTime)
