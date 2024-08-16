import logging
from fastapi import HTTPException, status
from database import Database
from schemas.news_schema import CreateNews

def is_news_exist(news_id: int):
    db = Database()
    try:
        cursor = db.conn.cursor()
        query = "select * from news where news_id = %s"
        cursor.execute(query, (news_id,))
        db_news = cursor.fetchall()
        if db_news:
            return True
        return False
    except Exception as e:
        logging.error(f'There is a problem : {e}')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    finally:
        db.conn.close()
def save_news(news_jadid: CreateNews):
    db = Database()
    try:
        cursor = db.conn.cursor()
        query = """
                Insert into news (news_url, image_url, title, news_lead, news_id, news_category, published_date )
                values (%s, %s, %s, %s, %s, %s, %s)      
            """
        values = (news_jadid['news_url'], news_jadid['image_url'], news_jadid['title'], news_jadid['news_lead'],
                  news_jadid['news_id'], news_jadid['news_category'], news_jadid['published_date'])
        cursor.execute(query, values)
        db.conn.commit()
    except Exception as e:
        logging.error(f'There is a problem : {e}')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    finally:
        db.conn.close()

def get_all_news():
    db = Database()
    try:
        cursor = db.conn.cursor()
        query = "select * from news "
        cursor.execute(query)
        news_list = cursor.fetchall()
        if news_list:
            total_news = list()
            for row in news_list:
                total_news.append({'id': row[0], 'news_url': row[1], 'image_url': row[2], 'title': row[3],
                                   'news_lead': row[4], 'news_id': row[5], 'news_category': row[6],
                                   'published_date': row[7]})
            return total_news
        else:
            logging.error('there is not any news in database')
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='there is not any news in database')
    except Exception as e:
        logging.error(f'There is a problem : {e}')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    finally:
        db.conn.close()

def get_news(news_id):
    db = Database()
    try:
        cursor = db.conn.cursor()
        query = "select * from news where news_id = %s"
        cursor.execute(query, (news_id,))
        db_news = cursor.fetchone()
        if db_news :
            return {'id': db_news[0], 'news_url': db_news[1], 'image_url': db_news[2], 'title': db_news[3],
                    'news_lead': db_news[4], 'news_id': db_news[5], 'news_category': db_news[6],
                    'published_date': db_news[7]}
        else:
            logging.error("News couldn't find")
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="News couldn't find")
    except Exception as e:
        logging.error(f'There is a problem : {e}')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    finally:
        db.conn.close()
