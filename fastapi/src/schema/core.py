import datetime
from typing import Optional

from pydantic import BaseModel


class DeleteSchema(BaseModel):
    deleted_at: Optional[datetime.datetime]


class Env(BaseModel):
    id: int
    title: str
