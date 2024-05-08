from api import db
from api.helpers import common_helper

ist_now = common_helper.get_current_utc_timestamp()


class TimestampMixin:
    created_on = db.Column(db.DateTime(timezone=True), default=ist_now, nullable=False)
    updated_on = db.Column(
        db.DateTime(timezone=True),
        onupdate=ist_now,
        default=ist_now,
        nullable=False,
    )
