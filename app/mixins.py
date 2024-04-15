from datetime import datetime

from pydantic import BaseModel, Field


class TimestampMixin(BaseModel):
    created_on: datetime = Field(default_factory=datetime.now)
    updated_on: datetime = Field(default_factory=datetime.now)

    class Config:
        orm_mode = True
