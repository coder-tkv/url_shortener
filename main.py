from contextlib import asynccontextmanager
from fastapi import FastAPI, Body, status
from fastapi.responses import RedirectResponse
from database.db import engine
from database.models import Base
from service import generate_shore_url


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)


@app.post('/short_url')
async def generate_slug(long_url: str = Body(embed=True)):
    new_slug = await generate_shore_url(long_url)
    return {'data': new_slug}


@app.get('/{slug}')
async def redirect_to_url(slug: str):
    return RedirectResponse(url=..., status_code=status.HTTP_302_FOUND)