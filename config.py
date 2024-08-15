from fastapi import FastAPI, status
from database import initialize_db
from Scrap_News.scrap import scrap_news
from crud_news import get_all_news, get_news
from data_analysis.analyse import category_analyse

scrap_api = FastAPI()

@scrap_api.on_event('startup')
async def startup_event():
    initialize_db()
    scrap_news()
@scrap_api.get("/news/{news_id}", status_code=status.HTTP_200_OK)
async def news(news_id: int):
    return get_news(news_id)

@scrap_api.get('/news/', status_code=status.HTTP_200_OK)
async def all_news():
    return get_all_news()

@scrap_api.get('/analyse/', status_code=status.HTTP_200_OK)
async def analyse_category():
    return category_analyse()