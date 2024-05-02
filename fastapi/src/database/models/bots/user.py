import uuid
import datetime
from sqlalchemy import Enum, Integer
from typing import Optional

from sqlalchemy import UUID, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.base import Base
from src.database.models.core.env import Env


class UserDomain(Base):
    # CANARY = (1, 'canary')
    # REGULAR = (2, 'regular')
    CANARY = 1
    REGULAR = 2

    __tablename__ = "user_domains"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title: Mapped[str] = mapped_column(String(32), nullable=False, unique=True)


class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    login: Mapped[str] = mapped_column(String(128), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String, nullable=True)

    project_id: Mapped[UUID] = mapped_column(ForeignKey("projects.id"), nullable=False)

    env_id: Mapped[int] = mapped_column(ForeignKey("envs.id"), nullable=False)
    env: Mapped[Env] = relationship(uselist=False, lazy="joined")

    domain_id = mapped_column(ForeignKey("user_domains.id"), nullable=False)
    domain: Mapped[UserDomain] = relationship(uselist=False, lazy="joined")

    locktime: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP, nullable=True, default=None)

    created_at: Mapped[datetime.datetime] = mapped_column(nullable=False, default=datetime.datetime.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(nullable=False, default=datetime.datetime.now(),
                                                          onupdate=datetime.datetime.now())
    deleted_at: Mapped[Optional[datetime.datetime]] = mapped_column(nullable=True)
