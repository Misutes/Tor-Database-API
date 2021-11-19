import os
from typing import Optional, List

from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse, FileResponse

from models import UpdatedEmails
from services.tor_service import get_service, TorService

router = APIRouter()


def tor_service():
    return get_service()


@router.get("/getUsers")
async def get_users(
        state: Optional[int] = None,
        count: Optional[int] = None,
        service: TorService = Depends(tor_service)
):
    result = await service.get_user(state, count)
    if isinstance(result, list):
        return result
    return JSONResponse(
        status_code=400,
        content=f"Users with state different '{state}' in db: {result}"
    )


@router.put("/updateUsers")
async def update_users(
        data: UpdatedEmails,
        service: TorService = Depends(tor_service)
):
    if data.state not in (0, 1, 2):
        return JSONResponse(
            status_code=400,
            content='invalid state'
        )

    msg = "emails were updated"
    if invalid_emails := await service.update_users(data.emails, data.state):
        msg = f"emails: {invalid_emails} wasn't updated"

    return JSONResponse(
        status_code=200,
        content=msg
    )


@router.get("/getRegister")
async def get_register(
        count: Optional[int] = None,
        service: TorService = Depends(tor_service)
):
    try:
        return await service.get_register(count)
    except ValueError:
        return JSONResponse(
            status_code=404,
            content="Users with state '1' not found"
        )


