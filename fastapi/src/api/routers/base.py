from fastapi import FastAPI

from src.api.routers.bots import user, project


def create_app_routers(app: FastAPI):
    app.include_router(user.router)
    app.include_router(project.router)
    return app
