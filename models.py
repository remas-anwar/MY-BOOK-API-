from sqlalchemy import Column, Integer, String, Date
from database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    publishedDate = Column(Date, nullable=False)
    numberOfPages = Column(Integer, nullable=False)