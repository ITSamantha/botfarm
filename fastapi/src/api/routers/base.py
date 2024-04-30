from fastapi import FastAPI

from src.api.routers import bots


def create_app_routers(app: FastAPI):
    app.include_router(bots.router)
    return app
