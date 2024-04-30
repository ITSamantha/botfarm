import uuid
import datetime
from typing import Optional

from sqlalchemy import UUID, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy_utils.types.choice import ChoiceType

from src.database.models.base import Base


class User(Base):

    ENV_CHOICES = [
        ('PROD', 'prod'),
        ('PREPROD', 'preprod'),
        ('STAGE', 'stage')
    ]

    DOMAIN_CHOICES = [
        ('CANARY', 'canary'),
        ('REGULAR', 'regular')
    ]

    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    login: Mapped[str] = mapped_column(String(128), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String, nullable=True)

    project_id: Mapped[UUID] = mapped_column(ForeignKey("projects.id"), nullable=False)

    env: Mapped[ChoiceType] = mapped_column(ChoiceType(ENV_CHOICES, impl=String(32)), nullable=False)
    domain: Mapped[ChoiceType] = mapped_column(ChoiceType(DOMAIN_CHOICES, impl=String(32)), nullable=False)

    locktime: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP, nullable=True, default=None)

    created_at: Mapped[datetime.datetime] = mapped_column(nullable=False, default=datetime.datetime.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(nullable=False, default=datetime.datetime.now(),
                                                          onupdate=datetime.datetime.now())
    deleted_at: Mapped[Optional[datetime.datetime]] = mapped_column(nullable=True)
