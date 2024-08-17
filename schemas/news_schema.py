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

class NewsCategory(BaseModel):
    category_date: tuple
    count: int

class NewsPctChange(BaseModel):
    category_date: list
    pct_change: float | None

class NewsRollingAvg(BaseModel):
    category_date: list
    rolling_avg: float | None

class NewsRollingStd(BaseModel):
    category_date: tuple
    rolling_std: float | None