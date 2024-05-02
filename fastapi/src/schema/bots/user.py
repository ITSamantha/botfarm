import datetime
import uuid
from typing import Optional

from pydantic import BaseModel

from src.schema.bots.project import ResponseProject


class ResponseUser(BaseModel):
    id: str
    login: str

    project: ResponseProject

    env: Env
    domain: UserDomain

    locktime: Optional[datetime.datetime]

    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: Optional[datetime.datetime]


class User(ResponseUser):
    password: str


class CreateUser(BaseModel):
    login: str
    password: str

    project_id: str

    env: Env
    domain: UserDomain


class UpdateUser(BaseModel):
    # TODO: OPTIONAL
    login: Optional[str] = None
    project_id: Optional[uuid.UUID] = None

    env: Optional[Env] = None
    domain: Optional[UserDomain] = None


class UserDomain(BaseModel):
    id: int
    title: str
