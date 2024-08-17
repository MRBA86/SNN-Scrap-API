from fastapi import HTTPException, status
import pandas as pd
from crud_news import get_all_news
import logging

def base_data():
    data = get_all_news()
    if data:
        try:
            df = pd.DataFrame(data)
            df['published_date'] = df['published_date'].dt.strftime('%Y-%m-%d')
            df.drop(['image_url', 'news_url', 'title', 'news_lead'], axis=1, inplace=True)
            date_cat_count = df.groupby('published_date')['news_category'].value_counts()
            return date_cat_count
        except Exception as e:
            logging.error(f'There is a problem : {e}')
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    logging.error('Data Not Found')
    raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Data not Found ')
def make_new_data():
    data = base_data()
    data1 = pd.Series.to_dict(data)
    new_data = {'Date': [], 'Category': [], 'Count': []}
    for index, value in data1.items():
        new_data['Date'].append(index[0])
        new_data['Category'].append(index[1])
        new_data['Count'].append(value)
    return new_data

def date_category_size():
    try:
        category_data = base_data()
        dict_count = pd.Series.to_dict(category_data)
        result = list()
        for key, value in dict_count.items():
            result.append({'date_category': key, 'count': value})
        return result
    except Exception as e:
        logging.error(f'There is a problem : {e}')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

def news_category_rate():
    try:
        dict_data = make_new_data()
        new_df = pd.DataFrame(dict_data)
        new_df['Date'] = pd.to_datetime(new_df['Date'])
        category_rate = new_df.groupby('Category')['Count'].mean()
        dict_category_rate = pd.Series.to_dict(category_rate)
        result = list()
        for key, value in dict_category_rate.items():
            result.append({'News_Category': key, 'Rate': value})
        return result

    except Exception as e:
        logging.error(f'There is a problem : {e}')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

def sum_news_in_date():
    try:
        dict_data = make_new_data()
        new_df = pd.DataFrame(dict_data)
        new_df['Date'] = pd.to_datetime(new_df['Date'])
        news_date_sum = new_df.groupby('Date')['Count'].sum()
        dict_news_date_sum = pd.Series.to_dict(news_date_sum)
        result = list()
        for key, value in dict_news_date_sum.items():
            result.append({'Date': key, 'Count-of_News': value})
        return result
    except Exception as e:
        logging.error(f'There is a problem : {e}')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

def top5_highest_category():
    try:
        dict_data = make_new_data()
        new_df = pd.DataFrame(dict_data)
        new_df['Date'] = pd.to_datetime(new_df['Date'])
        count_news_category = new_df.groupby('Category')['Count'].sum()
        top_category = pd.Series.sort_values(count_news_category, ascending=False).head()
        dict_top_category = pd.Series.to_dict(top_category)
        result = list()
        for key, value in dict_top_category.items():
            result.append({'News_Category': key, 'Count_of_News': value})
        return result
    except Exception as e:
        logging.error(f'There is a problem : {e}')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
def top5_lowest_category():
    try:
        dict_data = make_new_data()
        new_df = pd.DataFrame(dict_data)
        new_df['Date'] = pd.to_datetime(new_df['Date'])
        count_news_category = new_df.groupby('Category')['Count'].sum()
        low_category = pd.Series.sort_values(count_news_category, ascending=True).head()
        dict_low_category = pd.Series.to_dict(low_category)
        result = list()
        for key, value in dict_low_category.items():
            result.append({'News_Category': key, 'Count_of_News': value})
        return result
    except Exception as e:
        logging.error(f'There is a problem : {e}')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)