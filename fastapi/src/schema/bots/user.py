import datetime
from typing import Optional

from pydantic import BaseModel


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


class CreateUser(BaseModel):
    pass
