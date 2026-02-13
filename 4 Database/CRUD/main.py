from fastapi import FastAPI , HTTPException , Depends
from sqlalchemy.orm import Session
from database import engine , SessionLocal , Base
from typing import List
import models,schemas,crud

Base.metadata.create_all(bind = engine)

app = FastAPI()

#  dependency with database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# endpoints

# 1. to create an Employee

@app.post("/create_employee",response_model=schemas.Employeeout)
def create_employee(employee:schemas.EmployeeCreate,db:Session = Depends(get_db)):
    return crud.create_employee(db=db,employee=employee)


# 2 .  Read all the Employees

@app.get("/employees",response_model=List[schemas.Employeeout])
def get_employees(db:Session = Depends(get_db)):
    return crud.get_employees(db=db)

# 3. get specific employee

@app.get("/employee/{emp_id}",response_model=schemas.Employeeout)
def get_employee(emp_id:int,db:Session = Depends(get_db)):

    employee = crud.get_employee(db=db,emp_id=emp_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee does not Exist")
    return employee


# 4. Update Employee

@app.put("/update_employee/{emp_id}",response_model=schemas.Employeeout)
def update_employee(emp_id:int , employee:schemas.EmployeeUpdate , db:Session = Depends(get_db)):
    
    db_employee = crud.update_employee(db=db,emp_id=emp_id,employee=employee)

    if db_employee is None:
        raise HTTPException(status_code=404,detail="Emplotee does not exist")
    return db_employee


# 5. delete an employee
@app.delete("/delete_employee/{emp_id}",response_model=dict)
def delete_employee(emp_id:int,db:Session = Depends(get_db)):
    employee = crud.delete_employee(db=db,emp_id=emp_id)

    if employee is None:
        raise HTTPException(status_code=404,detail="Emplotee does not exist")
    
    return {"message":"Employee deleted successfully"}


