from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal, engine, Base
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets

# إنشاء الجداول في قاعدة البيانات
Base.metadata.create_all(bind=engine)

app = FastAPI()

# السماح بالاتصال من أي مكان (في حال استخدمنا الواجهة لاحقًا)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Basic Auth
security = HTTPBasic()
def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "remas")
    correct_password = secrets.compare_digest(credentials.password, "1234")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )

# دالة لإعطاء جلسة قاعدة البيانات في كل طلب
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 1. إضافة كتاب جديد
@app.post("/api/books", response_model=schemas.BookOut, dependencies=[Depends(authenticate)])
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# 2. جلب جميع الكتب (مع Pagination)
@app.get("/api/books", response_model=list[schemas.BookOut], dependencies=[Depends(authenticate)])
def get_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Book).offset(skip).limit(limit).all()

# 3. جلب تفاصيل كتاب معين
@app.get("/api/books/{book_id}", response_model=schemas.BookOut, dependencies=[Depends(authenticate)])
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

# 4. تحديث كتاب
@app.put("/api/books/{book_id}", response_model=schemas.BookOut, dependencies=[Depends(authenticate)])
def update_book(book_id: int, book_update: schemas.BookUpdate, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    for key, value in book_update.dict(exclude_unset=True).items():
        setattr(book, key, value)
    db.commit()
    db.refresh(book)
    return book

# 5. حذف كتاب
@app.delete("/api/books/{book_id}", dependencies=[Depends(authenticate)])
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return {"message": "Book deleted successfully"}