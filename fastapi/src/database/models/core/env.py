from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import Base


class Env(Base):
    PROD = 1
    PREPROD = 2
    STAGE = 3

    __tablename__ = "envs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title: Mapped[str] = mapped_column(String(32), nullable=False, unique=True)
