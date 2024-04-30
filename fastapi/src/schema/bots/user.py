import datetime
import uuid
from typing import Optional

from pydantic import BaseModel

from src.schema.bots.project import ResponseProject


class User(BaseModel):
    id: str
    login: str
    password: str

    project_id: str

    env: str
    domain: str

    locktime: Optional[datetime.datetime]

    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: Optional[datetime.datetime]


class ResponseUser(BaseModel):
    id: str
    login: str

    project: ResponseProject

    env: str
    domain: str
    locktime: Optional[datetime.datetime]

    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: Optional[datetime.datetime]


class CreateUser(BaseModel):
    login: str
    password: str

    project_id: str

    env: str
    domain: str


class UpdateUser(BaseModel):
    login: str
    project_id: str

    env: str
    domain: str
