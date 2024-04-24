from __future__ import absolute_import

from datetime import datetime

from api import db


class TimestampMixin:
    created_on = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_on = db.Column(
        db.DateTime,
        onupdate=datetime.now,
        default=datetime.now,
        nullable=False,
    )
