import os

from fastapi import APIRouter, Depends
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

from services.tor_service import TorService, get_service
from services.validation_service import check_service_field

router = APIRouter()
router.mount(
    "/static", StaticFiles(directory="src/routers/frontend/static"), name="static"
)

templates = Jinja2Templates(directory="src/routers/frontend/templates")


def tor_service():
    return get_service()


@router.get("/")
async def get_page(request: Request):
    return templates.TemplateResponse("main_page.html", {"request": request})


@router.get("/file.txt")
async def get_file(
    where_name: str,
    fields: str,
    count: int = 1,
    service: TorService = Depends(tor_service),
):
    check_service_field(where_name)

    path = os.path.join(os.path.abspath(os.path.dirname("src")), "file.txt")
    await service.get_file(path, fields, where_name, count)
    return FileResponse(path, media_type="application/octet-stream")
