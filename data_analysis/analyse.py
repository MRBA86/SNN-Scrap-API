from fastapi import HTTPException, status
import pandas as pd
from crud_news import get_all_news
import logging

logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename='./logs/app-logs.log')

data = get_all_news()
def date_category_size():
    if data:
        try:
            df = pd.DataFrame(data)
            df['published_date'] = df['published_date'].dt.strftime('%Y-%m-%d')
            df.drop(['image_url', 'news_url', 'title', 'news_lead'], axis=1, inplace=True)
            date_cat_count = df.groupby('published_date')['news_category'].value_counts()
            dict_count = pd.Series.to_dict(date_cat_count)
            result = list()
            for key, value in dict_count.items():
                result.append({'date_category': key, 'count': value})
            return result
        except Exception as e:
            logging.error(f'There is a problem : {e}')
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    logging.error('Data Not Found')
    raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Data not Found ')
def pct_change_cate_date():
    if data:
        try:
            df = pd.DataFrame(data)
            df['published_date'] = df['published_date'].dt.strftime('%Y-%m-%d')
            df.drop(['image_url', 'news_url', 'title', 'news_lead'], axis=1, inplace=True)
            date_cat_count = df.groupby('published_date')['news_category'].value_counts()
            pct_change = date_cat_count.pct_change()
            dict_pct_change = pd.Series.to_dict(pct_change)
            result_pct = list()
            for key, value in dict_pct_change.items():
                result_pct.append({'date_category': key, 'pct_change': value})
            return result_pct
        except Exception as e:
            logging.error(f'There is a problem : {e}')
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    logging.error('Data Not Found')
    raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Data not Found ')

def rolling_Avg_cate_date():
    if data:
        try:
            df = pd.DataFrame(data)
            df['published_date'] = df['published_date'].dt.strftime('%Y-%m-%d')
            df.drop(['image_url', 'news_url', 'title', 'news_lead'], axis=1, inplace=True)
            date_cat_count = df.groupby('published_date')['news_category'].value_counts()
            rolling_Avg = date_cat_count.rolling(window=2).mean()
            dict_rolling_Avg = pd.Series.to_dict(rolling_Avg)
            result_rolling_avg = list()
            for key, value in dict_rolling_Avg.items():
                result_rolling_avg.append({'date_category': key, 'rolling_Avg': value})
            return result_rolling_avg
        except Exception as e:
            logging.error(f'There is a problem : {e}')
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    logging.error('Data Not Found')
    raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Data not Found ')
def rolling_Std_cate_date():
    if data:
        try:
            df = pd.DataFrame(data)
            df['published_date'] = df['published_date'].dt.strftime('%Y-%m-%d')
            df.drop(['image_url', 'news_url', 'title', 'news_lead'], axis=1, inplace=True)
            date_cat_count= df.groupby('published_date')['news_category'].value_counts()
            rolling_Std_data = date_cat_count.rolling(window=2).std()
            dict_rolling_Std_data = pd.Series.to_dict(rolling_Std_data)
            result_rolling_Std = list()
            for key, value in dict_rolling_Std_data.items():
                result_rolling_Std.append({'date_category': key, 'rolling_Std_data': value})
            return result_rolling_Std
        except Exception as e:
            logging.error(f'There is a problem : {e}')
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    logging.error('Data Not Found')
    raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Data not Found ')