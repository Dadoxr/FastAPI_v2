"""
Main application file
"""

import uvicorn
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.core import settings
from src.core.urls import main_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Add sth action before start app and after end app
    """

    yield


app = FastAPI(
    title="FastAPI_v2",
    description="",
    version="2.0.0",
    debug=settings.DEBUG,
    lifespan=lifespan,
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(router=main_router.rest)
app.include_router(router=main_router.graphql)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8888, reload=settings.DEBUG)
