from http import HTTPStatus

from fastapi import APIRouter, Request, HTTPException, Depends
from starlette.responses import JSONResponse

from src.schema.bots.auth import LoginUser
from src.util.dependencies.auth import Auth
from src.util.jwt.jwt_auth import format_jwt_response
from src.util.use_case.login import LoginUseCase

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/login")
async def login(data: LoginUser):
    try:
        access_token = await LoginUseCase.login(data)
    except Exception as e:
        raise HTTPException(detail=str(e), status_code=HTTPStatus.UNAUTHORIZED)

    return format_jwt_response(access_token)


@router.post("/logout")
async def logout(request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)
    response: JSONResponse = JSONResponse(status_code=200, content={"detail": "You have successfully logged out."})
    response.delete_cookie('jwt_access_token')
    return response
