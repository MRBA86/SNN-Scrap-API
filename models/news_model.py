from sqlalchemy import Column, Integer, String, Text, DateTime
from database.sql_db import Base


class News(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True)
    news_url = Column(Text)
    image_url = Column(String(255))
    title = Column(String(255))
    news_lead = Column(String(255))
    news_id = Column(Integer, unique=True)
    news_category = Column(String(128))
    published_date = Column(DateTime)
