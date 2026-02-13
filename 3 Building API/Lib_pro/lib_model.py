from pydantic import BaseModel

class issue_model(BaseModel):

    student_roll : int
    student_name : str
    stud_class : int
    book_issue : str
    book_issue_date : str
    issue_qty : int

class Library(BaseModel):

    book_id : int
    book_name : str
    qty : int