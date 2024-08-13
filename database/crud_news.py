from database.sql_db import get_db
from models.news_model import News
from schemas.news_schema import CreateNews

mydb = get_db()
def is_news_exist(news_id: int):
    db_news = mydb.query(News).filter(News.news_id == news_id).first()
    if db_news:
        return True
    return False
def save_news(news_jadid: CreateNews):
    db_new_news = News(news_url=news_jadid['news_url'], image_url=news_jadid['image_url'], title=news_jadid['title'],
                   news_lead=news_jadid['news_lead'], news_id=news_jadid['news_id'],
                   news_category=news_jadid['news_category'], published_date=news_jadid['published_date'])
    mydb.add(db_new_news)
    mydb.commit()
    mydb.refresh(db_new_news)
