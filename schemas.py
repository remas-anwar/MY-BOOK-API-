from pydantic import BaseModel
from datetime import date

class BookBase(BaseModel):
    title: str
    author: str
    publishedDate: date
    numberOfPages: int

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    publishedDate: date | None = None
    numberOfPages: int | None = None

class BookOut(BookBase):
    id: int

    class Config:
        from_attributes = True