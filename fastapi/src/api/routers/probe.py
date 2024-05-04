from http import HTTPStatus

from fastapi import APIRouter
from starlette.responses import JSONResponse

router: APIRouter = APIRouter(
    prefix="/probes",
    tags=["probes"],
)


@router.get(path="/liveness")
async def liveness_probe():
    content = {"status": "ok"}
    return JSONResponse(content=content, status_code=HTTPStatus.OK)


@router.get(path="/readiness")
async def readiness_probe():
    # todo: change functionality
    content = {"status": "ok"}
    return JSONResponse(content=content, status_code=HTTPStatus.OK)


@router.get(path="/startup")
async def startup_probe():
    # todo: change functionality
    content = {"status": "ok"}
    return JSONResponse(content=content, status_code=HTTPStatus.OK)
