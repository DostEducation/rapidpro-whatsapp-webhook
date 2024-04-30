from api import db
from api.mixins import TimestampMixin


class UserFlows(TimestampMixin, db.Model):

    __tablename__ = "user_flows"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user_phone = db.Column(db.BigInteger, nullable=False, index=True)
    flow_uuid = db.Column(db.String(255))
    flow_name = db.Column(db.String(255))
    flow_type = db.Column(db.String(255))
    flow_run_status = db.Column(db.String(255))
    flow_start_time = db.Column(db.DateTime)
    flow_end_time = db.Column(db.DateTime)
    is_active = db.Column(db.Boolean, default=False, nullable=False)
