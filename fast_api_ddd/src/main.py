from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy.orm import clear_mappers

from account.adapter.mapper import start_mappers as user_start_mappers
from account.entrypoints.router import router as account_router
from backbone.adapter.abstract_data_model import MAPPER_REGISTRY
from backbone.infrastructure.databases.postgres_connection import DEFAULT_ENGIN


@asynccontextmanager
async def lifespan(app: FastAPI):
    user_start_mappers()
    MAPPER_REGISTRY.metadata.create_all(DEFAULT_ENGIN)
    MAPPER_REGISTRY.configure()
    yield
    clear_mappers()


app = FastAPI(lifespan=lifespan)
app.include_router(account_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run('main:app', host="0.0.0.0", port=8000)
