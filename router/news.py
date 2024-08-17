from fastapi import APIRouter, HTTPException, status
from crud_news import get_all_news, get_news
from Scrap_News.scrap import scrap_news
import logging

router = APIRouter(
    prefix='/news',
    tags=["news"])

@router.post("/", status_code=status.HTTP_201_CREATED)
async def scraping_news():
    count = scrap_news()
    if count == 0:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail='No New News Has Been Published')
    return {'Total News Scraped': count}
@router.get("/{news_id}", status_code=status.HTTP_200_OK)
async def news(news_id: int):
    try:
        return get_news(news_id)
    except Exception as e:
        logging.error(f'There is a problem : {e}')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
@router.get('/all_news/', status_code=status.HTTP_200_OK)
async def all_news():
    try:
        return get_all_news()
    except Exception as e:
        logging.error(f'There is a problem : {e}')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
