import json

from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from database import initialize_db
from Scrap_News.scrap import scrap_news
from crud_news import get_all_news, get_news
from data_analysis.analyse import date_category_size, pct_change_cate_date, rolling_Avg_cate_date, rolling_Std_cate_date

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

@scrap_api.get('/analyse/category/', status_code=status.HTTP_200_OK)
async def analyse_category():
    return date_category_size()


@scrap_api.get('/pct_change/', status_code=status.HTTP_200_OK)
async def get_pct_change():
    r = pct_change_cate_date()
    print(r)
    return JSONResponse(content={'t': r})

@scrap_api.get('/rolling_avg/', status_code=status.HTTP_200_OK)
async def get_rolling_avg():
    return rolling_Avg_cate_date()
@scrap_api.get('/rolling_std/', status_code=status.HTTP_200_OK)
async def get_rolling_std():
    return rolling_Std_cate_date()