from pydantic import BaseModel


class Env(BaseModel):
    id: int
    title: str
