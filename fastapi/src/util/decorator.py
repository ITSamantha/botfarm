from functools import wraps
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from http import HTTPStatus


def exception_processing(func):
    """Decorator to handle exceptions in FastAPI endpoints."""

    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except HTTPException as http_ex:
            raise http_ex
        except SQLAlchemyError as e:
            raise HTTPException(
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                detail=str(e)
            )
        except Exception as e:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail=str(e)
            )

    return wrapper
