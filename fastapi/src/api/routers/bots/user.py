import datetime
import uuid
from http import HTTPStatus
from typing import List, Optional

from fastapi import APIRouter, HTTPException

from src.api.routers.bots import auth
from src.database import models
from src.database.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.database.session_manager import db_manager
from src.schema.bots.user import ResponseUser, CreateUser, User, UpdateUser, LockUser
from src.schema.core import DeleteSchema
from src.util.crypt import Crypt
from src.util.datagen import DataGenerator
from src.util.decorator import exception_processing

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

router.include_router(auth.router)


@router.get(path="", response_model=List[ResponseUser])
@exception_processing
async def get_users():
    """Returns the list of users."""

    users: List[models.User] = await SqlAlchemyRepository(db_manager.get_session,
                                                          model=models.User).get_multi(deleted_at=None)
    return users


@router.get(path="/{user_id}", response_model=ResponseUser)
@exception_processing
async def get_user_by_id(user_id: uuid.UUID):
    """Returns the user with the given user_id."""

    user: models.User = await SqlAlchemyRepository(db_manager.get_session,
                                                   model=models.User).get_single(id=user_id)

    if not user:
        raise HTTPException(status_code=HTTPStatus.FORBIDDEN, detail="This user does not exist.")

    return user


@router.post(path="", response_model=User)
@exception_processing
async def create_user(autogenerate: bool = False, data: Optional[CreateUser] = None):
    """Returns created with the given data user."""

    if autogenerate:
        data, password = await DataGenerator.generate_user()
    else:
        password = data.password
        crypt = Crypt()
        data.password = crypt.hash(password)

    user: models.User = await SqlAlchemyRepository(db_manager.get_session,
                                                   model=models.User).create(data)

    user.password = password

    return user


@router.delete(path="/{user_id}", response_model=ResponseUser)
@exception_processing
async def delete_user(user_id: uuid.UUID):
    """Returns deleted user."""

    delete_schema: DeleteSchema = DeleteSchema(deleted_at=datetime.datetime.now())

    user: models.User = await SqlAlchemyRepository(db_manager.get_session, model=models.User) \
        .update(data=delete_schema,
                id=user_id)

    return user


@router.patch(path="/{user_id}/acquire_lock", response_model=LockUser)
@exception_processing
async def acquire_lock_user(user_id: uuid.UUID):
    """Returns locktime and user_id after user acquiring."""

    user_repo: SqlAlchemyRepository = SqlAlchemyRepository(db_manager.get_session, model=models.User)

    user: models.User = await user_repo.get_single(id=user_id)

    if user.deleted_at:
        raise HTTPException(status_code=HTTPStatus.FORBIDDEN, detail="This user had been deleted.")

    if user.locktime:
        raise HTTPException(status_code=HTTPStatus.FORBIDDEN, detail="This user has already been locked.")

    update_schema: UpdateUser = UpdateUser(locktime=datetime.datetime.now())

    user: models.User = await user_repo.update(data=update_schema,
                                               id=user_id)
    return user


@router.patch(path="/{user_id}/release_lock", response_model=LockUser)
@exception_processing
async def release_lock_user(user_id: uuid.UUID):
    """Returns null locktime and user_id after user release."""

    user_repo: SqlAlchemyRepository = SqlAlchemyRepository(db_manager.get_session, model=models.User)

    user: models.User = await user_repo.get_single(id=user_id)

    if user.deleted_at:
        raise HTTPException(status_code=HTTPStatus.FORBIDDEN, detail="This user had been deleted.")

    if not user.locktime:
        raise HTTPException(status_code=HTTPStatus.FORBIDDEN, detail="This user has not been locked.")

    update_schema: UpdateUser = UpdateUser(locktime=None)

    user: models.User = await user_repo.update(data=update_schema,
                                               exclude_none=False,
                                               id=user_id)
    return user
