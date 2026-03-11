from fastapi import FastAPI
from pydantic import BaseModel
from app.logic import is_elgible_for_loan

app = FastAPI()

class Applicant(BaseModel):
    income:float
    age:int
    employement_status : str


@app.post("/loan_eligibility")
def check_elgibility(applicant:Applicant):
    eligibility = is_elgible_for_loan(
        income=applicant.income,
        age=applicant.age,
        employement_status=applicant.employement_status
    )

    return {'eligibility':eligibility}