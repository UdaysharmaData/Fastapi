from fastapi import FastAPI , HTTPException
from models import Employee
from typing import List

employees_db:List[Employee] = []

app = FastAPI()

# 1. Read all the employees
@app.get('/employees',response_model=List[Employee])
def get_employee():
    return employees_db

# 2. Read specific Employee
@app.get('/employee/{emp_id}',response_model=Employee)
def get_emp(emp_id:int):
    for index,emp in enumerate(employees_db):
        if emp_id == emp.id:
            return employees_db[index]
    
    raise HTTPException(status_code=404,detail="Employee not found")


#3. Add Employee
@app.post('/employees',response_model=Employee)
def add_employee(new_emp:Employee):
    for employee in employees_db:
        if employee.id == new_emp.id:
            raise HTTPException(status_code=400, detail="Employee already Exists")
    
    employees_db.append(new_emp)

    return new_emp


# 4. Update Employee

@app.put('/update_employee/{emp_id}',response_model=Employee)
def update_employee(emp_id:int,updated_emp:Employee):
    for index,employee in enumerate(employees_db):
        if employee.id == emp_id:    
            employees_db[index] = updated_emp
            return updated_emp
    raise HTTPException(status_code=404,detail="Employee not found")


# 5. Delete Employee

@app.delete('/delete_emp/{emp_id}')
def delete_emp(emp_id:int):
    for index,emp in enumerate(employees_db):
        if emp.id == emp_id:
            del employees_db[index]
            return {"message":"Employee deleted successfully"}
        
    raise HTTPException(status_code=404,detail="Employee not found")
