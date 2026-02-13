from pydantic import BaseModel , Field , EmailStr
from typing import List

class EmployeeBase(BaseModel):

    name : str
    email : EmailStr

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(EmployeeBase):
    pass

class Employeeout(EmployeeBase):
    id:int

    class Config:
        orm_mode = True

