from api import db
from api.helpers import common_helper

time_now = common_helper.get_current_utc_timestamp()


class TimestampMixin:
    created_on = db.Column(db.DateTime(timezone=True), default=time_now, nullable=False)
    updated_on = db.Column(
        db.DateTime(timezone=True),
        onupdate=time_now,
        default=time_now,
        nullable=False,
    )
