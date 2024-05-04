import random
from typing import List

from faker import Faker
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import models
from src.database.models.bots.user import UserDomain
from src.database.models.core.env import Env
from src.database.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.database.session_manager import db_manager
from src.schema.bots.user import CreateUser
from src.util.crypt import Crypt


class DataGenerator:
    """Class to generate different types of data."""

    @staticmethod
    async def generate_user(session: AsyncSession) -> tuple[CreateUser, str]:
        """Returns user and password with generated random data."""

        fake: Faker = Faker()

        email: str = fake.free_email()
        crypt = Crypt()

        password: str = fake.password(length=12)
        hashed_password: str = crypt.hash(password)

        projects: List[models.Project] = await SqlAlchemyRepository(session,
                                                                    model=models.Project).get_multi(deleted_at=None)

        project: models.Project = random.choice(projects)

        env_id = random.choice([value for name, value in vars(Env).items() if isinstance(value, int)])
        domain_id = random.choice([value for name, value in vars(UserDomain).items() if isinstance(value, int)])

        user = CreateUser(login=email, password=hashed_password, project_id=project.id, env_id=env_id,
                          domain_id=domain_id)

        return user, password
