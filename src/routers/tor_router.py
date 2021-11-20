import http
from typing import Any, List

from fastapi import APIRouter, Depends
from starlette.responses import Response

from models import UpdateUsersData, User
from services.tor_service import TorService, get_service
from services.validation_service import (
    check_service_field,
    check_service_value,
    check_user_token,
)

router = APIRouter(dependencies=[Depends(check_user_token)])


def tor_service():
    return get_service()


@router.post("/createUsers")
async def create_users(users: List[User], service: TorService = Depends(tor_service)):
    await service.creat_users(users)
    return Response(status_code=http.HTTPStatus.OK, content="Users created")


@router.get("/getUsers")
async def get_users(
    where_name: str,
    fields: List[str] = [],
    where_value: Any = None,
    count: int = 1,
    service: TorService = Depends(tor_service),
):
    check_service_field(where_name)
    check_service_value(where_value)

    return await service.get_users(fields, where_name, where_value, count)


@router.put("/updateUsers")
async def update_users(
    update_data: UpdateUsersData, service: TorService = Depends(tor_service)
):
    check_service_field(update_data.where_field)
    check_service_value(update_data.where_value)

    check_service_field(update_data.field_name)
    check_service_value(update_data.field_value)

    await service.update_users(update_data)
    return Response(status_code=http.HTTPStatus.OK, content="Users updated")


@router.get("/getRegister")
async def get_register(
    where_name: str,
    fields: List[str] = [],
    count: int = 1,
    service: TorService = Depends(tor_service),
):
    check_service_field(where_name)

    return await service.get_users(fields, where_name, None, count)
