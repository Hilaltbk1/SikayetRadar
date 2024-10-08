from typing import AsyncIterator
from fastapi import FastAPI
from database import init_db, close_db

from contextlib import asynccontextmanager

from routers import posts_router, users_router


@asynccontextmanager
async def lifespan( app :FastAPI) -> AsyncIterator[None]:
    await init_db()
    yield
    await close_db()

app = FastAPI(lifespan=lifespan)

app.include_router(posts_router, prefix="/posts")
app.include_router(users_router, prefix="/users")
