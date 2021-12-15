from datetime import datetime

from pydantic import BaseModel, Field


class NewRegister(BaseModel):
    application: str = Field(...)
    code: int = Field(...)
    message: str = Field(...)
    date: datetime = Field(...)
