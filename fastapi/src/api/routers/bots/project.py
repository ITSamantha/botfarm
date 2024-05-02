import uuid
from http import HTTPStatus
from typing import List

from fastapi import APIRouter, HTTPException

from src.database import models
from src.database.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.database.session_manager import db_manager
from src.schema.bots.project import ResponseProject, CreateProject, UpdateProject

router: APIRouter = APIRouter(
    prefix="/projects",
    tags=["projects"],
)


@router.get(path="", response_model=List[ResponseProject])
async def get_projects():
    """Returns the list of user projects."""

    try:
        projects: List[models.Project] = await SqlAlchemyRepository(db_manager.get_session,
                                                                    model=models.Project).get_multi()
        return projects
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))


@router.get(path="/{project_id}", response_model=ResponseProject)
async def get_project_by_id(project_id: uuid.UUID):
    """Returns the project with the given project_id."""

    try:
        project: models.Project = await SqlAlchemyRepository(db_manager.get_session,
                                                             model=models.Project).get_single(id=project_id)
        return project
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))


@router.post(path="", response_model=ResponseProject)
async def create_project(data: CreateProject):
    """Returns created with the given data project."""

    try:
        project: models.Project = await SqlAlchemyRepository(db_manager.get_session,
                                                             model=models.Project).create(data)
        return project
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))


@router.patch(path="", response_model=ResponseProject)
async def create_project(data: UpdateProject):
    """Returns updated with the given data project."""

    try:
        project: models.Project = await SqlAlchemyRepository(db_manager.get_session,
                                                             model=models.Project).update(data)
        return project
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))
