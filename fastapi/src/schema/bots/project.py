import datetime
import uuid
from typing import Optional

from pydantic import BaseModel


class Project(BaseModel):
    id: uuid.UUID
    title: str

    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: Optional[datetime.datetime]


class ResponseProject(Project):
    pass


class CreateProject(BaseModel):
    title: str


class UpdateProject(BaseModel):
    title: str
