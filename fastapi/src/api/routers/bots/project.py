import datetime
import uuid
from typing import List

from fastapi import APIRouter

from src.database import models
from src.database.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.database.session_manager import db_manager
from src.schema.bots.project import ResponseProject, CreateProject, UpdateProject
from src.schema.core import DeleteSchema
from src.util.decorator import exception_processing

router: APIRouter = APIRouter(
    prefix="/projects",
    tags=["projects"],
)


@router.get(path="", response_model=List[ResponseProject])
@exception_processing
async def get_projects():
    """Returns the list of user projects."""

    projects: List[models.Project] = await SqlAlchemyRepository(db_manager.get_session,
                                                                model=models.Project).get_multi(deleted_at=None)
    return projects


@router.post(path="", response_model=ResponseProject)
@exception_processing
async def create_project(data: CreateProject):
    """Returns created with the given data project."""

    project: models.Project = await SqlAlchemyRepository(db_manager.get_session,
                                                         model=models.Project).create(data)
    return project


@router.patch(path="/{project_id}", response_model=ResponseProject)
@exception_processing
async def update_project(project_id: uuid.UUID, data: UpdateProject):
    """Returns updated with the given data project."""

    project: models.Project = await SqlAlchemyRepository(db_manager.get_session,
                                                         model=models.Project).update(data, id=project_id)
    return project


@router.get(path="/{project_id}", response_model=ResponseProject)
@exception_processing
async def get_project_by_id(project_id: uuid.UUID):
    """Returns the project with the given project_id."""

    project: models.Project = await SqlAlchemyRepository(db_manager.get_session,
                                                         model=models.Project).get_single(id=project_id)
    return project


@router.delete(path="/{project_id}")
@exception_processing
async def delete_project(project_id: uuid.UUID):
    """Returns deleted project."""

    delete_schema: DeleteSchema = DeleteSchema(deleted_at=datetime.datetime.now())

    project: models.Project = await SqlAlchemyRepository(db_manager.get_session, model=models.Project) \
        .update(data=delete_schema,
                id=project_id)
    # todo: cascade delete for users
    return project
