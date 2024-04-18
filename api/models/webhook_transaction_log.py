from api import db
from api.mixins import TimestampMixin


class WebhookTransactionLog(TimestampMixin, db.Model):

    __tablename__ = "webhook_transaction_log"
    id = db.Column(db.Integer, primary_key=True)
    payload = db.Column(db.Text)
    processed = db.Column(db.Boolean, nullable=False)
    attempts = db.Column(db.Integer, nullable=False, default="0")
