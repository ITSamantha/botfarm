import datetime
import uuid
from typing import Optional

from pydantic import BaseModel, EmailStr

from src.schema.bots.project import ResponseProject
from src.schema.core import Env


class UserDomain(BaseModel):
    id: int
    title: str


class ResponseUser(BaseModel):
    id: uuid.UUID
    login: EmailStr

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
    login: EmailStr
    password: str

    project_id: uuid.UUID

    env_id: int
    domain_id: int


class LockUser(BaseModel):
    id: uuid.UUID
    locktime: Optional[datetime.datetime]


class UpdateUser(BaseModel):
    login: Optional[str] = None
    project_id: Optional[uuid.UUID] = None

    env: Optional[Env] = None
    domain: Optional[UserDomain] = None

    locktime: Optional[datetime.datetime] = None
