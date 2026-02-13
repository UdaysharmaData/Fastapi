from pydantic import BaseModel , Field , StrictStr
from typing import Optional

class Employee(BaseModel):
    id :int = Field(...,gt=0)
    name : str = Field(...,min_length=3,max_length=50)
    department : str = Field(...,min_length=3,max_length=50)
    age :int = Field(...,gt=0,lt=70)
    blood_group : Optional[StrictStr] = Field(default=None)


