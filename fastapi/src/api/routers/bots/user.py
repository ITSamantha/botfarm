import uuid
from http import HTTPStatus
from typing import List

from fastapi import APIRouter, HTTPException

from src.database import models
from src.database.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.database.session_manager import db_manager
from src.schema.bots.user import ResponseUser

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get(path="", response_model=List[ResponseUser])
async def get_users():
    """Returns the list of users."""

    try:
        users: List[models.User] = await SqlAlchemyRepository(db_manager.get_session,
                                                              model=models.User).get_multi()
        return users
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))


@router.get(path="/{user_id}", response_model=ResponseUser)
async def get_user_by_id(user_id: uuid.UUID):
    """Returns the user with the given user_id."""

    try:
        user: models.User = await SqlAlchemyRepository(db_manager.get_session,
                                                       model=models.User).get_single(id=user_id)
        return user
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))
