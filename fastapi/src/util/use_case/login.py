from http import HTTPStatus

from fastapi import HTTPException

from src.database import models
from src.database.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.database.session_manager import db_manager
from src.config.jwt.config import settings_jwt
from src.schema.bots.auth import LoginUser
from src.util.crypt import Crypt
from src.util.jwt.jwt_auth import JWT


class LoginUseCase:
    @staticmethod
    async def login(data: LoginUser):
        user = await LoginUseCase.authenticate_user(data.login, data.password)

        if not user:
            raise HTTPException(detail="Incorrect username or password", status_code=HTTPStatus.BAD_REQUEST)

        jwt = JWT(settings_jwt)
        access_token = jwt.generate_access_token(data.login)

        return access_token

    @staticmethod
    async def authenticate_user(login: str, password: str):
        user: models.User = await SqlAlchemyRepository(db_manager.get_session, models.User).get_single(login=login)

        if not user:
            return False
        crypt = Crypt()

        if not crypt.verify(password, user.password):
            return False

        return user
