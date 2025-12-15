from sqlalchemy.orm import Session

from models import Book
from schemas import BookCreate, BookUpdate

def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def create_book(db: Session, book: BookCreate):
    db_book = Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def update_book(db: Session, db_book: Book, updates: BookUpdate):
    db_book.title = updates.title
    db_book.author = updates.author
    db_book.year = updates.year
    db.commit()
    db.refresh(db_book)
    return db_book