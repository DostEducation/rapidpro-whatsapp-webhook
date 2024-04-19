from api import db
from api.mixins import TimestampMixin


class UserActivities(TimestampMixin, db.Model):

    __tablename__ = "user_activities"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user_flow_id = db.Column(db.Integer, db.ForeignKey("user_flows.id"))
    activity = db.Column(db.String(500))
    started = db.Column(db.Boolean)
    started_on = db.Column(db.DateTime)
    succeeded = db.Column(db.Boolean)
    succeeded_on = db.Column(db.DateTime)
    completed = db.Column(db.Boolean)
    completed_on = db.Column(db.DateTime)
