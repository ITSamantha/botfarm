from http import HTTPStatus

from fastapi import Request
import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError, HTTPException
from starlette.responses import JSONResponse

from src.api.routers.base import create_app_routers
from src.config.app.config import settings_app


def get_application() -> FastAPI:
    application = FastAPI(
        title=settings_app.APP_NAME,
        debug=settings_app.DEBUG,
        version=settings_app.APP_VERSION
    )
    create_app_routers(application)

    return application


app = get_application()

if __name__ == "__main__":
    uvicorn.run(
        app=settings_app.UVICORN_APP_NAME,
        host=settings_app.UVICORN_HOST,
        port=settings_app.UVICORN_PORT,
        reload=settings_app.UVICORN_RELOAD
    )
