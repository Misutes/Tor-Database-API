import os

from fastapi import APIRouter, Depends, Form
from starlette.requests import Request
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from services.tor_service import get_service, TorService

router = APIRouter()
router.mount("/static", StaticFiles(directory="src/routers/frontend/static"), name="static")

templates = Jinja2Templates(directory="src/routers/frontend/templates")


def tor_service():
    return get_service()


@router.get("/")
async def get_page(
    request: Request
):
    return templates.TemplateResponse("main_page.html", {"request": request})


@router.get("/file.txt")
async def get_file(
        count: int,
        service: TorService = Depends(tor_service)
):
    path = os.path.join(os.path.abspath(os.path.dirname("src")), 'file.txt')
    await service.get_file(path, count)
    return FileResponse(path, media_type='application/octet-stream')
