from datetime import date

from pydantic import BaseModel


class News(BaseModel):
    title: str
    date_published: date
    section: str
    country: str
    news_content: str
