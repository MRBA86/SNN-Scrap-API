from fastapi import FastAPI
from database.sql_db import engine, Base
from models import news_model


scrap_api = FastAPI()

news_model.Base.metadata.create_all(bind=engine)


@scrap_api.get("/")
async def test():
    return { "hello" : "world"}