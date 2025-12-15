from sqlalchemy.orm import Session
import uvicorn
from fastapi import FastAPI, Depends, HTTPException, Query
from models import Base, Book
from database import SessionLocal, engine
from crud import create_book, update_book
from schemas import BookCreate, BookRead, BookUpdate
from typing import Any

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/books/", response_model=BookRead)
def add_new_book(book: BookCreate, db: Session = Depends(get_db)) -> Any:
    return create_book(db, book)

@app.get("/books/", response_model=list[BookRead])
async def get_all_books(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    if books is None:
        raise HTTPException(status_code=404, detail="No books were found")
    return books

@app.delete("/books/{book_id}")
async def delete_book_by_id(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return {"message": "Item deleted"}

@app.put("/books/{book_id}", response_model=BookRead)
async def update_book_by_id(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return update_book(db, db_book, book)

@app.get("/book/search/", response_model=list[BookRead])
async def search_books(
    title: str | None = Query(None, description="Search by book title"),
    author: str | None = Query(None, description="Search by author name"),
    year: int | None = Query(None, description="Search by publication year"),
    db: Session = Depends(get_db)
):
    query = db.query(Book)
    
    if title:
        query = query.filter(Book.title.contains(title))
    if author:
        query = query.filter(Book.author.contains(author))
    if year:
        query = query.filter(Book.year == year)
    
    books = query.all()
    
    if not books:
        raise HTTPException(status_code=404, detail="No books found matching the search criteria")
    
    return books

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)