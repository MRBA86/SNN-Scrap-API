import pandas as pd
from crud_news import get_all_news

data = get_all_news()
def category_analyse():
    if data:
        df = pd.DataFrame(data)
        df['published_date'] = df['published_date'].dt.strftime('%Y-%m-%d')
        df['count'] = df.groupby('published_date')['news_category'].value_counts()
        category_summary = df.groupby('news_category')['count'].sum().reset_index()
        date_summary = df.groupby('published_date')['count'].sum().reset_index()
        return df