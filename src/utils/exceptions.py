import http

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from starlette.requests import Request


def set_exceptions_handler(app: FastAPI):
    @app.exception_handler(ValidationError)
    async def validation_error(requests: Request, exc: ValidationError):
        return ORJSONResponse(status_code=http.HTTPStatus.BAD_REQUEST, content=exc.msg)

    @app.exception_handler(DecryptError)
    async def decrypt_error(requests: Request, exc: DecryptError):
        return ORJSONResponse(
            status_code=http.HTTPStatus.UNPROCESSABLE_ENTITY, content=exc.msg
        )

    @app.exception_handler(InvalidToken)
    async def invalid_token(requests: Request, exc: InvalidToken):
        return ORJSONResponse(status_code=http.HTTPStatus.FORBIDDEN, content=exc.msg)


class ValidationError(Exception):
    def __init__(self, msg):
        self.msg = msg


class DecryptError(Exception):
    msg = "Bad token"


class InvalidToken(Exception):
    msg = "Invalid token"
