from datetime import datetime

from pydantic import BaseModel

class NewsBase(BaseModel):
    news_url: str
    image_url: str
    title: str
    news_lead: str
    news_id: int
    news_category: str
    published_date: datetime

class CreateNews(NewsBase):
    pass

class News(NewsBase):
    id: int

    class Config:
        orm_mode = True