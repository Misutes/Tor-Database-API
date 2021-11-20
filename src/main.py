import logging

import inject
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from repositories.mongo_repository import TorRepository
from routers.frontend_router import router as fe_router
from routers.tor_router import router as tor_router
from settings import Settings
from utils.exceptions import set_exceptions_handler
from utils.util import remove_file

app = FastAPI()
set_exceptions_handler(app)
app.include_router(tor_router)
app.include_router(fe_router)


def config(binder):
    engine = AsyncIOMotorClient(Settings.MONGO_ADDRESS)
    database = engine[Settings.MONGO_DATABASE][Settings.MONGO_COLLECTION]
    repo = TorRepository(database)
    binder.bind(TorRepository, repo)


@app.on_event("startup")
async def startup():
    inject.configure(config)


@app.on_event("shutdown")
async def shutdown():
    remove_file()
    logging.info("App is closed")
