from fastapi import FastAPI
from database import init_db, close_db
from contextlib import asynccontextmanager
from routers.users_router import router as user_router
from routers.posts_router import router as post_router
from typing import AsyncIterator

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    await init_db()   # Veritabanı bağlantısı
    yield
    await close_db()  # Veritabanı kapatma işlemi

app = FastAPI(lifespan=lifespan)

app.include_router(post_router, prefix="/posts")
app.include_router(user_router, prefix="/users")