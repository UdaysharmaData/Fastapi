from fastapi import FastAPI , HTTPException
from lib_model import Library , issue_model
from typing import List

app = FastAPI()

lib_db :List[Library]= []

# 1 Retrieve all books
@app.get('/books',response_model=List[Library])
def get_all_books():
    return lib_db

# 2. Get specific book
@app.get("/get_book/{id}",response_model=Library)
def get_book(id:int):
    for index,book in enumerate(lib_db):
        if id == book.book_id:
            return lib_db[index]
    
    raise HTTPException(status_code=400,detail="Book not found")



# 3. Add a new book
@app.post("/add_books",response_model=Library)
def add_books(new_book:Library):
    for book in lib_db:
        if (book.book_id == new_book.book_id) or (book.book_name == new_book.book_name):
            raise HTTPException(status_code=400,detail="Book Already Exists")
    
    lib_db.append(new_book)
    return new_book

# 4 . Delete a book
@app.delete("/delete_book/{id}")
def delete_book(id:int):
    for index , book in enumerate(lib_db):
        if book.book_id == id:
            del lib_db[index]
            return {"message":"Book deleted successfully"}
    raise HTTPException(status_code=400,detail="Book Not found")

# 5. Update existing book
@app.put("/update_book/{id}",response_model=Library)
def update_book(id:int,updated_book:Library):
    for index , book in enumerate(lib_db):
        if book.book_id == id:
            lib_db[index] = updated_book
            return updated_book
    raise HTTPException(status_code=400,detail="Book not found")
    
