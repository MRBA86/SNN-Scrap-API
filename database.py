from fastapi import HTTPException, status
import mysql.connector
import logging

# Connect to MySQL
class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost", user="root", password="R00t1234", database="snn_scrap")
def initialize_db():
    db = Database()
    if db.conn.is_connected():
        try:
            cursor = db.conn.cursor()
            query = """CREATE TABLE IF NOT EXISTS news (
                id int primary key auto_increment ,
                news_url text,
                image_url varchar(255) ,
                title varchar(255),
                news_lead text,
                news_id int ,
                news_category varchar(128),
                published_date datetime )"""
            cursor.execute(query)
            db.conn.close()
        except Exception as e:
            logging.error(f'There is a problem : {e}')
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    else:
        logging.error('Database is Not Connected')
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Database is Not Connected')
