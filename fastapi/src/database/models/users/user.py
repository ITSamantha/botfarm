import uuid

from sqlalchemy import UUID
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)


