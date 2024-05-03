from functools import wraps
from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError


def exception_processing(func):
    """Decorator for processing exceptions for routes."""

    @wraps(func)
    async def inner(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except HTTPException as e:
            raise HTTPException(status_code=e.status_code, detail=str(e))
        except SQLAlchemyError as e:
            raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail="Database error.")
        except Exception as e:
            raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))

    return inner
