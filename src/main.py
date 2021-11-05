import logging

import inject
from fastapi import FastAPI
from peewee import SqliteDatabase


from routers.tor_router import router as tor_router
from routers.frontend_router import router as fe_router
from repositories.sqlite_repository import TorRepository
from settings import Settings
from utils.util import remove_file

app = FastAPI()
# set_exception_handler(app)
app.include_router(tor_router)
app.include_router(fe_router)


def config(binder):
    repo = TorRepository(Settings.DATABASE)
    binder.bind(TorRepository, repo)


@app.on_event("startup")
async def startup():
    inject.configure(config)


@app.on_event("shutdown")
async def shutdown():
    remove_file()
    logging.info("App is closed")
