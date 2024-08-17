from fastapi import APIRouter, HTTPException, status
from data_analysis.analyse import date_category_size, news_category_rate, sum_news_in_date, top5_highest_category
from data_analysis.analyse import top5_lowest_category
import logging
router = APIRouter(
    prefix='/analyse',
    tags=["Analayse"])


@router.get('/category_in_date/', status_code=status.HTTP_200_OK)
async def analyse_category():
    try:
        return date_category_size()
    except Exception as e:
        logging.error(f'There is a problem : {e}')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@router.get('/rate_category_news/', status_code=status.HTTP_200_OK)
def get_news_category_rate():
    try:
        return news_category_rate()
    except Exception as e:
        logging.error(f'There is a problem : {e}')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

@router.get('/count_news_by_date/', status_code=status.HTTP_200_OK)
def count_news_by_date():
    try:
        return sum_news_in_date()
    except Exception as e:
        logging.error(f'There is a problem : {e}')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
@router.get('/top5_highest_category/', status_code=status.HTTP_200_OK)
async def get_top5_highest_category():
    try:
        return top5_highest_category()
    except Exception as e:
        logging.error(f'There is a problem : {e}')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

@router.get('/top5_lowest_category/', status_code=status.HTTP_200_OK)
async def get_top5_lowest_category():
    try:
        return top5_lowest_category()
    except Exception as e:
        logging.error(f'There is a problem : {e}')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)