from pydantic import BaseModel, Field
from datetime import datetime


class TimestampMixin(BaseModel):
    created_on: datetime = Field(default_factory=datetime.now)
    updated_on: datetime = Field(default_factory=datetime.now)

    class Config:
        orm_mode = True
