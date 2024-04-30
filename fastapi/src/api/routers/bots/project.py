import uuid
from http import HTTPStatus
from typing import List

from fastapi import APIRouter, HTTPException

from src.database import models
from src.database.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.database.session_manager import db_manager
from src.schema.bots.project import ResponseProject, CreateProject

router = APIRouter(
    prefix="/projects",
    tags=["projects"],
)


@router.get(path="", response_model=List[ResponseProject])
async def get_projects():
    try:
        projects: List[models.Project] = await SqlAlchemyRepository(db_manager.get_session,
                                                                    model=models.Project).get_multi()
        return projects
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))


@router.get(path="/{project_id}", response_model=ResponseProject)
async def get_project(project_id: uuid.UUID):
    try:
        projects: List[models.Project] = await SqlAlchemyRepository(db_manager.get_session,
                                                                    model=models.Project).get_single(id=project_id)
        return projects
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))


@router.post(path="", response_model=ResponseProject)
async def create_project(data: CreateProject):
    try:
        project: models.Project = await SqlAlchemyRepository(db_manager.get_session,
                                                             model=models.Project).create(data)
        return project
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))
