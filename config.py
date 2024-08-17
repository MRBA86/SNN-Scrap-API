from fastapi import FastAPI
from database import initialize_db
from router import news
from router import analysis

scrap_api = FastAPI()
scrap_api.include_router(news.router)
scrap_api.include_router(analysis.router)

@scrap_api.on_event('startup')
async def startup_event():
    initialize_db()