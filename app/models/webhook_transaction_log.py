from pydantic import BaseModel
from sqlalchemy import Boolean, Column, Integer, Text

from app import TimestampMixin
from app.models.base import Base


class WebhookTransactionLog(Base):
    __tablename__ = "webhook_transaction_log"

    id = Column(Integer, primary_key=True)
    payload = Column(Text)
    processed = Column(Boolean, nullable=False)
    attempts = Column(Integer, nullable=False, default=0)


class WebhookTransactionLogSchema(BaseModel):
    payload: str
    processed: bool
    attempts: int
    timestamps: TimestampMixin

    class Config:
        orm_mode = True
