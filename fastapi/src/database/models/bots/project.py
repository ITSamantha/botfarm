import datetime
import uuid
from typing import Optional

from sqlalchemy import UUID, String
from sqlalchemy.orm import mapped_column, Mapped

from src.database.models.base import Base


class Project(Base):
    """Model to store user projects."""

    __tablename__ = "projects"

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    title: Mapped[str] = mapped_column(String(256), nullable=False, unique=True)

    created_at: Mapped[datetime.datetime] = mapped_column(nullable=False, default=datetime.datetime.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(nullable=False, default=datetime.datetime.now(),
                                                          onupdate=datetime.datetime.now())
    deleted_at: Mapped[Optional[datetime.datetime]] = mapped_column(nullable=True)
